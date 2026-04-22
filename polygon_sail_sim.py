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

import math
import time

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

if 'Viewport: 1' in session.viewports.keys():
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendFont='-*-verdana-medium-r-normal-*-*-720-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        titleFont='-*-verdana-medium-r-normal-*-*-480-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        stateFont='-*-verdana-medium-r-normal-*-*-480-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        triadFont='-*-verdana-bold-r-normal-*-*-480-*-*-p-*-*-*')

_start_time = time.perf_counter()

Mdb()
model = mdb.models['Model-1']

run_no = 0.1

# =====================================================================
# PARAMETERS 
# =====================================================================

# Design parameters
N         = 8        # number of polygon sides
A_sail    = 9.0      # sail area, m^2
R_hub     = 0.03     # hub circumradius (centre to hub vertex), m
H_hub     = 0.09     # hub extrusion height, m
d_wire    = 1.5      # SMA wire diameter, mm
r_wire    = d_wire / 2000   # SMA wire radius, m
mesh_hub  = 0.02     # hub mesh seed size, m
mesh_wire = 0.1      # wire mesh seed size, m

# Scenario parameters
altitude = 300       # altitude, km
drag_pressure_dict = {
    300: 0.0012580,
    325: 0.0007627,
    350: 0.0004571,
    375: 0.0003129,
    400: 0.0001813}
F_drag = drag_pressure_dict[altitude] * A_sail   # N

# Material properties
E_nitinol   = 40.0e9
E_alum      = 69.0e9
nu_nitinol  = 0.3
nu_alum     = 0.33
rho_nitinol = 6450.0
rho_alum    = 2700.0

# =====================================================================
# DERIVED GEOMETRY
# All quantities below are expressed in terms of N, R_hub, A_sail
# so that changing N at the top is the only edit required.
# =====================================================================

# --- Sail outer circumradius from area ---
# A = (N/2) * R^2 * sin(2*pi/N)  =>  R = sqrt(2*A / (N*sin(2*pi/N)))
R_sail = math.sqrt((2.0 * A_sail) / (N * math.sin(2.0 * math.pi / N)))

# --- Hub vertex half-edge components ---
# For a regular N-gon hub with circumradius R_hub, the first vertex
# (upper-left, where the wire attaches) sits at angle pi/2 + pi/N.
# a and b are its x- and y-magnitudes respectively:
#   vertex_0 = (-a, b)
# These are still used in the L_wire formula below.
a = R_hub * math.sin(math.pi / N)   # |x| of wire-attachment vertex
b = R_hub * math.cos(math.pi / N)   # |y| of wire-attachment vertex

# --- All N hub vertices (clockwise from upper-left) ---
# theta_i = pi/2 + pi/N - i*(2*pi/N)
# At i=0: cos(theta_0)=-sin(pi/N)=-a/R_hub, sin(theta_0)=cos(pi/N)=b/R_hub => (-a, b) ✓
hub_verts = []
for i in range(N):
    theta = math.pi / 2.0 + math.pi / N - i * (2.0 * math.pi / N)
    hub_verts.append((R_hub * math.cos(theta), R_hub * math.sin(theta)))

# --- Wire geometry ---
# Wire exits hub at vertex_0 = (-a, b) at angle beta from the horizontal.
# beta = 360/N degrees (equal angular spacing of N spokes).
# L_wire: from hub vertex to outer polygon vertex, via law of cosines
# simplified for the specific geometry (see derivation notes).
beta_rad   = math.radians(360.0 / N)
wire_start = hub_verts[0]                             # (-a, b, 0) -- attachment point
L_wire     = math.sqrt(R_sail**2 - b**2) - a         # wire length, m
wire_end   = (wire_start[0] + L_wire * math.cos(beta_rad),
              wire_start[1] + L_wire * math.sin(beta_rad))
wire_mid   = ((wire_start[0] + wire_end[0]) / 2.0,
              (wire_start[1] + wire_end[1]) / 2.0,
              0.0)

