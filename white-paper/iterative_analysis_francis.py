# THIS VERSION IS ITERATIVE & USES STATICSTEP. THIS IS THE OFFICIAL VERSION


# ==============================================================================
# ABAQUS PYTHON SCRIPT: SMA WIRE BATCH SIMULATION
# ==============================================================================


from abaqus import *
from abaqusConstants import *
import mesh, xyPlot, job
import csv


# ------------------------------------------------------------------------------
# Shared input variables
# ------------------------------------------------------------------------------
sail_areas = [20, 50, 100, 150, 200] # m^2
wire_diameters = [0.0005, 0.0010, 0.0015, 0.0020, 0.0025] # m


Nitinol_Density = 6450.0 # kg/m^3
Nitinol_Elastic_Modulus = 35.0e9 # Pa
Poissons_Ratio = 0.3
Wire_Section_Poissons_Ratio = 0.3


Number_wires = 8
Sail_Angular_Acceleration = 1e-06 # Assumed max angular acceleration undergone by sail (rad/s^2)


Solar_Irradiance = 5444 # W/m² at 0.5 AU
Sail_Reflectivity = 1 # Reflection efficiency of sail from 0-1


Equatorial_Radius_km = 6378.14 # Earth radius (km)
GM_km3_s2 = 398600.4355 # Standard Gravitational Parameter μ (km^3/s^2)
Deorbit_Altitude_km = 300.0 # Altitude (km)  ASUMED IN WHITE PAPER
Air_Density = 1.916e-11 # Atmospheric density ρ at 300 km (kg/m^3)
Drag_Coefficient = 2.2 # Aerodynamic drag coefficient Cd for low earth orbit


Elements_Per_Meter = 64 # How many elements exist per meter of wire. Adjusted to determine minimum amount for convergence. Determined in convergence study.


