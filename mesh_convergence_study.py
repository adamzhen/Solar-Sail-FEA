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

_total_start = time.perf_counter()

# =====================================================================
# MESH CONVERGENCE STUDY -- EDIT THESE
# =====================================================================
ALTITUDE   = 200          # km
D_WIRE_MM  = 1.5          # wire diameter, mm

# Area used to set the load: F = p(ALTITUDE) * A_LOAD.
# 4.2956 m^2 is the lagged area used for the 1.5 mm / 200 km run of the
# restart study (A_drag from 225 km). Set A_LOAD = A_sail for a flat-sail load,
# or use the area your own study row shows in "A_used_for_load (m^2)".
A_LOAD     = 4.2956

# Number of beam elements along the wire for each mesh. Keep the factor of 2
# between consecutive meshes so Richardson extrapolation / GCI are valid.
N_ELEM_LIST = [3, 6, 12, 24, 48, 96, 192]

CONV_TOL   = 0.01         # a mesh is "converged" if the change vs the next-finer mesh is < 1%
ELEM_CODE  = B31H         # wire element type (e.g. B31H, B31, B32)

# =====================================================================
# FIXED PARAMETERS (same as the main study)
# =====================================================================
N         = 8
A_sail    = 9.0
R_hub     = 0.03
H_hub     = 0.09
mesh_hub  = 0.02

Cd        = 2.2
mu_earth  = 3.986004418e14
R_earth   = 6371.0e3

density_dict = {
    100: 4.928e-07, 125: 1.139e-08, 150: 1.902e-09, 175: 6.466e-10,
    200: 2.840e-10, 225: 1.415e-10, 250: 7.570e-11, 275: 3.897e-11,
    300: 1.914e-11, 325: 1.165e-11, 350: 7.007e-12, 375: 4.814e-12,
    400: 2.800e-12}

E_nitinol   = 35.0e9
nu_nitinol  = 0.3
rho_nitinol = 6450.0
E_alum      = 69.0e9
nu_alum     = 0.33
rho_alum    = 2700.0

def drag_pressure(alt_km):
    v2 = mu_earth / (R_earth + alt_km * 1e3)
    return 0.5 * Cd * density_dict[alt_km] * v2

# =====================================================================
# GEOMETRY
# =====================================================================
r_wire = D_WIRE_MM / 2000.0
R_sail = math.sqrt((2.0 * A_sail) / (N * math.sin(2.0 * math.pi / N)))
a = R_hub * math.sin(math.pi / N)
b = R_hub * math.cos(math.pi / N)
cosN = math.cos(math.pi / N)
sinN = math.sin(math.pi / N)

hub_verts = []
for i in range(N):
    theta = math.pi / 2.0 + math.pi / N - i * (2.0 * math.pi / N)
    hub_verts.append((R_hub * math.cos(theta), R_hub * math.sin(theta)))

beta_rad   = math.radians(180.0)
wire_start = hub_verts[0]
L_wire     = math.sqrt(R_sail**2 - b**2) - a
wire_end   = (wire_start[0] - L_wire, wire_start[1])
wire_mid   = ((wire_start[0] + wire_end[0]) / 2.0,
              (wire_start[1] + wire_end[1]) / 2.0, 0.0)
wx, wy = wire_start
cos_b = math.cos(beta_rad)
sin_b = math.sin(beta_rad)
A_hub = 0.5 * N * R_hub**2 * math.sin(2.0 * math.pi / N)

p_drag  = drag_pressure(ALTITUDE)
F_drag  = p_drag * A_LOAD
w_scale = 2.0 * F_drag / (N * L_wire**2)

print('Mesh convergence: d={} mm, alt={} km'.format(D_WIRE_MM, ALTITUDE))
print('p={:.5e} N/m^2, A_LOAD={} m^2, F={:.5e} N, w_scale={:.5e} N/m^2'.format(
    p_drag, A_LOAD, F_drag, w_scale))