# --- Distributed load scale factor ---
# w(s) = w_scale * s,  where s is arc length from wire_start
# Integrates to F_drag/N over [0, L_wire] (one spoke's share of total drag)
w_scale = 2.0 * F_drag / (N * L_wire**2)

print('N={}, R_sail={:.4f} m, a={:.5f} m, b={:.5f} m'.format(N, R_sail, a, b))
print('L_wire={:.4f} m, F_drag={:.6f} N, w_scale={:.4e} N/m^2'.format(
    L_wire, F_drag, w_scale))

# =====================================================================
# PART 1: HUB  -- general N-gon, works for any N >= 3
# =====================================================================

s = model.ConstrainedSketch(name='__profile__',
                            sheetSize=max(1.0, 4.0 * R_hub))
s.setPrimaryObject(option=STANDALONE)

# Draw the N sides of the regular polygon.
# hub_verts[(i+1) % N] wraps the last vertex back to vertex 0.
for i in range(N):
    s.Line(point1=hub_verts[i], point2=hub_verts[(i + 1) % N])

p = model.Part(name='Hub', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = model.parts['Hub']
p.BaseSolidExtrude(sketch=s, depth=H_hub)
s.unsetPrimaryObject()
del model.sketches['__profile__']

# =====================================================================
# PART 2: SMA WIRE (3D beam)
# =====================================================================

s2 = model.ConstrainedSketch(name='__profile__', sheetSize=10.0)
s2.setPrimaryObject(option=STANDALONE)
s2.Line(point1=wire_start, point2=wire_end)

wire_part = model.Part(name='SMAWire', dimensionality=THREE_D, type=DEFORMABLE_BODY)
wire_part = model.parts['SMAWire']
wire_part.BaseWire(sketch=s2)
s2.unsetPrimaryObject()
del model.sketches['__profile__']

# =====================================================================
# MATERIALS
# =====================================================================

model.Material(name='Nitinol')
model.materials['Nitinol'].Density(table=((rho_nitinol,),))
model.materials['Nitinol'].Elastic(table=((E_nitinol, nu_nitinol),))

model.Material(name='Aluminum')
model.materials['Aluminum'].Density(table=((rho_alum,),))
model.materials['Aluminum'].Elastic(table=((E_alum, nu_alum),))

# =====================================================================
# SECTIONS
# =====================================================================

model.CircularProfile(name='WireProfile', r=r_wire)
model.BeamSection(
    name                 = 'WireSection',
    integration          = DURING_ANALYSIS,
    poissonRatio         = 0.0,
    profile              = 'WireProfile',
    material             = 'Nitinol',
    temperatureVar       = LINEAR,
    beamSectionOffset    = (0.0, 0.0),
    consistentMassMatrix = False)

model.HomogeneousSolidSection(
    name      = 'HubSection',
    material  = 'Aluminum',
    thickness = None)

# =====================================================================
# SECTION ASSIGNMENTS
# =====================================================================

hub     = model.parts['Hub']
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

# =====================================================================
# BEAM ORIENTATION
# n1 = (0,0,1): cross-section local 1-axis points along global Z
# =====================================================================

wire_part.assignBeamSectionOrientation(
    region=wire_set,
    method=N1_COSINES,
    n1=(0.0, 0.0, 1.0))

# =====================================================================
# MESHING
# Hub: free tet (visualization only -- no BCs or loads on hub).
# Wire: B31H hybrid beam elements (required for slender geometry).
# =====================================================================

hub = model.parts['Hub']
hub.seedPart(size=mesh_hub, deviationFactor=0.1, minSizeFactor=0.1)
hub.setMeshControls(regions=hub.cells, elemShape=TET, technique=FREE)
hub.setElementType(
    regions=(hub.cells,),
    elemTypes=(mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD),
               mesh.ElemType(elemCode=C3D6,  elemLibrary=STANDARD),
               mesh.ElemType(elemCode=C3D4,  elemLibrary=STANDARD)))
hub.generateMesh()

wire_part = model.parts['SMAWire']
wire_part.seedPart(size=mesh_wire, deviationFactor=0.1, minSizeFactor=0.1)
wire_part.setElementType(
    regions=(wire_part.edges,),
    elemTypes=(mesh.ElemType(elemCode=B31H, elemLibrary=STANDARD),))