# ------------------------------------------------------------------------------
# Single-case solver
# ------------------------------------------------------------------------------
def run_case(case_id, sail_area, wire_diameter, elements_per_meter):
    """Build, solve, and extract results for one sail-area/wire-diameter case."""


    # Fresh model for every case; all Abaqus object names use case_id where needed.
    try:
        del mdb.models['Model-1']
    except KeyError:
        pass
    model = mdb.Model(name='Model-1')


    # Derived geometry
    area_wire_length = ((sail_area) / (2.0 * (2.0)**0.5))**0.5


    # --------------------------------------------------------------------------
    # 1. INITIALIZATION & SKETCHING
    # --------------------------------------------------------------------------
    sketch_name = 'Wire_Sketch_' + case_id
    part_name = 'SMA_Wire_' + case_id


    sketch = model.ConstrainedSketch(name=sketch_name, sheetSize=200.0)
    sketch.Line(point1=(0.0, 0.0), point2=(area_wire_length, 0.0))
    sketch.HorizontalConstraint(entity=sketch.geometry[2], addUndoState=False)


    part = model.Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    part.BaseWire(sketch=sketch)
    del model.sketches[sketch_name]


    # --------------------------------------------------------------------------
    # 2. MATERIALS, PROFILES, & SECTIONS
    # --------------------------------------------------------------------------
    profile_name = 'Profile_' + case_id
    material_name = 'Nitinol_' + case_id
    section_name = 'Section_' + case_id
    wire_edge_set_name = 'Wire_Edge_Set_' + case_id


    model.CircularProfile(name=profile_name, r=wire_diameter / 2.0)


    mat = model.Material(name=material_name)
    mat.Density(table=((Nitinol_Density,),))
    mat.Elastic(table=((Nitinol_Elastic_Modulus, Poissons_Ratio),))


    model.BeamSection(
        name=section_name,
        integration=DURING_ANALYSIS,
        poissonRatio=Wire_Section_Poissons_Ratio,
        profile=profile_name,
        material=material_name,
        temperatureVar=LINEAR,
        beamSectionOffset=(0.0, 0.0),
        consistentMassMatrix=False
    )


    region = part.Set(
        edges=part.edges.getSequenceFromMask(mask=('[#1 ]',),),
        name=wire_edge_set_name
    )
    part.SectionAssignment(
        region=region,
        sectionName=section_name,
        offset=0.0,
        offsetType=MIDDLE_SURFACE,
        thicknessAssignment=FROM_SECTION
    )
    part.assignBeamSectionOrientation(
        region=region,
        method=N1_COSINES,
        n1=(0.0, 0.0, -1.0)
    )


    # --------------------------------------------------------------------------
    # 3. ASSEMBLY & MESHING
    # --------------------------------------------------------------------------
    assembly = model.rootAssembly
    assembly.DatumCsysByDefault(CARTESIAN)


    instance_name = 'Instance_' + case_id
    instance = assembly.Instance(name=instance_name, part=part, dependent=ON)


    part.seedPart(
        size=1.0 / elements_per_meter,
        deviationFactor=0.1,
        minSizeFactor=0.1
    )
    elem_type = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
    part.setElementType(
        regions=(part.edges.getSequenceFromMask(mask=('[#1 ]',),),),
        elemTypes=(elem_type,)
    )
    part.generateMesh()
    assembly.regenerate()


    # --------------------------------------------------------------------------
    # 4. STEP, BOUNDARY CONDITIONS, SOLUTION CONTROLS, & LOADS
    # --------------------------------------------------------------------------
    step_name = 'Load_Step_' + case_id


    model.StaticStep(
        name=step_name,
        previous='Initial',
        nlgeom=ON,
        timePeriod=1.0,
        timeIncrementationMethod=AUTOMATIC,
        initialInc=0.001,
        minInc=1e-10,
        maxInc=0.02,
        maxNumInc=10000
    )


    root_set_name = 'Root_Node_Set_' + case_id
    root_region = assembly.Set(
        vertices=instance.vertices.getSequenceFromMask(mask=('[#1 ]',),),
        name=root_set_name
    )
    model.EncastreBC(
        name='ENCASTRE_BC_' + case_id,
        createStepName='Initial',
        region=root_region
    )


    assembly_wire_set_name = 'Assembly_Wire_Set_' + case_id
    wire_region = assembly.Set(
        edges=instance.edges.getSequenceFromMask(mask=('[#1 ]',),),
        name=assembly_wire_set_name
    )
    model.RotationalBodyForce(
        name='Angular_Acceleration_Load_' + case_id,
        createStepName=step_name,
        region=wire_region,
        magnitude=Sail_Angular_Acceleration,
        centrifugal=OFF,
        rotaryAcceleration=ON,
        point1=(0.0, 0.0, 0.0),
        point2=(0.0, 0.0, 1.0)
    )


    # Distributed SRP and drag are represented as equivalent nodal CF2 loads.
    srp_total_force_on_sail = (
        Solar_Irradiance * sail_area * (1.0 + Sail_Reflectivity)
    ) / (2.998e+8)


    drag_total_force_on_sail = (
        0.5 * Air_Density *
        (((GM_km3_s2 / (Equatorial_Radius_km + Deorbit_Altitude_km))**0.5) * 1000.0)**2 *
        Drag_Coefficient * sail_area
    )


    all_nodes = sorted(instance.nodes, key=lambda n: n.coordinates[0])
    total_nodes = len(all_nodes)


    for load_label, total_force in [
        ('SRP', srp_total_force_on_sail),
        ('Drag', drag_total_force_on_sail)
    ]:
        force_coefficient = (2.0 * total_force) / (
            Number_wires * (area_wire_length**2)
        )


        for i, node in enumerate(all_nodes):
            r_current_node_dist = round(node.coordinates[0], 6)
            w_current_node_force = force_coefficient * r_current_node_dist


            if abs(w_current_node_force) < 1e-12:
                continue


            node_set_name = f'{load_label}_Node_Set_{case_id}_{i + 1}'
            load_name = f'{load_label}_Load_{case_id}_{i + 1}'
            node_set = assembly.Set(
                nodes=instance.nodes.sequenceFromLabels((node.label,)),
                name=node_set_name
            )


            if i == 0:
                half_prev = 0.0
            else:
                r_prev = round(all_nodes[i - 1].coordinates[0], 6)
                w_prev = force_coefficient * r_prev
                w_avg_prev = (w_current_node_force + w_prev) / 2.0
                half_prev = (
                    w_avg_prev * (r_current_node_dist - r_prev)
                ) / 2.0


            if i == total_nodes - 1:
                half_next = 0.0
            else:
                r_next = round(all_nodes[i + 1].coordinates[0], 6)
                w_next = force_coefficient * r_next
                w_avg_next = (w_current_node_force + w_next) / 2.0
                half_next = (
                    w_avg_next * (r_next - r_current_node_dist)
                ) / 2.0


            model.ConcentratedForce(
                name=load_name,
                createStepName=step_name,
                region=node_set,
                cf2=-1.0 * (half_prev + half_next),
                distributionType=UNIFORM,
                field=''
            )


    # --------------------------------------------------------------------------
    # 5. JOB SUBMISSION
    # --------------------------------------------------------------------------
    job_name = 'Job_' + case_id
    if job_name in mdb.jobs:
        del mdb.jobs[job_name]


    analysis_job = mdb.Job(
        name=job_name,
        model='Model-1',
        description='',
        type=ANALYSIS,
        memory=90,
        memoryUnits=PERCENTAGE,
        getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE,
        nodalOutputPrecision=SINGLE,
        resultsFormat=ODB
    )
    analysis_job.submit(consistencyChecking=OFF)
    analysis_job.waitForCompletion()


    if analysis_job.status != COMPLETED:
        raise RuntimeError(
            f'Job status: {analysis_job.status}'
        )


    # --------------------------------------------------------------------------
    # 6. POST-PROCESSING & RESULT EXTRACTION
    # --------------------------------------------------------------------------
    odb = session.openOdb(name=job_name + '.odb')
    final_frame = odb.steps[step_name].frames[-1]
    final_step_time = final_frame.frameValue


    disp_field = final_frame.fieldOutputs['U']
    max_disp = max(v.magnitude for v in disp_field.values)


    exclusion_distance = 0.01
    stress_field = final_frame.fieldOutputs['S']
    stress_field_nodal = stress_field.getSubset(position=ELEMENT_NODAL)
    mises_stress_field = stress_field_nodal.getScalarField(invariant=MISES)
    r_by_label = {
        node.label: round(node.coordinates[0], 6)
        for node in all_nodes
    }
    filtered_stresses = [
        v.data for v in mises_stress_field.values
        if r_by_label.get(v.nodeLabel, 0.0) >= exclusion_distance
    ]


    if not filtered_stresses:
        odb.close()
        raise RuntimeError(
            f'No ELEMENT_NODAL Mises stress values were found beyond '
            f'{exclusion_distance} m for case {case_id}.'
        )


    max_stress = max(filtered_stresses)


    # Keep the old direct XY displacement plot behavior, now namespaced per case.
    r_vals = []
    u_vals = []
    disp_by_label = {v.nodeLabel: v.magnitude for v in disp_field.values}
    for node in all_nodes:
        r_vals.append(round(node.coordinates[0], 6))
        u_vals.append(disp_by_label[node.label])


    xy_data_name = 'Tip_Deflection_Direct_' + case_id
    if xy_data_name in session.xyDataObjects:
        del session.xyDataObjects[xy_data_name]


    xy_data = session.XYData(
        name=xy_data_name,
        data=list(zip(r_vals, u_vals))
    )


    xy_plot_name = 'XYPlot_' + case_id
    if xy_plot_name in session.xyPlots:
        xy_plot = session.xyPlots[xy_plot_name]
    else:
        xy_plot = session.XYPlot(xy_plot_name)


    chart = xy_plot.charts[xy_plot.charts.keys()[0]]
    curve = session.Curve(xyData=xy_data)
    chart.setValues(curvesToPlot=(curve,))


    if 'Viewport: 1' in session.viewports:
        viewport = session.viewports['Viewport: 1']


        viewport.setValues(displayedObject=odb)
        viewport.odbDisplay.setPrimaryVariable(
            variableLabel='U',
            outputPosition=NODAL,
            refinement=(INVARIANT, 'Magnitude')
        )


        viewport.setValues(displayedObject=xy_plot)


    print(f'Case: {case_id}')
    print(
        f'Frame index used: {len(odb.steps[step_name].frames) - 1} '
        f'Final step time: {final_step_time}'
    )


    print(f'Max displacement (m): {max_disp}')
    print(f'Max Mises stress excluding root region (Pa): {max_stress}')


    odb.close()


    return {
        'case_id': case_id,
        'sail_area': sail_area,
        'wire_diameter': wire_diameter,
        'elements_per_meter': elements_per_meter,
        'job_status': 'COMPLETED',
        'error_message': '',
        'final_step_time': final_step_time,
        'max_displacement_m': max_disp,
        'max_stress_pa': max_stress
    }


