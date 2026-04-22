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

session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

if 'Viewport: 1' in session.viewports.keys():
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        legendFont='-*-verdana-medium-r-normal-*-*-720-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        titleFont='-*-verdana-medium-r-normal-*-*-480-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        stateFont='-*-verdana-medium-r-normal-*-*-480-*-*-p-*-*-*')
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
        triadFont='-*-verdana-bold-r-normal-*-*-480-*-*-p-*-*-*')

# start timer
_start_time = time.perf_counter()

######################################
# Variable and Fixed Design Parameters
######################################

##########################
# FEA Modeling Parameters
##########################

####################################
### Calculated Properties/Values ###
####################################

#####################################
### Generation of SOLID FEA Model ###
#####################################

Mdb()
model = mdb.models['Model-1']

# =====================================================================
# PARAMETERS
# =====================================================================

# Design parameters
N         = 8         # number of sides of polygon
A_sail    = 9         # area of sail, m^2
R_hub     = 0.03      # hub circumradius, m
H_hub     = 0.05      # hub height, m
r_wire    = 0.001     # wire radius, m
mesh_hub  = 0.02      # global mesh size for hub, m
mesh_wire = 0.1       # global mesh size for wire, m
#F_drag    = 0.0041    # total drag force on sail, N

# Scenario parameters
altitude  = 325       # altitude, km   
drag_pressure_dict = {  300: 0.0012580, # altitude (km): drag pressure (Pa)
                        325: 0.0007627, 
                        350: 0.0004571, 
                        375: 0.0003129, 
                        400: 0.0001813}
F_drag    = drag_pressure_dict[altitude] * A_sail # total drag force on sail, N  

# Material properties
E_nitinol   = 40.0e9   # Nitinol Young's modulus, Pa
E_alum      = 69.0e9   # Aluminum Young's modulus, Pa
nu_nitinol  = 0.3
nu_alum     = 0.33
rho_nitinol = 6450.0
rho_alum    = 2700.0

# =====================================================================
# DERIVED GEOMETRY
# =====================================================================

R_sail = math.sqrt((2.0 * A_sail) / (N * math.sin(2.0 * math.pi / N))) # sail circumradius, m

beta = 360 / N   # wire exit angle from polygon side, degrees

a        = R_hub * math.sin(math.pi / N)
b        = R_hub * math.cos(math.pi / N)
beta_rad = math.radians(beta)

L_wire  = math.sqrt(R_sail**2 - b**2) - a 
#print('Wire length: {:.3f} m'.format(L_wire))
f_drag    = F_drag / N / L_wire    # average drag force per unit length, N/m

wire_start = (-a, b)
wire_end   = (wire_start[0] + L_wire * math.cos(beta_rad),
              wire_start[1] + L_wire * math.sin(beta_rad))
wire_mid   = ((wire_start[0] + wire_end[0]) / 2.0,
              (wire_start[1] + wire_end[1]) / 2.0,
              0.0)

# =====================================================================
# PART 1: HUB (visualization only -- not constrained or loaded)
# =====================================================================
if 'Hub' in model.parts.keys():
    del model.parts['Hub']
if '__profile__' in model.sketches.keys():
    del model.sketches['__profile__']

s = model.ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)

p1 = (-a,  b);  p2 = ( a,  b)
p3 = ( b,  a);  p4 = ( b, -a)
p5 = ( a, -b);  p6 = (-a, -b)
p7 = (-b, -a);  p8 = (-b,  a)

s.Line(point1=p1, point2=p2)
s.HorizontalConstraint(entity=g.findAt((0.0, b)), addUndoState=False)
s.Line(point1=p2, point2=p3)
s.Line(point1=p3, point2=p4)
s.VerticalConstraint(entity=g.findAt((b, 0.0)), addUndoState=False)
s.Line(point1=p4, point2=p5)
s.Line(point1=p5, point2=p6)
s.HorizontalConstraint(entity=g.findAt((0.0, -b)), addUndoState=False)
s.Line(point1=p6, point2=p7)
s.Line(point1=p7, point2=p8)
s.VerticalConstraint(entity=g.findAt((-b, 0.0)), addUndoState=False)
s.Line(point1=p8, point2=p1)