# =====================================================================
# DRAG-AREA FUNCTION (same as the main study)
# =====================================================================
def solve_alpha(q):
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
    rho = [max(r, 1e-6) for r in rho]
    n = len(rho)
    k = 0.5 * N * math.sin(2.0 * math.pi / N)
    alpha = [solve_alpha(min(r0[i] / rho[i], 50.0)) for i in range(n)]
    h = [rho[i] * sinN * math.tan(alpha[i] / 2.0) for i in range(n)]
    A_proj = A_hub
    A_drag = A_hub
    w_last = 1.0
    delta  = 0.0
    for i in range(n - 1):
        dA = k * (rho[i + 1]**2 - rho[i]**2)
        drho = rho[i + 1] - rho[i]
        dz   = z[i + 1] - z[i]
        phi  = math.atan2(abs(dz), abs(drho)) if abs(drho) > 1e-15 else 0.0
        q    = min(0.5 * (r0[i] + r0[i + 1]) / (0.5 * (rho[i] + rho[i + 1])), 50.0)
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
    return dict(A_proj=A_proj, A_drag=A_drag, delta=delta)

# =====================================================================
# MODEL BUILDER (one wire mesh density per call)
# =====================================================================
def build_model(model, n_elem):
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

    # Materials and sections
    model.Material(name='Nitinol')
    model.materials['Nitinol'].Density(table=((rho_nitinol,),))
    model.materials['Nitinol'].Elastic(table=((E_nitinol, nu_nitinol),))
    model.Material(name='Aluminum')
    model.materials['Aluminum'].Density(table=((rho_alum,),))
    model.materials['Aluminum'].Elastic(table=((E_alum, nu_alum),))

    model.CircularProfile(name='WireProfile', r=r_wire)
    model.BeamSection(
        name='WireSection', integration=DURING_ANALYSIS,
        poissonRatio=0.0, profile='WireProfile', material='Nitinol',
        temperatureVar=LINEAR, beamSectionOffset=(0.0, 0.0),
        consistentMassMatrix=False)
    model.HomogeneousSolidSection(
        name='HubSection', material='Aluminum', thickness=None)

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
    wire_part.Set(vertices=wire_part.vertices.getByBoundingSphere(
        center=(wire_start[0], wire_start[1], 0.0), radius=r_wire * 2),
        name='WireFixed')

    # Mesh: hub fixed; wire seeded by NUMBER of elements
    hub.seedPart(size=mesh_hub, deviationFactor=0.1, minSizeFactor=0.1)
    hub.setMeshControls(regions=hub.cells, elemShape=TET, technique=FREE)
    hub.setElementType(
        regions=(hub.cells,),
        elemTypes=(mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD),
                   mesh.ElemType(elemCode=C3D6,  elemLibrary=STANDARD),
                   mesh.ElemType(elemCode=C3D4,  elemLibrary=STANDARD)))
    hub.generateMesh()

    wire_part.seedEdgeByNumber(edges=wire_part.edges, number=n_elem,
                               constraint=FIXED)
    wire_part.setElementType(
        regions=(wire_part.edges,),
        elemTypes=(mesh.ElemType(elemCode=ELEM_CODE, elemLibrary=STANDARD),))
    wire_part.generateMesh()

    # Assembly
    asm = model.rootAssembly
    asm.DatumCsysByDefault(CARTESIAN)
    asm.Instance(name='Hub-1',     part=model.parts['Hub'],     dependent=ON)
    asm.Instance(name='SMAWire-1', part=model.parts['SMAWire'], dependent=ON)

    # Step, BC, load
    model.StaticStep(
        name='DragStep', previous='Initial',
        description='Static drag load on wire', nlgeom=ON,
        maxNumInc=1000, initialInc=0.001, minInc=1e-8, maxInc=0.05)
    wire_inst = asm.instances['SMAWire-1']
    model.EncastreBC(name='WireFixed', createStepName='DragStep',
                     region=wire_inst.sets['WireFixed'])
    arc_expr = '({:.8f} + X * {:.8f} + Y * {:.8f})'.format(
        -wx * cos_b - wy * sin_b, cos_b, sin_b)
    model.ExpressionField(name='DragField', localCsys=None,
        description='Arc length s along wire from hub attachment point',
        expression=arc_expr)
    asm.Set(edges=wire_inst.edges.getByBoundingSphere(
        center=wire_mid, radius=L_wire * 0.6), name='WireEdges')
    model.LineLoad(name='DragLoad', createStepName='DragStep',
                   region=asm.sets['WireEdges'], comp3=-w_scale,
                   distributionType=FIELD, field='DragField')

