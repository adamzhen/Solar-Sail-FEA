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
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

_total_start = time.perf_counter()

STUDY_NO = 1.2

# =====================================================================
# FIXED PARAMETERS  (not varied in the factorial study)
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
E_nitinol   = 35.0e9
nu_nitinol  = 0.3
rho_nitinol = 6450.0
E_alum      = 69.0e9
nu_alum     = 0.33
rho_alum    = 2700.0

# =====================================================================
# FACTORIAL STUDY FACTORS  (edit these lists to change the study)
# =====================================================================

N_list        = [4, 6, 8, 10, 12]                    # number of polygon sides
d_wire_list   = [1, 1.25, 1.5, 2, 2.5, 3]          # wire diameter, mm
altitude_list = [300, 325, 350, 375, 400]               # altitude, km

# convert diameter to radius
r_wire_list = [d/2000 for d in d_wire_list]             # wire radius, (m)

n_runs = len(N_list) * len(d_wire_list) * len(altitude_list)
print('Full factorial: {} runs total'.format(n_runs))

# =====================================================================
# RESULTS FILE -- write both section headers once before the loop;
# input rows are appended run-by-run, output rows written after all runs.
# =====================================================================

results_path = f'factorial_results_{STUDY_NO}.txt'

with open(results_path, 'w') as f:
    f.write('Inputs\n')
    f.write(
        'run_no, N, A_sail (m^2), altitude (km), F_drag (N), '
        'r_wire (m), d_wire (mm), R_hub (m), H_hub (m), '
        'mesh_hub (m), mesh_wire (m), '
        'E_nitinol (GPa), nu_nitinol, rho_nitinol (kg/m^3), '
        'R_sail (m), L_wire (m), beta (deg), w_scale (N/m^2)\n'
    )

# Output rows buffered in memory; written as a block after the loop
output_rows = []

# =====================================================================
# FACTORIAL LOOP  (outer: N,  middle: r_wire,  inner: altitude)
# =====================================================================

run_no = 0