p = model.Part(name='Hub', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = model.parts['Hub']
p.BaseSolidExtrude(sketch=s, depth=H_hub)
s.unsetPrimaryObject()
del model.sketches['__profile__']

# =====================================================================
# PART 2: SMA WIRE (3D BEAM)
# =====================================================================
if 'SMAWire' in model.parts.keys():
    del model.parts['SMAWire']

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
for mat in ['Nitinol', 'Aluminum']:
    if mat in model.materials.keys():
        del model.materials[mat]

model.Material(name='Nitinol')
model.materials['Nitinol'].Density(table=((rho_nitinol,),))
model.materials['Nitinol'].Elastic(table=((E_nitinol, nu_nitinol),))

model.Material(name='Aluminum')
model.materials['Aluminum'].Density(table=((rho_alum,),))
model.materials['Aluminum'].Elastic(table=((E_alum, nu_alum),))

# =====================================================================
# SECTIONS
# =====================================================================
for prof in ['WireProfile']:
    if prof in model.profiles.keys():
        del model.profiles[prof]
for sec in ['WireSection', 'HubSection']:
    if sec in model.sections.keys():
        del model.sections[sec]

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
# Hub: free tet mesh (visualization only).
# Wire: B31H hybrid beam elements -- required for slender wire
#       (slenderness L/r = 3000).
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
# ASSEMBLY INSTANCES
# Hub included for visualization only -- no BCs, loads, or constraints.
# =====================================================================
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)

for inst in ['Hub-1', 'SMAWire-1']:
    if inst in assembly.instances.keys():
        del assembly.instances[inst]

assembly.Instance(name='Hub-1',     part=model.parts['Hub'],    dependent=ON)
assembly.Instance(name='SMAWire-1', part=model.parts['SMAWire'], dependent=ON)

# =====================================================================
# STEP
# =====================================================================
if 'DragStep' in model.steps.keys():
    del model.steps['DragStep']

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
# BOUNDARY CONDITION: encastre the wire attachment end
# Defined at part level -- survives re-meshing.
# =====================================================================
wire_inst  = assembly.instances['SMAWire-1']
attach_pt  = (-a, b, 0.0)

wire_part    = model.parts['SMAWire']
wire_fix_v   = wire_part.vertices.getByBoundingSphere(
    center=attach_pt, radius=r_wire * 2)
wire_fix_set = wire_part.Set(vertices=wire_fix_v, name='WireFixed')

model.EncastreBC(
    name           = 'WireFixed',
    createStepName = 'DragStep',
    region         = wire_inst.sets['WireFixed'])

# =====================================================================
# DRAG LOAD: distributed line load w(s) = w_scale * s
# s = arc length along wire from hub attachment point
# s = dot( (X - wx, Y - wy), (cos(beta), sin(beta)) )
#   = (X - wx)*cos(beta) + (Y - wy)*sin(beta)
# w_scale = 2 * F_drag / (N * L_wire^2)
# Effective load per unit length in -Z = -w_scale * s
# =====================================================================

wx       = wire_start[0]          # X coord of wire root (hub attachment)
wy       = wire_start[1]          # Y coord of wire root
cos_b    = math.cos(beta_rad)
sin_b    = math.sin(beta_rad)
w_scale  = 2.0 * F_drag / (N * L_wire**2)

arc_expr = '({:.8f} + X * {:.8f} + Y * {:.8f})'.format(
    -wx * cos_b - wy * sin_b,   # constant offset term
     cos_b,                      # X coefficient
     sin_b)                      # Y coefficient

mdb.models['Model-1'].ExpressionField(
    name        = 'DragField',
    localCsys   = None,
    description = 'Arc length s along wire from hub attachment',
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
# JOB: create and submit
# numCpus and numGPUs can be increased if your machine supports it.
# waitForCompletion=False returns immediately; remove to block until done.
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
# POST-PROCESSING: Plot distributed load w(s) along wire
# =====================================================================
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

s      = np.linspace(0.0, L_wire, 300)
w      = w_scale * s * 1e3          # convert to mN/m

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(s, w, 'b-', lw=2.0)
ax.set_xlabel('Arc length  s  (m)')
ax.set_ylabel('Load per unit length  (mN / m)')
ax.set_title('Distributed Drag Load Along Wire')
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('distributed_load.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print('Saved: distributed_load.png')

# Calculate total elapsed time
_elapsed = time.perf_counter() - _start_time
print("Total script elapsed time: %.3f seconds" % _elapsed)