# =====================================================================
# RESULT EXTRACTION
# =====================================================================
def extract_results(job_name):
    odb   = session.openOdb(name=job_name + '.odb')
    frame = odb.steps['DragStep'].frames[-1]
    u_field = frame.fieldOutputs['U']
    s_field = frame.fieldOutputs['S']
    e_field = frame.fieldOutputs['E']
    odb_wire = odb.rootAssembly.instances['SMAWIRE-1']

    n_elems_odb = len(odb_wire.elements)
    n_nodes_odb = len(odb_wire.nodes)

    u_wire   = u_field.getSubset(region=odb_wire).values
    max_disp = max(v.magnitude for v in u_wire)

    coords = {}
    for nd in odb_wire.nodes:
        coords[nd.label] = nd.coordinates
    tip_label = min(coords.keys(), key=lambda lab: coords[lab][0])
    tip_u = [v.data for v in u_wire if v.nodeLabel == tip_label][0]

    max_stress = max(abs(v.data[0]) for v in s_field.values)
    max_strain = max(abs(v.data[0]) for v in e_field.values)

    pts = []
    for v in u_wire:
        c = coords[v.nodeLabel]
        pts.append((wx - c[0],
                    math.hypot(c[0], c[1]),
                    math.hypot(c[0] + v.data[0], c[1] + v.data[1]),
                    c[0] + v.data[0],
                    c[2] + v.data[2]))
    pts.sort(key=lambda t: t[0])
    odb.close()

    area = drag_area([t[1] for t in pts], [t[2] for t in pts], [t[4] for t in pts])
    out = dict(n_elems=n_elems_odb, n_nodes=n_nodes_odb,
               max_disp=max_disp, U1=tip_u[0], U2=tip_u[1], U3=tip_u[2],
               max_stress=max_stress, max_strain=max_strain,
               A_proj=area['A_proj'], A_drag=area['A_drag'], delta=area['delta'],
               profile_x=[t[3] for t in pts], profile_z=[t[4] for t in pts])
    return out

# =====================================================================
# RUN ALL MESHES
# =====================================================================
results = []
Mdb()
for n_elem in N_ELEM_LIST:
    t0 = time.perf_counter()
    model_name = 'Mesh_{}'.format(n_elem)
    job_name   = 'MeshConv_d{}_A{}_n{}'.format(
        str(D_WIRE_MM).replace('.', 'p'), ALTITUDE, n_elem)
    print('\n--- {} elements (h = {:.4f} m) ---'.format(n_elem, L_wire / n_elem))

    model = mdb.Model(name=model_name)
    build_model(model, n_elem)

    mdb.Job(name=job_name, model=model_name,
            description='Mesh convergence n={}'.format(n_elem),
            type=ANALYSIS, atTime=None, waitMinutes=0, queue=None,
            memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,
            echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
            userSubroutine='', scratch='', resultsFormat=ODB,
            numCpus=1, numGPUs=0)
    lck = job_name + '.lck'
    if os.access(lck, os.F_OK):
        os.remove(lck)
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
    mdb.jobs[job_name].waitForCompletion()
    if mdb.jobs[job_name].status != COMPLETED:
        print('  Job {} did not complete; stopping refinement here.'.format(job_name))
        break
    t_wait = time.time()
    while os.path.exists(lck) and time.time() - t_wait < 300:
        time.sleep(1.0)

    res = extract_results(job_name)
    res['n_elem_requested'] = n_elem
    res['h'] = L_wire / n_elem
    res['wall_time'] = time.perf_counter() - t0
    results.append(res)
    print('  tip U1={:.5e}  U3={:.5e}  max|U|={:.5e}  S11max={:.4e}  A_drag={:.5f}  t={:.1f}s'.format(
        res['U1'], res['U3'], res['max_disp'], res['max_stress'],
        res['A_drag'], res['wall_time']))