# ------------------------------------------------------------------------------
# BATCH DRIVER: ALL SAIL-AREA / WIRE-DIAMETER COMBINATIONS
# ------------------------------------------------------------------------------
results = []


for sail_area in sail_areas:
    for wire_diameter in wire_diameters:
        diameter_label = str(wire_diameter).replace('.', 'p')
        case_id = f'A{sail_area}_D{diameter_label}'


        print(f'Running case: {case_id}')


        try:
            result = run_case(
                case_id=case_id,
                sail_area=sail_area,
                wire_diameter=wire_diameter,
                elements_per_meter=Elements_Per_Meter
            )


        except Exception as error:
            result = {
                'case_id': case_id,
                'sail_area': sail_area,
                'wire_diameter': wire_diameter,
                'elements_per_meter': Elements_Per_Meter,
                'job_status': 'FAILED',
                'error_message': str(error),
                'final_step_time': '',
                'max_displacement_m': '',
                'max_stress_pa': ''
            }


            print(f'FAILED: {case_id}')
            print(f'Error: {error}')


        results.append(result)
        print(result)


# ------------------------------------------------------------------------------
# WRITE BATCH RESULTS TO CSV
# ------------------------------------------------------------------------------
csv_path = 'convergence_results_batch.csv'


with open(csv_path, 'w') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            'case_id',
            'sail_area',
            'wire_diameter',
            'elements_per_meter',
            'job_status',
            'error_message',
            'final_step_time',
            'max_displacement_m',
            'max_stress_pa'
        ]
    )
    writer.writeheader()


    for result in results:
        writer.writerow(result)


# Writes results to a csv file. Rewrite into preexisting csv file. Must save csv file if you want to save data, else file will be overwritten.
print(f'Results written to: {csv_path}')




