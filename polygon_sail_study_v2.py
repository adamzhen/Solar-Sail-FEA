from abaqus import *
from abaqusConstants import *
import __main__
import section
import odbSection
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import job
import sketch
import visualization
import xyPlot
import connectorBehavior
import displayGroupOdbToolset as dgo

import os
import csv
import math
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

if 'Viewport: 1' in session.viewports.keys():
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        titleFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        stateFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        triadFont='-*-verdana-bold-r-normal-*-*-120-*-*-p-*-*-*')

_total_start = time.perf_counter()

STUDY_NO = 2.0

# =====================================================================
# FIXED PARAMETERS
# =====================================================================
N         = 8          # number of polygon sides (fixed)
A_sail    = 9.0        # sail area, m^2
R_hub     = 0.03       # hub circumradius, m
H_hub     = 0.09       # hub extrusion height, m
mesh_hub  = 0.02       # hub mesh seed size, m
mesh_wire = 0.1        # wire mesh seed size, m

# Atmosphere / drag
Cd        = 2.2
mu_earth  = 3.986004418e14   # m^3/s^2
R_earth   = 6371.0e3         # m

# Total mass density (kg/m^3) vs altitude (km).
# 200-275 km: NRLMSISE-00 moderate activity (F10.7=140, Ap=15, ISO 14222
#             Table A.2), log-interpolated to 225/250/275 km.
# 300-400 km: densities implied by the previous pressure table
#             (p = 0.5*Cd*rho*v_orbit^2 with Cd=2.2, circular orbit).
density_dict = {
    200: 2.840e-10,
    225: 1.415e-10,
    250: 7.570e-11,
    275: 3.897e-11,
    300: 1.914e-11,
    325: 1.165e-11,
    350: 7.007e-12,
    375: 4.814e-12,
    400: 2.800e-12}

def drag_pressure(alt_km):
    v2 = mu_earth / (R_earth + alt_km * 1e3)
    return 0.5 * Cd * density_dict[alt_km] * v2   # N/m^2

# Material properties
E_nitinol   = 35.0e9
nu_nitinol  = 0.3
rho_nitinol = 6450.0
E_alum      = 69.0e9
nu_alum     = 0.33
rho_alum    = 2700.0

# =====================================================================
# STUDY FACTORS
# =====================================================================
d_wire_list   = [1.5, 2, 2.5, 3]                               # mm
altitude_list = [200, 225, 250, 275, 300, 325, 350, 375, 400]  # km
alt_sequence  = sorted(altitude_list, reverse=True)            # 400 -> 200

n_runs = len(d_wire_list) * len(alt_sequence)
print('Study: {} runs ({} diameters x {} altitudes)'.format(
    n_runs, len(d_wire_list), len(alt_sequence)))

# =====================================================================
# GEOMETRY (N fixed -> computed once)
# =====================================================================
R_sail = math.sqrt((2.0 * A_sail) / (N * math.sin(2.0 * math.pi / N)))
a = R_hub * math.sin(math.pi / N)
b = R_hub * math.cos(math.pi / N)
cosN = math.cos(math.pi / N)
sinN = math.sin(math.pi / N)

hub_verts = []
for i in range(N):
    theta = math.pi / 2.0 + math.pi / N - i * (2.0 * math.pi / N)
    hub_verts.append((R_hub * math.cos(theta), R_hub * math.sin(theta)))

# Wire runs parallel to the x-axis in the -x direction from vertex 0
beta_rad   = math.radians(180.0)
wire_start = hub_verts[0]
L_wire     = math.sqrt(R_sail**2 - b**2) - a
wire_end   = (wire_start[0] - L_wire, wire_start[1])
wire_mid   = ((wire_start[0] + wire_end[0]) / 2.0,
              (wire_start[1] + wire_end[1]) / 2.0,
              0.0)
wx = wire_start[0]
wy = wire_start[1]
cos_b = math.cos(beta_rad)
sin_b = math.sin(beta_rad)
A_hub = 0.5 * N * R_hub**2 * math.sin(2.0 * math.pi / N)