for N in N_list:
    for r_wire in r_wire_list:
        for altitude in altitude_list:

            run_no += 1
            _run_start = time.perf_counter()
            print('\n--- Run {:03d}/{:03d}  N={}  d={:.1f}mm  alt={}km ---'.format(
                run_no, n_runs, N, 2000*r_wire, altitude))

            # ----------------------------------------------------------
            # DERIVED GEOMETRY  (recomputed each run from current N,
            # r_wire, altitude; fixed params stay as declared above)
            # ----------------------------------------------------------
            F_drag    = drag_pressure_dict[altitude] * A_sail
            R_sail    = math.sqrt((2.0 * A_sail) / (N * math.sin(2.0 * math.pi / N)))
            a         = R_hub * math.sin(math.pi / N)
            b         = R_hub * math.cos(math.pi / N)
            beta_rad  = math.radians(360.0 / N)

            hub_verts = []
            for i in range(N):
                theta = math.pi / 2.0 + math.pi / N - i * (2.0 * math.pi / N)
                hub_verts.append((R_hub * math.cos(theta), R_hub * math.sin(theta)))

            wire_start = hub_verts[0]
            L_wire     = math.sqrt(R_sail**2 - b**2) - a
            wire_end   = (wire_start[0] + L_wire * math.cos(beta_rad),
                          wire_start[1] + L_wire * math.sin(beta_rad))
            wire_mid   = ((wire_start[0] + wire_end[0]) / 2.0,
                          (wire_start[1] + wire_end[1]) / 2.0,
                          0.0)
            w_scale    = 2.0 * F_drag / (N * L_wire**2)
            wx         = wire_start[0]
            wy         = wire_start[1]
            cos_b      = math.cos(beta_rad)
            sin_b      = math.sin(beta_rad)

            # ----------------------------------------------------------
            # FRESH MODEL DATABASE FOR THIS RUN
            # ----------------------------------------------------------
            Mdb()
            model = mdb.models['Model-1']

            # --- PART 1: HUB (general N-gon) ---
            s = model.ConstrainedSketch(name='__profile__',
                                        sheetSize=max(1.0, 4.0 * R_hub))
            s.setPrimaryObject(option=STANDALONE)
            for i in range(N):
                s.Line(point1=hub_verts[i], point2=hub_verts[(i + 1) % N])
            p = model.Part(name='Hub', dimensionality=THREE_D, type=DEFORMABLE_BODY)
            p = model.parts['Hub']
            p.BaseSolidExtrude(sketch=s, depth=H_hub)
            s.unsetPrimaryObject()
            del model.sketches['__profile__']

            # --- PART 2: SMA WIRE ---
            s2 = model.ConstrainedSketch(name='__profile__', sheetSize=10.0)
            s2.setPrimaryObject(option=STANDALONE)
            s2.Line(point1=wire_start, point2=wire_end)
            wire_part = model.Part(name='SMAWire', dimensionality=THREE_D,
                                   type=DEFORMABLE_BODY)
            wire_part = model.parts['SMAWire']
            wire_part.BaseWire(sketch=s2)
            s2.unsetPrimaryObject()
            del model.sketches['__profile__']

            # --- MATERIALS ---
            model.Material(name='Nitinol')
            model.materials['Nitinol'].Density(table=((rho_nitinol,),))
            model.materials['Nitinol'].Elastic(table=((E_nitinol, nu_nitinol),))
            model.Material(name='Aluminum')
            model.materials['Aluminum'].Density(table=((rho_alum,),))
            model.materials['Aluminum'].Elastic(table=((E_alum, nu_alum),))

            # --- SECTIONS ---
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
                name='HubSection', material='Aluminum', thickness=None)

            # --- SECTION ASSIGNMENTS ---
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
            wire_part.assignBeamSectionOrientation(
                region=wire_set, method=N1_COSINES, n1=(0.0, 0.0, 1.0))

            # --- MESHING ---
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

            # --- ASSEMBLY ---
            assembly = model.rootAssembly
            assembly.DatumCsysByDefault(CARTESIAN)
            assembly.Instance(name='Hub-1',     part=model.parts['Hub'],     dependent=ON)
            assembly.Instance(name='SMAWire-1', part=model.parts['SMAWire'], dependent=ON)

            # --- STEP ---
            model.StaticStep(
                name        = 'DragStep',
                previous    = 'Initial',
                description = 'Static drag load on wire',
                nlgeom      = ON,
                maxNumInc   = 1000,
                initialInc  = 0.001,
                minInc      = 1e-8,
                maxInc      = 0.05)

            # --- BOUNDARY CONDITION ---
            wire_inst  = assembly.instances['SMAWire-1']
            attach_pt  = (wire_start[0], wire_start[1], 0.0)
            wire_part  = model.parts['SMAWire']
            wire_fix_v = wire_part.vertices.getByBoundingSphere(
                center=attach_pt, radius=r_wire * 2)
            wire_fix_set = wire_part.Set(vertices=wire_fix_v, name='WireFixed')
            model.EncastreBC(
                name='WireFixed', createStepName='DragStep',
                region=wire_inst.sets['WireFixed'])

            # --- DRAG LOAD ---
            arc_expr = '({:.8f} + X * {:.8f} + Y * {:.8f})'.format(
                -wx * cos_b - wy * sin_b, cos_b, sin_b)
            mdb.models['Model-1'].ExpressionField(
                name='DragField', localCsys=None,
                description='Arc length s along wire from hub attachment point',
                expression=arc_expr)
            wire_edge_set = assembly.Set(
                edges=wire_inst.edges.getByBoundingSphere(
                    center=wire_mid, radius=L_wire * 0.6),
                name='WireEdges')
            model.LineLoad(
                name='DragLoad', createStepName='DragStep',
                region=assembly.sets['WireEdges'],
                comp3=-w_scale, distributionType=FIELD, field='DragField')

            # --- JOB ---
            job_name = 'Run{:03d}'.format(run_no)
            mdb.Job(
                name                 = job_name,
                model                = 'Model-1',
                description          = 'Run {:03d}: N={} d={:.1f}mm alt={}km'.format(
                                       run_no, N, 2000*r_wire, altitude),
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
            print('  Job {} completed.'.format(job_name))

            # ----------------------------------------------------------
            # POST-PROCESSING
            # ----------------------------------------------------------

            # ODB results
            odb        = session.openOdb(name=job_name + '.odb')
            frame      = odb.steps['DragStep'].frames[-1]
            u_field    = frame.fieldOutputs['U']
            s_field    = frame.fieldOutputs['S']
            e_field    = frame.fieldOutputs['E']
            max_disp   = max(v.magnitude for v in u_field.values)
            max_stress = max(abs(v.data[0]) for v in s_field.values)
            max_strain = max(abs(v.data[0]) for v in e_field.values)
            odb.close()

            _run_elapsed = time.perf_counter() - _run_start

            # Distributed load plot (unique file per run)
            # s_arr = np.linspace(0.0, L_wire, 300)
            # w_arr = w_scale * s_arr * 1e3
            # fig, ax = plt.subplots(figsize=(8, 4.5))
            # ax.plot(s_arr, w_arr, 'b-', lw=2.0)
            # ax.set_xlabel('Arc length  s  (m)', fontsize=11)
            # ax.set_ylabel('Load per unit length  (mN / m)', fontsize=11)
            # ax.set_title('Distributed Drag Load  Run {:03d}  '
            #              '(N={}  d={:.1f}mm  {}km)'.format(
            #              run_no, N, 2000*r_wire, altitude), fontsize=12)
            # ax.grid(True, alpha=0.3)
            # eq = (r'$w(s) = \dfrac{{2\,F_{{drag}}}}{{N \cdot L^2}}\cdot s'
            #       r' = \dfrac{{2 \times {:.4f}\,\mathrm{{N}}}}'
            #       r'{{{} \times {:.4f}^2\,\mathrm{{m}}^2}}'
            #       r'\cdot s = {:.4e}\cdot s\;\;[\mathrm{{N/m}}]$').format(
            #       F_drag, N, L_wire, w_scale)
            # ax.text(0.03, 0.95, eq, transform=ax.transAxes,
            #         fontsize=10, va='top', color='navy')
            # fig.tight_layout()
            # fig.savefig('distributed_load_run{:03d}.png'.format(run_no),
            #             dpi=150, bbox_inches='tight')
            # plt.close(fig)

            # Append input data row
            with open(results_path, 'a') as f:
                f.write(
                    '{}, {}, {}, {}, {:.6e}, {}, {:.3f}, '
                    '{}, {}, {}, {}, '
                    '{:.2f}, {}, {}, '
                    '{:.6f}, {:.6f}, {:.4f}, '
                    '{:.6e}\n'.format(
                        run_no, N, A_sail, altitude, F_drag,
                        r_wire, 2000*r_wire,
                        R_hub, H_hub, mesh_hub, mesh_wire,
                        E_nitinol / (1E9), nu_nitinol, rho_nitinol,
                        R_sail, L_wire, math.degrees(beta_rad), w_scale)
                )
            
            wire_mass = N * np.pi * r_wire**2 * L_wire * rho_nitinol  # total mass of nitinol wires (kg)

            # Buffer output row
            output_rows.append(
                '{}, {:.4f}, {:.6e}, {:.6e}, {:.6e}, {:.3f}\n'.format(
                    run_no, wire_mass, max_disp, max_stress, max_strain, _run_elapsed)
            )

            print('  wire_mass={:.4f} kg  max_disp={:.4e} m  max_stress={:.4e} Pa  '
                  'max_strain={:.4e}  t={:.1f}s'.format(
                  wire_mass, max_disp, max_stress, max_strain, _run_elapsed))

# =====================================================================
# WRITE OUTPUTS SECTION  (after all runs so the block is contiguous)
# =====================================================================

with open(results_path, 'a') as f:
    f.write('\nOutputs\n')
    f.write('run_no, wire_mass (kg), max_deformation (m), max_stress_S11 (Pa), '
            'max_strain_E11, elapsed_time (s)\n')
    for row in output_rows:
        f.write(row)

_total_elapsed = time.perf_counter() - _total_start
print('\nAll {} runs complete.  Total time: {:.1f} s'.format(run_no, _total_elapsed))
print('Results saved to: ' + results_path)