if len(results) < 2:
    raise RuntimeError('Need at least two completed meshes for a convergence study.')

# =====================================================================
# CONVERGENCE METRICS
# =====================================================================
metrics = [('U1', 'U1_tip (m)'), ('U3', 'U3_tip (m)'),
           ('max_disp', 'max_deformation (m)'),
           ('max_stress', 'max_stress_S11 (Pa)'),
           ('A_drag', 'A_drag (m^2)')]

def rel_change(f_coarse, f_fine):
    return abs(f_fine - f_coarse) / abs(f_fine) if f_fine != 0 else float('nan')

def richardson(f1, f2, f3, r=2.0):
    """f1 finest, f2 medium, f3 coarse; constant refinement ratio r."""
    try:
        e32 = f3 - f2
        e21 = f2 - f1
        if e21 == 0.0 or e32 / e21 <= 0.0:
            return float('nan'), float('nan'), float('nan')
        p = math.log(e32 / e21) / math.log(r)
        f_ext = f1 + (f1 - f2) / (r**p - 1.0)
        gci = 1.25 * abs((f1 - f2) / f1) / (r**p - 1.0)
        return p, f_ext, gci
    except Exception:
        return float('nan'), float('nan'), float('nan')

finest = results[-1]
summary = []
for key, label in metrics:
    vals = [r[key] for r in results]
    p, f_ext, gci = (float('nan'),) * 3
    if len(vals) >= 3:
        p, f_ext, gci = richardson(vals[-1], vals[-2], vals[-3])
    summary.append((key, label, p, f_ext, gci))

# Smallest mesh whose change vs the next-finer mesh is below CONV_TOL for ALL key metrics
converged_n = None
for i in range(len(results) - 1):
    ok = True
    for key, label in metrics:
        if rel_change(results[i][key], results[i + 1][key]) >= CONV_TOL:
            ok = False
            break
    if ok:
        converged_n = results[i]['n_elem_requested']
        break

# =====================================================================
# WRITE CSV
# =====================================================================
tag = 'd{}mm_{}km'.format(str(D_WIRE_MM).replace('.', 'p'), ALTITUDE)
csv_path = 'mesh_convergence_{}.csv'.format(tag)
with open(csv_path, 'w', newline='') as f:
    w = csv.writer(f)
    header = ['n_elem_requested', 'n_elems_odb', 'n_nodes', 'elem_size_h (m)',
              'U1_tip (m)', 'U2_tip (m)', 'U3_tip (m)', 'max_deformation (m)',
              'max_stress_S11 (Pa)', 'max_strain_E11',
              'A_projected (m^2)', 'A_drag (m^2)', 'edge_scallop_depth (m)',
              'wall_time (s)']
    for key, label in metrics:
        header.append('rel_change_' + key + ' (vs next finer)')
    for key, label in metrics:
        header.append('rel_err_' + key + ' (vs finest)')
    w.writerow(header)
    for i, r in enumerate(results):
        row = [r['n_elem_requested'], r['n_elems'], r['n_nodes'], r['h'],
               r['U1'], r['U2'], r['U3'], r['max_disp'],
               r['max_stress'], r['max_strain'],
               r['A_proj'], r['A_drag'], r['delta'], r['wall_time']]
        for key, label in metrics:
            row.append(rel_change(r[key], results[i + 1][key])
                       if i < len(results) - 1 else '')
        for key, label in metrics:
            row.append(rel_change(r[key], finest[key])
                       if i < len(results) - 1 else '')
        w.writerow(row)
    w.writerow([])
    w.writerow(['Richardson extrapolation / GCI (three finest meshes, ratio 2)'])
    w.writerow(['quantity', 'observed_order_p', 'extrapolated_value', 'GCI_fine'])
    for key, label, p, f_ext, gci in summary:
        w.writerow([label, p, f_ext, gci])
    w.writerow([])
    w.writerow(['converged_at_n_elem (all metrics < {:.1%} change)'.format(CONV_TOL),
                converged_n if converged_n is not None else 'not reached'])