wire_part.generateMesh()

# =====================================================================
# ASSEMBLY
# =====================================================================

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)

assembly.Instance(name='Hub-1',     part=model.parts['Hub'],     dependent=ON)
assembly.Instance(name='SMAWire-1', part=model.parts['SMAWire'], dependent=ON)

# =====================================================================
# STEP
# =====================================================================

model.StaticStep(
    name        = 'DragStep',
    previous    = 'Initial',
    description = 'Static drag load on wire',
    nlgeom      = ON,
    maxNumInc   = 1000,
    initialInc  = 0.001,
    minInc      = 1e-8,
    maxInc      = 0.05)

# =====================================================================
# BOUNDARY CONDITION: encastre wire root at hub attachment point
# wire_start = hub_verts[0] = (-a, b) for all N
# =====================================================================

wire_inst  = assembly.instances['SMAWire-1']
attach_pt  = (wire_start[0], wire_start[1], 0.0)   # = (-a, b, 0)

wire_part    = model.parts['SMAWire']
wire_fix_v   = wire_part.vertices.getByBoundingSphere(
    center=attach_pt, radius=r_wire * 2)
wire_fix_set = wire_part.Set(vertices=wire_fix_v, name='WireFixed')

model.EncastreBC(
    name           = 'WireFixed',
    createStepName = 'DragStep',
    region         = wire_inst.sets['WireFixed'])

# =====================================================================
# DRAG LOAD: analytically distributed line load w(s) = w_scale * s
#
# s = arc length from wire_start = dot((X-wx, Y-wy), (cos_b, sin_b))
#   = (X - wx)*cos_b + (Y - wy)*sin_b
#   = (-wx*cos_b - wy*sin_b) + X*cos_b + Y*sin_b
#
# ExpressionField bakes wx, wy, cos_b, sin_b as float literals so
# Abaqus only sees X and Y as variables (as required).
# =====================================================================

wx    = wire_start[0]          # = -a
wy    = wire_start[1]          # =  b
cos_b = math.cos(beta_rad)
sin_b = math.sin(beta_rad)

arc_expr = '({:.8f} + X * {:.8f} + Y * {:.8f})'.format(
    -wx * cos_b - wy * sin_b,  # constant offset
     cos_b,                     # X coefficient
     sin_b)                     # Y coefficient

mdb.models['Model-1'].ExpressionField(
    name        = 'DragField',
    localCsys   = None,
    description = 'Arc length s along wire from hub attachment point',
    expression  = arc_expr)

wire_edge_set = assembly.Set(
    edges=wire_inst.edges.getByBoundingSphere(
        center=wire_mid, radius=L_wire * 0.6),
    name='WireEdges')

model.LineLoad(
    name             = 'DragLoad',
    createStepName   = 'DragStep',
    region           = assembly.sets['WireEdges'],
    comp3            = -w_scale,
    distributionType = FIELD,
    field            = 'DragField')

# =====================================================================
# JOB
# =====================================================================

job_name = 'SailWireDrag'

if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]

mdb.Job(
    name                 = job_name,
    model                = 'Model-1',
    description          = 'Static drag analysis of SMA sail wire',
    type                 = ANALYSIS,
    atTime               = None,
    waitMinutes          = 0,
    queue                = None,
    memory               = 90,
    memoryUnits          = PERCENTAGE,
    getMemoryFromAnalysis= True,
    explicitPrecision    = SINGLE,
    nodalOutputPrecision = SINGLE,
    echoPrint            = OFF,
    modelPrint           = OFF,
    contactPrint         = OFF,
    historyPrint         = OFF,
    userSubroutine       = '',
    scratch              = '',
    resultsFormat        = ODB,
    numCpus              = 1,
    numGPUs              = 0)

mdb.jobs[job_name].submit(consistencyChecking=OFF)
mdb.jobs[job_name].waitForCompletion()
print('Job {} completed.'.format(job_name))