# =====================================================================
# DRAG-AREA FUNCTION
# =====================================================================
def solve_alpha(q):
    """Half-angle alpha of a circular arc with arc/chord ratio q = alpha/sin(alpha)."""
    if q <= 1.0 + 1e-12:
        return 0.0
    lo, hi = 1e-9, math.pi - 1e-6
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mid / math.sin(mid) < q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def drag_area(r0, rho, z):
    """
    r0  : undeformed in-plane radius of each wire node from hub centre (m)
    rho : deformed in-plane radius (m)
    z   : out-of-plane displacement U3 (m)           (all ordered root -> tip)
    Flow is along Z.

    Straight-edge polygon:
      A_proj = hub polygon + N-fold wedge areas out to the deformed radii.

    Billow between wires (inextensible Kapton gore, flat width 2*r0*sin(pi/N)
    squeezed into chord 2*rho*sin(pi/N)):
      q = r0/rho = alpha/sin(alpha)  ->  arc half-angle alpha(s)
      sag h(s) = (chord/2) * tan(alpha/2)   (centreline of gore bulges in -Z)

    Rim-edge scallop (in-plane inward curvature of the free edge):
      The gore centreline has a conserved length. Its billow sag adds slope
      dh/ds, so its in-plane reach is shorter than the straight chord-midpoint
      would be:
        delta = cos(pi/N) * sum[ sqrt(dr0^2 - dz^2) - sqrt(dr0^2 - (dz - dh)^2) ]
      Each rim edge is a parabola through its two tips with mid-edge pulled
      inward by delta; sliver area removed = (2/3) * chord * delta per edge.

    Drag weighting (free-molecular, per projected area):
      w = cos^2(phi) * (1 - sin^2(alpha)/3)
      phi = atan(dz/drho) radial slope of wire;  circumferential billow tilt
      averaged over projected width gives (1 - sin^2(alpha)/3).
    """
    n = len(rho)
    k = 0.5 * N * math.sin(2.0 * math.pi / N)

    alpha = [solve_alpha(r0[i] / rho[i]) for i in range(n)]
    h = [rho[i] * sinN * math.tan(alpha[i] / 2.0) for i in range(n)]   # (chord/2)*tan(alpha/2)

    A_proj = A_hub
    A_drag = A_hub
    w_last = 1.0
    delta  = 0.0
    for i in range(n - 1):
        dA = k * (rho[i + 1]**2 - rho[i]**2)
        drho = rho[i + 1] - rho[i]
        dz   = z[i + 1] - z[i]
        phi  = math.atan2(abs(dz), abs(drho)) if abs(drho) > 1e-15 else 0.0
        q    = 0.5 * (r0[i] + r0[i + 1]) / (0.5 * (rho[i] + rho[i + 1]))
        al   = solve_alpha(q)
        w    = (math.cos(phi) ** 2) * (1.0 - math.sin(al) ** 2 / 3.0)
        A_proj += dA
        A_drag += dA * w
        w_last = w

        dr0 = r0[i + 1] - r0[i]
        dh  = h[i + 1] - h[i]
        base = max(dr0**2 - dz**2, 0.0)
        bill = max(dr0**2 - (dz - dh)**2, 0.0)
        delta += cosN * (math.sqrt(base) - math.sqrt(bill))

    chord = 2.0 * rho[-1] * sinN
    A_scallop = N * (2.0 / 3.0) * chord * delta
    A_proj -= A_scallop
    A_drag -= A_scallop * w_last
    return dict(A_proj=A_proj, A_drag=A_drag, delta=delta,
                h_tip=h[-1], alpha_tip=alpha[-1])