# =====================================================================
# PLOTS
# =====================================================================
ns  = [r['n_elem_requested'] for r in results]
fig, axs = plt.subplots(2, 2, figsize=(12, 9))

ax = axs[0, 0]
ax.semilogx(ns, [abs(r['U3']) for r in results], 'o-', label='|U3| tip')
ax.semilogx(ns, [abs(r['U1']) for r in results], 's-', label='|U1| tip')
ax.semilogx(ns, [r['max_disp'] for r in results], '^-', label='max |U|')
ax.set_xlabel('Elements along wire'); ax.set_ylabel('Displacement (m)')
ax.set_title('Tip displacement vs mesh'); ax.grid(True, which='both', alpha=0.3)
ax.legend(fontsize=8)

ax = axs[0, 1]
ax.semilogx(ns, [r['A_drag'] for r in results], 'o-', color='tab:red', label='A_drag')
ax.semilogx(ns, [r['A_proj'] for r in results], 's--', color='tab:orange', label='A_projected')
ax.set_xlabel('Elements along wire'); ax.set_ylabel('Area (m$^2$)')
ax.set_title('Drag area vs mesh'); ax.grid(True, which='both', alpha=0.3)
ax.legend(fontsize=8)

ax = axs[1, 0]
for key, label in metrics:
    errs = [rel_change(r[key], finest[key]) for r in results[:-1]]
    ax.loglog(ns[:-1], [max(e, 1e-12) for e in errs], 'o-', label=key)
ax.axhline(CONV_TOL, color='k', ls='--', lw=0.8, label='tolerance')
ax.set_xlabel('Elements along wire'); ax.set_ylabel('Relative error vs finest mesh')
ax.set_title('Error vs finest mesh'); ax.grid(True, which='both', alpha=0.3)
ax.legend(fontsize=8)

ax = axs[1, 1]
ax.loglog(ns, [r['wall_time'] for r in results], 'o-', color='tab:green')
ax.set_xlabel('Elements along wire'); ax.set_ylabel('Wall time per run (s)')
ax.set_title('Cost'); ax.grid(True, which='both', alpha=0.3)

fig.suptitle('Mesh convergence: d = {} mm, {} km, F = {:.4f} N'.format(
    D_WIRE_MM, ALTITUDE, F_drag), fontsize=13)
fig.tight_layout()
fig.savefig('mesh_convergence_{}.png'.format(tag), dpi=170)
plt.close(fig)

# Wire profiles for each mesh (XZ plane)
fig, ax = plt.subplots(figsize=(9, 6))
norm = Normalize(vmin=0, vmax=len(results) - 1)
cmap = cm.viridis
for i, r in enumerate(results):
    ax.plot(r['profile_x'], r['profile_z'], '-', lw=0.9, color=cmap(norm(i)),
            label='{} elems'.format(r['n_elem_requested']))
ax.plot([wire_start[0], wire_end[0]], [0, 0], 'k--', lw=0.6, label='Undeformed')
ax.set_aspect('equal', 'datalim')
ax.set_xlabel('X (m)'); ax.set_ylabel('Z (m)')
ax.set_title('Deformed wire profile by mesh density (XZ plane)')
ax.grid(True, alpha=0.3, lw=0.4); ax.legend(fontsize=8, loc='lower left')
fig.tight_layout()
fig.savefig('mesh_convergence_profiles_{}.png'.format(tag), dpi=200)
plt.close(fig)

# =====================================================================
# CONSOLE SUMMARY
# =====================================================================
print('\n=== Mesh convergence summary ({}) ==='.format(tag))
for key, label, p, f_ext, gci in summary:
    print('{:<24s} order p={:.3f}  extrapolated={:.6e}  GCI_fine={:.3e}'.format(
        label, p, f_ext, gci))
if converged_n is not None:
    print('Converged (<{:.1%} change on all metrics) at {} elements'.format(
        CONV_TOL, converged_n))
else:
    print('Tolerance NOT reached within the meshes run; refine further.')
print('Saved: ' + csv_path)
print('Total time: {:.1f} s'.format(time.perf_counter() - _total_start))