# =====================================================================
# POST-PROCESSING
# =====================================================================
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- 1. READ ODB FOR MAX DEFORMATION, STRESS, STRAIN -------------------
odb       = session.openOdb(name=job_name + '.odb')
frame     = odb.steps['DragStep'].frames[-1]   # last converged frame

# Displacement magnitude (nodal)
u_field   = frame.fieldOutputs['U']
max_disp  = max(v.magnitude for v in u_field.values)

# Normal stress S11 (axial + bending; dominant for beam in bending)
# S field has components [S11, S12, S13] at each section point
s_field   = frame.fieldOutputs['S']
max_stress = max(abs(v.data[0]) for v in s_field.values)

# Normal strain E11
e_field   = frame.fieldOutputs['E']
max_strain = max(abs(v.data[0]) for v in e_field.values)

odb.close()

# --- 2. DISTRIBUTED LOAD PLOT WITH EQUATION ANNOTATION ----------------
s_arr = np.linspace(0.0, L_wire, 300)
w_arr = w_scale * s_arr * 1e3          # N/m -> mN/m

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(s_arr, w_arr, 'b-', lw=2.0)
ax.set_xlabel('Arc length  s  (m)', fontsize=11)
ax.set_ylabel('Load per unit length  (mN / m)', fontsize=11)
ax.set_title('Distributed Drag Load Along Wire  '
             '(N={}, {} km)'.format(N, altitude), fontsize=12)
ax.grid(True, alpha=0.3)

# Symbolic and numerical equation annotations
eq = (r'$w(s) = \dfrac{{2\,F_{{drag}}}}{{N \cdot L^2}}\cdot s'
      r' = \dfrac{{2 \times {:.4f}\,\mathrm{{N}}}}'
      r'{{{} \times {:.4f}^2\,\mathrm{{m}}^2}}'
      r'\cdot s = {:.4e}\cdot s\;\;[\mathrm{{N/m}}]$').format(
      F_drag, N, L_wire, w_scale)

ax.text(0.03, 0.95, eq,
        transform=ax.transAxes, fontsize=10,
        va='top', color='navy')

fig.tight_layout()
fig.savefig('distributed_load.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print('Saved: distributed_load.png')

# --- 3. WRITE RUN DATA TO TEXT FILE ------------------------------------
_elapsed = time.perf_counter() - _start_time
out_path = f'results_{run_no}.txt'

with open(out_path, 'w') as f:

    f.write('Inputs\n')
    f.write(
        'N, A_sail (m^2), altitude (km), F_drag (N), r_wire (m), d_wire (mm), '
        'R_hub (m), H_hub (m), mesh_hub (m), mesh_wire (m), '
        'E_nitinol (Pa), nu_nitinol, rho_nitinol (kg/m^3), '
        'R_sail (m), L_wire (m), beta (deg), w_scale (N/m^2)\n'
    )
    f.write(
        '{}, {}, {}, {:.6e}, {}, {:.3f}, '
        '{}, {}, {}, {}, '
        '{:.4e}, {}, {}, '
        '{:.6f}, {:.6f}, {:.4f}, '
        '{:.6e}\n'.format(
            N, A_sail, altitude, F_drag, r_wire, 2000*r_wire,
            R_hub, H_hub, mesh_hub, mesh_wire,
            E_nitinol, nu_nitinol, rho_nitinol,
            R_sail, L_wire, math.degrees(beta_rad), w_scale)
    )

    f.write('\nOutputs\n')
    f.write('max_deformation (m), max_stress_S11 (Pa), max_strain_E11, '
            'elapsed_time (s)\n')
    f.write('{:.6e}, {:.6e}, {:.6e}, {:.3f}\n'.format(
        max_disp, max_stress, max_strain, _elapsed))

print('Saved: ' + out_path)
print('Max deformation: {:.4e} m'.format(max_disp))
print('Max stress S11:  {:.4e} Pa'.format(max_stress))
print('Max strain E11:  {:.4e}'.format(max_strain))
print('Total elapsed time: {:.3f} s'.format(_elapsed))