# =====================================================================
# MODEL-BUILDING HELPERS
# =====================================================================
def build_base(model, r_wire):
    """Parts, materials, sections, mesh, assembly (no steps/loads)."""
    # Hub
    s = model.ConstrainedSketch(name='__profile__',
                                sheetSize=max(1.0, 4.0 * R_hub))
    s.setPrimaryObject(option=STANDALONE)
    for i in range(N):
        s.Line(point1=hub_verts[i], point2=hub_verts[(i + 1) % N])
    model.Part(name='Hub', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    model.parts['Hub'].BaseSolidExtrude(sketch=s, depth=H_hub)
    s.unsetPrimaryObject()
    del model.sketches['__profile__']

    # Wire
    s2 = model.ConstrainedSketch(name='__profile__', sheetSize=10.0)
    s2.setPrimaryObject(option=STANDALONE)
    s2.Line(point1=wire_start, point2=wire_end)
    model.Part(name='SMAWire', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    model.parts['SMAWire'].BaseWire(sketch=s2)
    s2.unsetPrimaryObject()
    del model.sketches['__profile__']

    # Materials
    model.Material(name='Nitinol')
    model.materials['Nitinol'].Density(table=((rho_nitinol,),))
    model.materials['Nitinol'].Elastic(table=((E_nitinol, nu_nitinol),))
    model.Material(name='Aluminum')
    model.materials['Aluminum'].Density(table=((rho_alum,),))
    model.materials['Aluminum'].Elastic(table=((E_alum, nu_alum),))

    # Sections
    model.CircularProfile(name='WireProfile', r=r_wire)
    model.BeamSection(
        name='WireSection', integration=DURING_ANALYSIS,
        poissonRatio=0.0, profile='WireProfile', material='Nitinol',
        temperatureVar=LINEAR, beamSectionOffset=(0.0, 0.0),
        consistentMassMatrix=False)
    model.HomogeneousSolidSection(
        name='HubSection', material='Aluminum', thickness=None)

    # Section assignments
    hub = model.parts['Hub']
    hub_set = hub.Set(cells=hub.cells, name='HubSet')
    hub.SectionAssignment(
        region=hub_set, sectionName='HubSection',
        offset=0.0, offsetType=MIDDLE_SURFACE,
        offsetField='', thicknessAssignment=FROM_SECTION)

    wire_part = model.parts['SMAWire']
    wire_edge = wire_part.edges.findAt((wire_mid,))
    wire_set  = wire_part.Set(edges=wire_edge, name='WireSet')
    wire_part.SectionAssignment(
        region=wire_set, sectionName='WireSection',
        offset=0.0, offsetType=MIDDLE_SURFACE,
        offsetField='', thicknessAssignment=FROM_SECTION)
    wire_part.assignBeamSectionOrientation(
        region=wire_set, method=N1_COSINES, n1=(0.0, 0.0, 1.0))

    # Root vertex set (for the encastre BC)
    attach_pt = (wire_start[0], wire_start[1], 0.0)
    wire_part.Set(vertices=wire_part.vertices.getByBoundingSphere(
        center=attach_pt, radius=r_wire * 2), name='WireFixed')

    # Mesh
    hub.seedPart(size=mesh_hub, deviationFactor=0.1, minSizeFactor=0.1)
    hub.setMeshControls(regions=hub.cells, elemShape=TET, technique=FREE)
    hub.setElementType(
        regions=(hub.cells,),
        elemTypes=(mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD),
                   mesh.ElemType(elemCode=C3D6,  elemLibrary=STANDARD),
                   mesh.ElemType(elemCode=C3D4,  elemLibrary=STANDARD)))
    hub.generateMesh()

    wire_part.seedPart(size=mesh_wire, deviationFactor=0.1, minSizeFactor=0.1)
    wire_part.setElementType(
        regions=(wire_part.edges,),
        elemTypes=(mesh.ElemType(elemCode=B31H, elemLibrary=STANDARD),))
    wire_part.generateMesh()

    # Assembly
    asm = model.rootAssembly
    asm.DatumCsysByDefault(CARTESIAN)
    asm.Instance(name='Hub-1',     part=model.parts['Hub'],     dependent=ON)
    asm.Instance(name='SMAWire-1', part=model.parts['SMAWire'], dependent=ON)


def add_first_step(model, step_name, w_scale):
    """First step: BC, drag field and line load are defined here."""
    model.StaticStep(
        name=step_name, previous='Initial',
        description='Static drag load on wire', nlgeom=ON,
        maxNumInc=1000, initialInc=0.001, minInc=1e-8, maxInc=0.05)
    model.steps[step_name].Restart(frequency=1, numberIntervals=0, overlay=ON)

    asm = model.rootAssembly
    wire_inst = asm.instances['SMAWire-1']
    model.EncastreBC(name='WireFixed', createStepName=step_name,
                     region=wire_inst.sets['WireFixed'])

    arc_expr = '({:.8f} + X * {:.8f} + Y * {:.8f})'.format(
        -wx * cos_b - wy * sin_b, cos_b, sin_b)
    model.ExpressionField(
        name='DragField', localCsys=None,
        description='Arc length s along wire from hub attachment point',
        expression=arc_expr)
    asm.Set(edges=wire_inst.edges.getByBoundingSphere(
        center=wire_mid, radius=L_wire * 0.6), name='WireEdges')
    model.LineLoad(
        name='DragLoad', createStepName=step_name,
        region=asm.sets['WireEdges'],
        comp3=-w_scale, distributionType=FIELD, field='DragField')


def add_restart_step(model, prev_job, prev_step, step_name, w_scale):
    """
    Append a step to the SAME model that restarts from prev_job/prev_step
    (same pattern as starlib.create_restart_step). BC, field and line load
    carry over; only the load magnitude is changed in the new step.
    """
    model.setValues(restartJob=prev_job, restartStep=prev_step)
    model.StaticStep(
        name=step_name, previous=prev_step,
        description='Static drag load on wire', nlgeom=ON,
        maxNumInc=1000, initialInc=0.001, minInc=1e-8, maxInc=0.05)
    model.steps[step_name].Restart(frequency=1, numberIntervals=0, overlay=ON)
    model.loads['DragLoad'].setValuesInStep(stepName=step_name, comp3=-w_scale)


def make_job(model_name, job_name, description, job_type):
    if job_name in mdb.jobs.keys():
        del mdb.jobs[job_name]
    mdb.Job(
        name=job_name, model=model_name, description=description,
        type=job_type, atTime=None, waitMinutes=0, queue=None,
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,
        echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
        userSubroutine='', scratch='', resultsFormat=ODB,
        numCpus=1, numGPUs=0)


def run_job(job_name, odb_wait_timeout=600.0):
    lck = job_name + '.lck'
    if os.access(lck, os.F_OK):
        os.remove(lck)
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
    mdb.jobs[job_name].waitForCompletion()
    ok = (mdb.jobs[job_name].status == COMPLETED)
    t0 = time.time()
    while os.path.exists(lck) and time.time() - t0 < odb_wait_timeout:
        time.sleep(1.0)
    return ok


def extract_results(job_name, step_name):
    """Read results from the new step only (restart ODBs hold only new steps)."""
    odb   = session.openOdb(name=job_name + '.odb')
    frame = odb.steps[step_name].frames[-1]
    u_field = frame.fieldOutputs['U']
    s_field = frame.fieldOutputs['S']
    e_field = frame.fieldOutputs['E']
    odb_wire = odb.rootAssembly.instances['SMAWIRE-1']

    u_wire   = u_field.getSubset(region=odb_wire).values
    max_disp = max(v.magnitude for v in u_wire)

    coords = {}
    for nd in odb_wire.nodes:
        coords[nd.label] = nd.coordinates

    # Tip node = wire node with the smallest x (wire runs in -x)
    tip_label = min(coords.keys(), key=lambda lab: coords[lab][0])
    tip_u = None
    for v in u_wire:
        if v.nodeLabel == tip_label:
            tip_u = v.data
            break
    U1, U2, U3 = tip_u[0], tip_u[1], tip_u[2]

    max_stress = max(abs(v.data[0]) for v in s_field.values)
    max_strain = max(abs(v.data[0]) for v in e_field.values)

    pts = []
    for v in u_wire:
        c = coords[v.nodeLabel]
        pts.append((wx - c[0],
                    math.hypot(c[0], c[1]),
                    math.hypot(c[0] + v.data[0], c[1] + v.data[1]),
                    v.data[2]))
    pts.sort(key=lambda t: t[0])
    odb.close()

    area = drag_area([t[1] for t in pts],
                     [t[2] for t in pts],
                     [t[3] for t in pts])
    out = dict(max_disp=max_disp, U1=U1, U2=U2, U3=U3,
               max_stress=max_stress, max_strain=max_strain)
    out.update(area)
    return out


def sail_outline(U1, U2, delta, npts=15):
    """
    Closed top-down outline: N rim edges, each a parabola through its two
    wire tips with the mid-edge pulled inward by delta (scallop).
    """
    xt = wire_end[0] + U1
    yt = wire_end[1] + U2
    verts = []
    for k in range(N):
        ang = -k * 2.0 * math.pi / N
        verts.append((xt * math.cos(ang) - yt * math.sin(ang),
                      xt * math.sin(ang) + yt * math.cos(ang)))
    xs, ys = [], []
    for k in range(N):
        v0 = verts[k]
        v1 = verts[(k + 1) % N]
        mx, my = 0.5 * (v0[0] + v1[0]), 0.5 * (v0[1] + v1[1])
        mr = math.hypot(mx, my)
        nx, ny = mx / mr, my / mr                     # outward unit normal
        px, py = mx - delta * nx, my - delta * ny     # pulled-in mid-edge
        cx, cy = 2.0 * px - mx, 2.0 * py - my         # Bezier control point
        for j in range(npts):
            t = j / float(npts)
            xs.append((1 - t)**2 * v0[0] + 2 * (1 - t) * t * cx + t**2 * v1[0])
            ys.append((1 - t)**2 * v0[1] + 2 * (1 - t) * t * cy + t**2 * v1[1])
    xs.append(xs[0])
    ys.append(ys[0])
    return xs, ys


def plot_outlines(d_mm, records):
    """One top-down figure per wire diameter; thin lines, true scale."""
    alts = [r['altitude'] for r in records]
    norm = Normalize(vmin=min(alts), vmax=max(alts))
    cmap = cm.viridis_r

    fig, ax = plt.subplots(figsize=(7, 7))

    u_x, u_y = sail_outline(0.0, 0.0, 0.0)
    ax.plot(u_x, u_y, 'k--', lw=0.4, label='Undeformed')

    hx = [v[0] for v in hub_verts] + [hub_verts[0][0]]
    hy = [v[1] for v in hub_verts] + [hub_verts[0][1]]
    ax.plot(hx, hy, 'k-', lw=0.5)

    for r in records:
        xs, ys = sail_outline(r['U1'], r['U2'], r['delta'])
        ax.plot(xs, ys, '-', lw=0.4, color=cmap(norm(r['altitude'])))

    sm = cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    cb = fig.colorbar(sm, ax=ax, shrink=0.8)
    cb.set_label('Altitude (km)')

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_title('Projected sail profile, top-down view (true scale)\n'
                 'd_wire = {} mm, N = {}'.format(d_mm, N))
    ax.grid(True, alpha=0.2, lw=0.3)
    ax.legend(loc='upper right', fontsize=8)
    fig.tight_layout()
    fname = 'sail_outline_d{}mm.png'.format(str(d_mm).replace('.', 'p'))
    fig.savefig(fname, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('Saved: ' + fname)

# =====================================================================
# RESULTS CSV (one row per run, inputs and outputs side by side)
# =====================================================================
results_path = 'factorial_results_{}.csv'.format(STUDY_NO)

csv_header = [
    'run_no', 'd_wire (mm)', 'r_wire (m)', 'altitude (km)', 'N',
    'A_sail (m^2)', 'rho_atm (kg/m^3)', 'Cd', 'drag_pressure (N/m^2)',
    'A_used_for_load (m^2)', 'F_drag (N)', 'w_scale (N/m^2)',
    'R_hub (m)', 'H_hub (m)', 'mesh_hub (m)', 'mesh_wire (m)',
    'E_nitinol (GPa)', 'nu_nitinol', 'rho_nitinol (kg/m^3)',
    'R_sail (m)', 'L_wire (m)', 'beta (deg)',
    'wire_mass (kg)', 'max_deformation (m)',
    'U1_tip (m)', 'U2_tip (m)', 'U3_tip (m)',
    'max_stress_S11 (Pa)', 'max_strain_E11',
    'tip_radius (m)', 'edge_scallop_depth (m)', 'billow_sag_tip (m)',
    'A_projected (m^2)', 'A_drag (m^2)',
    'A_projected/A_sail', 'A_drag/A_sail',
    'job_type', 'elapsed_time (s)']

with open(results_path, 'w', newline='') as f:
    csv.writer(f).writerow(csv_header)

# =====================================================================
# STUDY LOOP: ONE MODEL PER WIRE DIAMETER, one job per altitude
# =====================================================================
run_no = 0

for d_mm in d_wire_list:
    r_wire = d_mm / 2000.0
    d_tag  = str(d_mm).replace('.', 'p')

    Mdb()
    model = mdb.models['Model-1']
    build_base(model, r_wire)

    A_prev   = A_sail            # flat sail for the first (400 km) run
    prev_job = None
    prev_step = None
    records  = []

    for altitude in alt_sequence:
        run_no += 1
        _run_start = time.perf_counter()
        print('\n--- Run {:03d}/{:03d} d={} mm alt={} km ---'.format(
            run_no, n_runs, d_mm, altitude))

        p_drag  = drag_pressure(altitude)
        A_used  = A_prev                 # lagged drag area (previous altitude)
        F_drag  = p_drag * A_used
        w_scale = 2.0 * F_drag / (N * L_wire**2)

        step_name = 'Step-{}'.format(altitude)
        job_name  = 'D{}_A{}'.format(d_tag, altitude)

        if prev_job is None:
            add_first_step(model, step_name, w_scale)
            job_type = ANALYSIS
            type_str = 'analysis'
        else:
            add_restart_step(model, prev_job, prev_step, step_name, w_scale)
            job_type = RESTART
            type_str = 'restart'

        make_job(model.name, job_name,
                 '{} d={} alt={}'.format(type_str, d_mm, altitude), job_type)
        if not run_job(job_name):
            raise RuntimeError('Job {} ({}) did not complete. Check {}.msg / '
                               '{}.dat'.format(job_name, type_str, job_name, job_name))
        print('  Job {} ({}) completed.'.format(job_name, type_str))

        res = extract_results(job_name, step_name)

        prev_job, prev_step = job_name, step_name
        A_prev = res['A_drag']           # feeds the next (lower) altitude

        _run_elapsed = time.perf_counter() - _run_start
        wire_mass = N * np.pi * r_wire**2 * L_wire * rho_nitinol
        tip_R = math.hypot(wire_end[0] + res['U1'], wire_end[1] + res['U2'])

        with open(results_path, 'a', newline='') as f:
            csv.writer(f).writerow([
                run_no, d_mm, r_wire, altitude, N,
                A_sail, density_dict[altitude], Cd, p_drag,
                A_used, F_drag, w_scale,
                R_hub, H_hub, mesh_hub, mesh_wire,
                E_nitinol / 1e9, nu_nitinol, rho_nitinol,
                R_sail, L_wire, math.degrees(beta_rad),
                wire_mass, res['max_disp'],
                res['U1'], res['U2'], res['U3'],
                res['max_stress'], res['max_strain'],
                tip_R, res['delta'], res['h_tip'],
                res['A_proj'], res['A_drag'],
                res['A_proj'] / A_sail, res['A_drag'] / A_sail,
                type_str, _run_elapsed])

        records.append(dict(altitude=altitude, U1=res['U1'], U2=res['U2'],
                            U3=res['U3'], delta=res['delta']))

        print('  F={:.5e} N  max_disp={:.4e} m  tip U=({:.3e}, {:.3e}, {:.3e}) m'.format(
            F_drag, res['max_disp'], res['U1'], res['U2'], res['U3']))
        print('  A_proj={:.5f}  A_drag={:.5f} m^2  scallop={:.3e} m  t={:.1f}s'.format(
            res['A_proj'], res['A_drag'], res['delta'], _run_elapsed))

    plot_outlines(d_mm, records)

_total_elapsed = time.perf_counter() - _total_start
print('\nAll {} runs complete. Total time: {:.1f} s'.format(run_no, _total_elapsed))
print('Results saved to: ' + results_path)
