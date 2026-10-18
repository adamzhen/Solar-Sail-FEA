# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-08.00.46 RELr427 198590
# Run by adzheng on Sat Oct 17 13:11:02 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=305.930206298828, 
    height=156.505554199219)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('C:/Users/adzheng/Solar-Sail-FEA/polygon_sail_sim.py', 
    __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: N=8, R_sail=5.9460 m, a=0.01148 m, b=0.02772 m
#: L_wire=5.9345 m, F_drag=0.018130 N, w_scale=1.2870e-04 N/m^2
#: Job SailWireDrag: Analysis Input File Processor completed successfully.
#: Job SailWireDrag: Abaqus/Standard completed successfully.
#: Job SailWireDrag completed successfully. 
#: Job SailWireDrag completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Saved: distributed_load.png
#: Saved: results_0.1.txt
#: Max deformation: 4.8828e+00 m
#: Max stress S11:  1.8276e+07 Pa
#: Max strain E11:  4.5691e-04
#: Total elapsed time: 19.119 s
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='DragStep', frame=29)
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.20158, 
    farPlane=14.7918, width=12.6685, height=4.81777, viewOffsetX=0.411198, 
    viewOffsetY=-0.021119)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='DragStep', frame=29)
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='DragStep', frame=29)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
execfile('C:/Users/adzheng/Solar-Sail-FEA/polygon_sail_sim.py', 
    __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: N=8, R_sail=1.8803 m, a=0.01148 m, b=0.02772 m
#: L_wire=1.8686 m, F_drag=0.004571 N, w_scale=3.2727e-04 N/m^2
#: Job SailWireDrag: Analysis Input File Processor completed successfully.
#: Job SailWireDrag: Abaqus/Standard completed successfully.
#: Job SailWireDrag completed successfully. 
#: Job SailWireDrag completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Saved: distributed_load.png
#: Saved: results_0.1.txt
#: Max deformation: 6.8652e-02 m
#: Max stress S11:  2.0608e+06 Pa
#: Max strain E11:  5.1519e-05
#: Total elapsed time: 18.379 s
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='DragStep', frame=26)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='DragStep', frame=29)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='DragStep', frame=29)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.02257, 
    farPlane=4.67578, width=1.61543, height=0.61434, viewOffsetX=-0.00103477, 
    viewOffsetY=-0.0205809)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.01442, 
    farPlane=4.68392, width=1.61108, height=0.612684, viewOffsetX=0.0643924, 
    viewOffsetY=0.0468698)
session.viewports['Viewport: 1'].view.setValues(width=1.7139, height=0.651789, 
    viewOffsetX=0.0662189, viewOffsetY=0.0431543)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='DragStep', frame=29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.91675, 
    farPlane=4.77453, width=1.65838, height=0.630675, cameraPosition=(-1.07915, 
    -1.69828, -2.49572), cameraUpVector=(0.748523, 0.127158, -0.650802), 
    cameraTarget=(0.723547, 0.585931, 0.023964), viewOffsetX=0.0640739, 
    viewOffsetY=0.0417564)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.71405, 
    farPlane=4.97724, width=4.15296, height=1.57935, viewOffsetX=0.064039, 
    viewOffsetY=-0.024035)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.17566, 
    farPlane=4.52457, width=4.8593, height=1.84797, cameraPosition=(0.711671, 
    -0.66057, -3.60677), cameraUpVector=(0.999946, 0.0100177, 0.00294888), 
    cameraTarget=(0.688614, 0.567095, 0.0413054), viewOffsetX=0.074931, 
    viewOffsetY=-0.028123)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.29889, 
    farPlane=4.39945, width=5.45277, height=2.07366, viewOffsetX=0.140488, 
    viewOffsetY=0.170021)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.27657, 
    farPlane=4.42177, width=5.41588, height=2.05963, viewOffsetX=0.0742441, 
    viewOffsetY=-0.0405258)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.7197, 
    farPlane=3.97865, width=0.517453, height=0.196785, viewOffsetX=-0.560003, 
    viewOffsetY=-0.634116)
execfile('C:/Users/adzheng/Solar-Sail-FEA/polygon_sail_sim.py', 
    __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: N=8, R_sail=1.8803 m, a=0.01148 m, b=0.02772 m
#: L_wire=1.8686 m, F_drag=0.004571 N, w_scale=3.2727e-04 N/m^2
#: Job SailWireDrag: Analysis Input File Processor completed successfully.
#: Job SailWireDrag: Abaqus/Standard completed successfully.
#: Job SailWireDrag completed successfully. 
#: Job SailWireDrag completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              1
#: Saved: distributed_load.png
#: Saved: results_0.1.txt
#: Max deformation: 6.8652e-02 m
#: Max stress S11:  2.0608e+06 Pa
#: Max strain E11:  5.1519e-05
#: Tip U1: 1.4576e-03 m
#: Tip U2: -4.9601e-17 m
#: Tip U3: -6.8636e-02 m
#: Total elapsed time: 19.025 s
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/SailWireDrag.odb'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.59736, 
    farPlane=4.0456, width=2.28694, height=0.869713, viewOffsetX=0.0458183, 
    viewOffsetY=0.0198913)
execfile('C:/Users/adzheng/Solar-Sail-FEA/polygon_sail_study_v2.py', 
    __main__.__dict__)
#: Study: 36 runs (4 diameters x 9 altitudes)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 001/036 d=1.5 mm alt=400 km ---
#: The model "Cold_1p5_400" has been created.
#: Job D1p5_A400_cold: Analysis Input File Processor completed successfully.
#: Job D1p5_A400_cold: Abaqus/Standard completed successfully.
#: Job D1p5_A400_cold completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A400_cold.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=2.3908e-02 m  tip U=(1.864e-04, -1.711e-17, -2.391e-02) m
#:   A_proj=8.99812  A_drag=8.99436 m^2  [cold]  t=18.1s
#: 
#: --- Run 002/036 d=1.5 mm alt=375 km ---
#: The model "Rst_1p5_375" has been created.
#: Job D1p5_A375_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A375_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A375_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A375_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              2
#:   F=2.81424e-03 N  max_disp=4.1220e-02 m  tip U=(5.541e-04, -2.986e-17, -4.122e-02) m
#:   A_proj=8.99441  A_drag=8.98324 m^2  [restart]  t=18.0s
#: 
#: --- Run 003/036 d=1.5 mm alt=350 km ---
#: The model "Rst_1p5_350" has been created.
#: Job D1p5_A350_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A350_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A350_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A350_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              3
#:   F=4.10640e-03 N  max_disp=6.0122e-02 m  tip U=(1.179e-03, -4.389e-17, -6.011e-02) m
#:   A_proj=8.98811  A_drag=8.96438 m^2  [restart]  t=18.0s
#: 
#: --- Run 004/036 d=1.5 mm alt=325 km ---
#: The model "Rst_1p5_325" has been created.
#: Job D1p5_A325_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A325_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A325_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A325_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              4
#:   F=6.83851e-03 N  max_disp=9.9985e-02 m  tip U=(3.260e-03, -7.249e-17, -9.993e-02) m
#:   A_proj=8.96714  A_drag=8.90184 m^2  [restart]  t=20.1s
#: 
#: --- Run 005/036 d=1.5 mm alt=300 km ---
#: The model "Rst_1p5_300" has been created.
#: Job D1p5_A300_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A300_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A300_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A300_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              5
#:   F=1.11985e-02 N  max_disp=1.6314e-01 m  tip U=(8.679e-03, -1.187e-16, -1.629e-01) m
#:   A_proj=8.91265  A_drag=8.74098 m^2  [restart]  t=20.0s
#: 
#: --- Run 006/036 d=1.5 mm alt=275 km ---
#: The model "Rst_1p5_275" has been created.
#: Job D1p5_A275_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A275_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A275_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A275_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              6
#:   F=2.24730e-02 N  max_disp=3.2192e-01 m  tip U=(3.378e-02, -2.482e-16, -3.201e-01) m
#:   A_proj=8.66238  A_drag=8.03218 m^2  [restart]  t=20.0s
#: 
#: --- Run 007/036 d=1.5 mm alt=250 km ---
#: The model "Rst_1p5_250" has been created.
#: Job D1p5_A250_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A250_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A250_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A250_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              7
#:   F=4.02658e-02 N  max_disp=5.5142e-01 m  tip U=(9.903e-02, -4.605e-16, -5.425e-01) m
#:   A_proj=8.02859  A_drag=6.44386 m^2  [restart]  t=24.1s
#: 
#: --- Run 008/036 d=1.5 mm alt=225 km ---
#: The model "Rst_1p5_225" has been created.
#: Job D1p5_A225_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A225_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A225_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A225_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              8
#:   F=6.06112e-02 N  max_disp=7.7419e-01 m  tip U=(1.949e-01, -6.006e-16, -7.493e-01) m
#:   A_proj=7.14077  A_drag=4.65841 m^2  [restart]  t=24.2s
#: 
#: --- Run 009/036 d=1.5 mm alt=200 km ---
#: The model "Rst_1p5_200" has been created.
#: Job D1p5_A200_rst: Analysis Input File Processor completed successfully.
#: Job D1p5_A200_rst: Abaqus/Standard completed successfully.
#: Job D1p5_A200_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A200_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              9
#:   F=8.82785e-02 N  max_disp=1.0122e+00 m  tip U=(3.324e-01, -6.399e-16, -9.560e-01) m
#:   A_proj=5.95914  A_drag=2.92984 m^2  [restart]  t=26.1s
#: Saved: sail_outline_d1p5mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 010/036 d=2 mm alt=400 km ---
#: The model "Cold_2_400" has been created.
#: Job D2_A400_cold: Analysis Input File Processor completed successfully.
#: Job D2_A400_cold: Abaqus/Standard completed successfully.
#: Job D2_A400_cold completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A400_cold.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=7.5654e-03 m  tip U=(1.866e-05, -5.176e-18, -7.565e-03) m
#:   A_proj=8.99981  A_drag=8.99943 m^2  [cold]  t=18.0s
#: 
#: --- Run 011/036 d=2 mm alt=375 km ---
#: The model "Rst_2_375" has been created.
#: Job D2_A375_rst: Analysis Input File Processor completed successfully.
#: Job D2_A375_rst: Abaqus/Standard completed successfully.
#: Job D2_A375_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A375_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              2
#:   F=2.81582e-03 N  max_disp=1.3054e-02 m  tip U=(5.557e-05, -9.189e-18, -1.305e-02) m
#:   A_proj=8.99944  A_drag=8.99832 m^2  [restart]  t=18.0s
#: 
#: --- Run 012/036 d=2 mm alt=350 km ---
#: The model "Rst_2_350" has been created.
#: Job D2_A350_rst: Analysis Input File Processor completed successfully.
#: Job D2_A350_rst: Abaqus/Standard completed successfully.
#: Job D2_A350_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A350_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              3
#:   F=4.11330e-03 N  max_disp=1.9068e-02 m  tip U=(1.186e-04, -1.316e-17, -1.907e-02) m
#:   A_proj=8.99880  A_drag=8.99641 m^2  [restart]  t=20.0s
#: 
#: --- Run 013/036 d=2 mm alt=325 km ---
#: The model "Rst_2_325" has been created.
#: Job D2_A325_rst: Analysis Input File Processor completed successfully.
#: Job D2_A325_rst: Abaqus/Standard completed successfully.
#: Job D2_A325_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A325_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              4
#:   F=6.86294e-03 N  max_disp=3.1811e-02 m  tip U=(3.300e-04, -2.217e-17, -3.181e-02) m
#:   A_proj=8.99667  A_drag=8.99002 m^2  [restart]  t=22.1s
#: 
#: --- Run 014/036 d=2 mm alt=300 km ---
#: The model "Rst_2_300" has been created.
#: Job D2_A300_rst: Analysis Input File Processor completed successfully.
#: Job D2_A300_rst: Abaqus/Standard completed successfully.
#: Job D2_A300_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A300_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              5
#:   F=1.13095e-02 N  max_disp=5.2401e-02 m  tip U=(8.954e-04, -3.595e-17, -5.239e-02) m
#:   A_proj=8.99097  A_drag=8.97293 m^2  [restart]  t=22.0s
#: 
#: --- Run 015/036 d=2 mm alt=275 km ---
#: The model "Rst_2_275" has been created.
#: Job D2_A275_rst: Analysis Input File Processor completed successfully.
#: Job D2_A275_rst: Abaqus/Standard completed successfully.
#: Job D2_A275_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A275_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              6
#:   F=2.30693e-02 N  max_disp=1.0669e-01 m  tip U=(3.712e-03, -7.506e-17, -1.066e-01) m
#:   A_proj=8.96259  A_drag=8.88831 m^2  [restart]  t=22.0s
#: 
#: --- Run 016/036 d=2 mm alt=250 km ---
#: The model "Rst_2_250" has been created.
#: Job D2_A250_rst: Analysis Input File Processor completed successfully.
#: Job D2_A250_rst: Abaqus/Standard completed successfully.
#: Job D2_A250_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A250_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              7
#:   F=4.45576e-02 N  max_disp=2.0471e-01 m  tip U=(1.366e-02, -1.444e-16, -2.042e-01) m
#:   A_proj=8.86267  A_drag=8.59553 m^2  [restart]  t=24.1s
#: 
#: --- Run 017/036 d=2 mm alt=225 km ---
#: The model "Rst_2_225" has been created.
#: Job D2_A225_rst: Analysis Input File Processor completed successfully.
#: Job D2_A225_rst: Abaqus/Standard completed successfully.
#: Job D2_A225_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A225_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              8
#:   F=8.08498e-02 N  max_disp=3.6411e-01 m  tip U=(4.321e-02, -2.653e-16, -3.615e-01) m
#:   A_proj=8.56930  A_drag=7.78077 m^2  [restart]  t=26.1s
#: 
#: --- Run 018/036 d=2 mm alt=200 km ---
#: The model "Rst_2_200" has been created.
#: Job D2_A200_rst: Analysis Input File Processor completed successfully.
#: Job D2_A200_rst: Abaqus/Standard completed successfully.
#: Job D2_A200_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A200_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              9
#:   F=1.47448e-01 N  max_disp=6.2603e-01 m  tip U=(1.276e-01, -4.813e-16, -6.129e-01) m
#:   A_proj=7.75876  A_drag=5.85055 m^2  [restart]  t=26.2s
#: Saved: sail_outline_d2mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 019/036 d=2.5 mm alt=400 km ---
#: The model "Cold_2p5_400" has been created.
#: Job D2p5_A400_cold: Analysis Input File Processor completed successfully.
#: Job D2p5_A400_cold: Abaqus/Standard completed successfully.
#: Job D2p5_A400_cold completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A400_cold.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=3.0988e-03 m  tip U=(3.131e-06, -2.142e-18, -3.099e-03) m
#:   A_proj=8.99997  A_drag=8.99991 m^2  [cold]  t=18.1s
#: 
#: --- Run 020/036 d=2.5 mm alt=375 km ---
#: The model "Rst_2p5_375" has been created.
#: Job D2p5_A375_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A375_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A375_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A375_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              2
#:   F=2.81597e-03 N  max_disp=5.3474e-03 m  tip U=(9.325e-06, -3.722e-18, -5.347e-03) m
#:   A_proj=8.99991  A_drag=8.99972 m^2  [restart]  t=18.0s
#: 
#: --- Run 021/036 d=2.5 mm alt=350 km ---
#: The model "Rst_2p5_350" has been created.
#: Job D2p5_A350_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A350_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A350_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A350_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              3
#:   F=4.11394e-03 N  max_disp=7.8121e-03 m  tip U=(1.990e-05, -5.408e-18, -7.812e-03) m
#:   A_proj=8.99980  A_drag=8.99940 m^2  [restart]  t=19.9s
#: 
#: --- Run 022/036 d=2.5 mm alt=325 km ---
#: The model "Rst_2p5_325" has been created.
#: Job D2p5_A325_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A325_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A325_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A325_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              4
#:   F=6.86522e-03 N  max_disp=1.3036e-02 m  tip U=(5.542e-05, -9.019e-18, -1.304e-02) m
#:   A_proj=8.99944  A_drag=8.99832 m^2  [restart]  t=22.0s
#: 
#: --- Run 023/036 d=2.5 mm alt=300 km ---
#: The model "Rst_2p5_300" has been created.
#: Job D2p5_A300_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A300_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A300_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A300_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              5
#:   F=1.13199e-02 N  max_disp=2.1494e-02 m  tip U=(1.507e-04, -1.510e-17, -2.149e-02) m
#:   A_proj=8.99848  A_drag=8.99544 m^2  [restart]  t=22.8s
#: 
#: --- Run 024/036 d=2.5 mm alt=275 km ---
#: The model "Rst_2p5_275" has been created.
#: Job D2p5_A275_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A275_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A275_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A275_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              6
#:   F=2.31272e-02 N  max_disp=4.3899e-02 m  tip U=(6.285e-04, -3.057e-17, -4.389e-02) m
#:   A_proj=8.99366  A_drag=8.98099 m^2  [restart]  t=22.0s
#: 
#: --- Run 025/036 d=2.5 mm alt=250 km ---
#: The model "Rst_2p5_250" has been created.
#: Job D2p5_A250_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A250_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A250_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A250_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              7
#:   F=4.50222e-02 N  max_disp=8.5361e-02 m  tip U=(2.376e-03, -5.992e-17, -8.533e-02) m
#:   A_proj=8.97604  A_drag=8.92835 m^2  [restart]  t=22.1s
#: 
#: --- Run 026/036 d=2.5 mm alt=225 km ---
#: The model "Rst_2p5_225" has been created.
#: Job D2p5_A225_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A225_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A225_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A225_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              8
#:   F=8.39803e-02 N  max_disp=1.5861e-01 m  tip U=(8.203e-03, -1.120e-16, -1.584e-01) m
#:   A_proj=8.91743  A_drag=8.75499 m^2  [restart]  t=24.2s
#: 
#: --- Run 027/036 d=2.5 mm alt=200 km ---
#: The model "Rst_2p5_200" has been created.
#: Job D2p5_A200_rst: Analysis Input File Processor completed successfully.
#: Job D2p5_A200_rst: Abaqus/Standard completed successfully.
#: Job D2p5_A200_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A200_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              9
#:   F=1.65910e-01 N  max_disp=3.0859e-01 m  tip U=(3.104e-02, -2.224e-16, -3.070e-01) m
#:   A_proj=8.68953  A_drag=8.10673 m^2  [restart]  t=24.2s
#: Saved: sail_outline_d2p5mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 028/036 d=3 mm alt=400 km ---
#: The model "Cold_3_400" has been created.
#: Job D3_A400_cold: Analysis Input File Processor completed successfully.
#: Job D3_A400_cold: Abaqus/Standard completed successfully.
#: Job D3_A400_cold completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A400_cold.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=1.4944e-03 m  tip U=(7.283e-07, -1.079e-18, -1.494e-03) m
#:   A_proj=8.99999  A_drag=8.99998 m^2  [cold]  t=18.1s
#: 
#: --- Run 029/036 d=3 mm alt=375 km ---
#: The model "Rst_3_375" has been created.
#: Job D3_A375_rst: Analysis Input File Processor completed successfully.
#: Job D3_A375_rst: Abaqus/Standard completed successfully.
#: Job D3_A375_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A375_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              2
#:   F=2.81599e-03 N  max_disp=2.5788e-03 m  tip U=(2.169e-06, -1.868e-18, -2.579e-03) m
#:   A_proj=8.99998  A_drag=8.99993 m^2  [restart]  t=20.0s
#: 
#: --- Run 030/036 d=3 mm alt=350 km ---
#: The model "Rst_3_350" has been created.
#: Job D3_A350_rst: Analysis Input File Processor completed successfully.
#: Job D3_A350_rst: Abaqus/Standard completed successfully.
#: Job D3_A350_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A350_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              3
#:   F=4.11404e-03 N  max_disp=3.7676e-03 m  tip U=(4.629e-06, -2.757e-18, -3.768e-03) m
#:   A_proj=8.99995  A_drag=8.99986 m^2  [restart]  t=20.0s
#: 
#: --- Run 031/036 d=3 mm alt=325 km ---
#: The model "Rst_3_325" has been created.
#: Job D3_A325_rst: Analysis Input File Processor completed successfully.
#: Job D3_A325_rst: Abaqus/Standard completed successfully.
#: Job D3_A325_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A325_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              4
#:   F=6.86557e-03 N  max_disp=6.2873e-03 m  tip U=(1.289e-05, -4.502e-18, -6.287e-03) m
#:   A_proj=8.99987  A_drag=8.99961 m^2  [restart]  t=22.0s
#: 
#: --- Run 032/036 d=3 mm alt=300 km ---
#: The model "Rst_3_300" has been created.
#: Job D3_A300_rst: Analysis Input File Processor completed successfully.
#: Job D3_A300_rst: Abaqus/Standard completed successfully.
#: Job D3_A300_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A300_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              5
#:   F=1.13215e-02 N  max_disp=1.0368e-02 m  tip U=(3.505e-05, -7.553e-18, -1.037e-02) m
#:   A_proj=8.99965  A_drag=8.99894 m^2  [restart]  t=22.1s
#: 
#: --- Run 033/036 d=3 mm alt=275 km ---
#: The model "Rst_3_275" has been created.
#: Job D3_A275_rst: Analysis Input File Processor completed successfully.
#: Job D3_A275_rst: Abaqus/Standard completed successfully.
#: Job D3_A275_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A275_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              6
#:   F=2.31362e-02 N  max_disp=2.1186e-02 m  tip U=(1.464e-04, -1.516e-17, -2.119e-02) m
#:   A_proj=8.99852  A_drag=8.99557 m^2  [restart]  t=22.1s
#: 
#: --- Run 034/036 d=3 mm alt=250 km ---
#: The model "Rst_3_250" has been created.
#: Job D3_A250_rst: Analysis Input File Processor completed successfully.
#: Job D3_A250_rst: Abaqus/Standard completed successfully.
#: Job D3_A250_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A250_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              7
#:   F=4.50953e-02 N  max_disp=4.1282e-02 m  tip U=(5.558e-04, -2.977e-17, -4.128e-02) m
#:   A_proj=8.99439  A_drag=8.98319 m^2  [restart]  t=24.1s
#: 
#: --- Run 035/036 d=3 mm alt=225 km ---
#: The model "Rst_3_225" has been created.
#: Job D3_A225_rst: Analysis Input File Processor completed successfully.
#: Job D3_A225_rst: Abaqus/Standard completed successfully.
#: Job D3_A225_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A225_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              8
#:   F=8.44961e-02 N  max_disp=7.7280e-02 m  tip U=(1.948e-03, -5.603e-17, -7.726e-02) m
#:   A_proj=8.98036  A_drag=8.94123 m^2  [restart]  t=26.1s
#: 
#: --- Run 036/036 d=3 mm alt=200 km ---
#: The model "Rst_3_200" has been created.
#: Job D3_A200_rst: Analysis Input File Processor completed successfully.
#: Job D3_A200_rst: Abaqus/Standard completed successfully.
#: Job D3_A200_rst completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A200_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              9
#:   F=1.69439e-01 N  max_disp=1.5437e-01 m  tip U=(7.771e-03, -1.129e-16, -1.542e-01) m
#:   A_proj=8.92177  A_drag=8.76774 m^2  [restart]  t=26.2s
#: Saved: sail_outline_d3mm.png
#: 
#: All 36 runs complete. Total time: 782.7 s
#: Results saved to: factorial_results_3.0.txt
a = mdb.models['Cold_3_400'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A300_rst.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A300_rst.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          6
#: Number of Steps:              5
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-300', frame=29)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
execfile('C:/Users/adzheng/Solar-Sail-FEA/polygon_sail_study_v2.py', 
    __main__.__dict__)
#: Study: 36 runs (4 diameters x 9 altitudes)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 001/036 d=1.5 mm alt=400 km ---
#: Job D1p5_A400: Analysis Input File Processor completed successfully.
#: Job D1p5_A400: Abaqus/Standard completed successfully.
#: Job D1p5_A400 completed successfully. 
#:   Job D1p5_A400 (analysis) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=2.3908e-02 m  tip U=(1.864e-04, -1.711e-17, -2.391e-02) m
#:   A_proj=8.99707  A_drag=8.99331 m^2  scallop=1.441e-04 m  t=18.0s
#: 
#: --- Run 002/036 d=1.5 mm alt=375 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A375: Analysis Input File Processor completed successfully.
#: Job D1p5_A375: Abaqus/Standard completed successfully.
#: Job D1p5_A375 completed successfully. 
#:   Job D1p5_A375 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.81391e-03 N  max_disp=4.1216e-02 m  tip U=(5.540e-04, -2.970e-17, -4.121e-02) m
#:   A_proj=8.99129  A_drag=8.98013 m^2  scallop=4.283e-04 m  t=18.0s
#: 
#: --- Run 003/036 d=1.5 mm alt=350 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A350: Analysis Input File Processor completed successfully.
#: Job D1p5_A350: Abaqus/Standard completed successfully.
#: Job D1p5_A350 completed successfully. 
#:   Job D1p5_A350 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=4.10498e-03 N  max_disp=6.0101e-02 m  tip U=(1.178e-03, -4.399e-17, -6.009e-02) m
#:   A_proj=8.98149  A_drag=8.95780 m^2  scallop=9.111e-04 m  t=18.0s
#: 
#: --- Run 004/036 d=1.5 mm alt=325 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A325: Analysis Input File Processor completed successfully.
#: Job D1p5_A325: Abaqus/Standard completed successfully.
#: Job D1p5_A325 completed successfully. 
#:   Job D1p5_A325 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=6.83349e-03 N  max_disp=9.9912e-02 m  tip U=(3.255e-03, -7.171e-17, -9.986e-02) m
#:   A_proj=8.94886  A_drag=8.88383 m^2  scallop=2.521e-03 m  t=18.1s
#: 
#: --- Run 005/036 d=1.5 mm alt=300 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A300: Analysis Input File Processor completed successfully.
#: Job D1p5_A300: Abaqus/Standard completed successfully.
#: Job D1p5_A300 completed successfully. 
#:   Job D1p5_A300 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.11759e-02 N  max_disp=1.6282e-01 m  tip U=(8.644e-03, -1.197e-16, -1.626e-01) m
#:   A_proj=8.86432  A_drag=8.69454 m^2  scallop=6.717e-03 m  t=18.0s
#: 
#: --- Run 006/036 d=1.5 mm alt=275 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A275: Analysis Input File Processor completed successfully.
#: Job D1p5_A275: Abaqus/Standard completed successfully.
#: Job D1p5_A275 completed successfully. 
#:   Job D1p5_A275 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.23536e-02 N  max_disp=3.2029e-01 m  tip U=(3.344e-02, -2.426e-16, -3.185e-01) m
#:   A_proj=8.47706  A_drag=7.87034 m^2  scallop=2.641e-02 m  t=18.1s
#: 
#: --- Run 007/036 d=1.5 mm alt=250 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A250: Analysis Input File Processor completed successfully.
#: Job D1p5_A250: Abaqus/Standard completed successfully.
#: Job D1p5_A250 completed successfully. 
#:   Job D1p5_A250 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=3.94545e-02 N  max_disp=5.4163e-01 m  tip U=(9.555e-02, -4.469e-16, -5.331e-01) m
#:   A_proj=7.51770  A_drag=6.10940 m^2  scallop=7.895e-02 m  t=18.1s
#: 
#: --- Run 008/036 d=1.5 mm alt=225 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A225: Analysis Input File Processor completed successfully.
#: Job D1p5_A225: Abaqus/Standard completed successfully.
#: Job D1p5_A225 completed successfully. 
#:   Job D1p5_A225 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=5.74652e-02 N  max_disp=7.4254e-01 m  tip U=(1.794e-01, -5.670e-16, -7.206e-01) m
#:   A_proj=6.23583  A_drag=4.29564 m^2  scallop=1.596e-01 m  t=18.0s
#: 
#: --- Run 009/036 d=1.5 mm alt=200 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A200: Analysis Input File Processor completed successfully.
#: Job D1p5_A200: Abaqus/Standard completed successfully.
#: Job D1p5_A200 completed successfully. 
#:   Job D1p5_A200 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=8.14039e-02 N  max_disp=9.5927e-01 m  tip U=(2.987e-01, -6.739e-16, -9.116e-01) m
#:   A_proj=4.35358  A_drag=2.50817 m^2  scallop=3.109e-01 m  t=18.0s
#: Saved: sail_outline_d1p5mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 010/036 d=2 mm alt=400 km ---
#: Job D2_A400: Analysis Input File Processor completed successfully.
#: Job D2_A400: Abaqus/Standard completed successfully.
#: Job D2_A400 completed successfully. 
#:   Job D2_A400 (analysis) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=7.5654e-03 m  tip U=(1.866e-05, -5.176e-18, -7.565e-03) m
#:   A_proj=8.99971  A_drag=8.99933 m^2  scallop=1.446e-05 m  t=17.9s
#: 
#: --- Run 011/036 d=2 mm alt=375 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A375: Analysis Input File Processor completed successfully.
#: Job D2_A375: Abaqus/Standard completed successfully.
#: Job D2_A375 completed successfully. 
#:   Job D2_A375 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.81579e-03 N  max_disp=1.3054e-02 m  tip U=(5.557e-05, -9.234e-18, -1.305e-02) m
#:   A_proj=8.99913  A_drag=8.99801 m^2  scallop=4.294e-05 m  t=18.0s
#: 
#: --- Run 012/036 d=2 mm alt=350 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A350: Analysis Input File Processor completed successfully.
#: Job D2_A350: Abaqus/Standard completed successfully.
#: Job D2_A350 completed successfully. 
#:   Job D2_A350 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=4.11315e-03 N  max_disp=1.9068e-02 m  tip U=(1.186e-04, -1.340e-17, -1.907e-02) m
#:   A_proj=8.99814  A_drag=8.99574 m^2  scallop=9.167e-05 m  t=18.0s
#: 
#: --- Run 013/036 d=2 mm alt=325 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A325: Analysis Input File Processor completed successfully.
#: Job D2_A325: Abaqus/Standard completed successfully.
#: Job D2_A325 completed successfully. 
#:   Job D2_A325 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=6.86243e-03 N  max_disp=3.1808e-02 m  tip U=(3.299e-04, -2.239e-17, -3.181e-02) m
#:   A_proj=8.99481  A_drag=8.98816 m^2  scallop=2.551e-04 m  t=18.0s
#: 
#: --- Run 014/036 d=2 mm alt=300 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A300: Analysis Input File Processor completed successfully.
#: Job D2_A300: Abaqus/Standard completed successfully.
#: Job D2_A300 completed successfully. 
#:   Job D2_A300 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.13071e-02 N  max_disp=5.2390e-02 m  tip U=(8.951e-04, -3.634e-17, -5.238e-02) m
#:   A_proj=8.98593  A_drag=8.96792 m^2  scallop=6.922e-04 m  t=18.0s
#: 
#: --- Run 015/036 d=2 mm alt=275 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A275: Analysis Input File Processor completed successfully.
#: Job D2_A275: Abaqus/Standard completed successfully.
#: Job D2_A275 completed successfully. 
#:   Job D2_A275 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.30564e-02 N  max_disp=1.0663e-01 m  tip U=(3.708e-03, -7.414e-17, -1.066e-01) m
#:   A_proj=8.94176  A_drag=8.86779 m^2  scallop=2.872e-03 m  t=18.0s
#: 
#: --- Run 016/036 d=2 mm alt=250 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A250: Analysis Input File Processor completed successfully.
#: Job D2_A250: Abaqus/Standard completed successfully.
#: Job D2_A250 completed successfully. 
#:   Job D2_A250 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=4.44547e-02 N  max_disp=2.0424e-01 m  tip U=(1.360e-02, -1.464e-16, -2.038e-01) m
#:   A_proj=8.78667  A_drag=8.52369 m^2  scallop=1.060e-02 m  t=18.0s
#: 
#: --- Run 017/036 d=2 mm alt=225 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A225: Analysis Input File Processor completed successfully.
#: Job D2_A225: Abaqus/Standard completed successfully.
#: Job D2_A225 completed successfully. 
#:   Job D2_A225 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=8.01740e-02 N  max_disp=3.6124e-01 m  tip U=(4.253e-02, -2.638e-16, -3.587e-01) m
#:   A_proj=8.33573  A_drag=7.58652 m^2  scallop=3.380e-02 m  t=18.1s
#: 
#: --- Run 018/036 d=2 mm alt=200 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A200: Analysis Input File Processor completed successfully.
#: Job D2_A200: Abaqus/Standard completed successfully.
#: Job D2_A200 completed successfully. 
#:   Job D2_A200 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.43767e-01 N  max_disp=6.1274e-01 m  tip U=(1.222e-01, -4.536e-16, -6.004e-01) m
#:   A_proj=7.10886  A_drag=5.46917 m^2  scallop=1.032e-01 m  t=18.1s
#: Saved: sail_outline_d2mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 019/036 d=2.5 mm alt=400 km ---
#: Job D2p5_A400: Analysis Input File Processor completed successfully.
#: Job D2p5_A400: Abaqus/Standard completed successfully.
#: Job D2p5_A400 completed successfully. 
#:   Job D2p5_A400 (analysis) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=3.0988e-03 m  tip U=(3.131e-06, -2.142e-18, -3.099e-03) m
#:   A_proj=8.99995  A_drag=8.99989 m^2  scallop=2.419e-06 m  t=18.0s
#: 
#: --- Run 020/036 d=2.5 mm alt=375 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A375: Analysis Input File Processor completed successfully.
#: Job D2p5_A375: Abaqus/Standard completed successfully.
#: Job D2p5_A375 completed successfully. 
#:   Job D2p5_A375 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.81597e-03 N  max_disp=5.3474e-03 m  tip U=(9.325e-06, -3.640e-18, -5.347e-03) m
#:   A_proj=8.99985  A_drag=8.99967 m^2  scallop=7.191e-06 m  t=18.1s
#: 
#: --- Run 021/036 d=2.5 mm alt=350 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A350: Analysis Input File Processor completed successfully.
#: Job D2p5_A350: Abaqus/Standard completed successfully.
#: Job D2p5_A350 completed successfully. 
#:   Job D2p5_A350 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=4.11391e-03 N  max_disp=7.8121e-03 m  tip U=(1.990e-05, -5.375e-18, -7.812e-03) m
#:   A_proj=8.99969  A_drag=8.99929 m^2  scallop=1.540e-05 m  t=18.0s
#: 
#: --- Run 022/036 d=2.5 mm alt=325 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A325: Analysis Input File Processor completed successfully.
#: Job D2p5_A325: Abaqus/Standard completed successfully.
#: Job D2p5_A325 completed successfully. 
#:   Job D2p5_A325 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=6.86513e-03 N  max_disp=1.3036e-02 m  tip U=(5.542e-05, -9.015e-18, -1.304e-02) m
#:   A_proj=8.99913  A_drag=8.99801 m^2  scallop=4.285e-05 m  t=18.0s
#: 
#: --- Run 023/036 d=2.5 mm alt=300 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A300: Analysis Input File Processor completed successfully.
#: Job D2p5_A300: Abaqus/Standard completed successfully.
#: Job D2p5_A300 completed successfully. 
#:   Job D2p5_A300 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.13195e-02 N  max_disp=2.1493e-02 m  tip U=(1.506e-04, -1.468e-17, -2.149e-02) m
#:   A_proj=8.99763  A_drag=8.99459 m^2  scallop=1.165e-04 m  t=18.0s
#: 
#: --- Run 024/036 d=2.5 mm alt=275 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A275: Analysis Input File Processor completed successfully.
#: Job D2p5_A275: Abaqus/Standard completed successfully.
#: Job D2p5_A275 completed successfully. 
#:   Job D2p5_A275 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.31250e-02 N  max_disp=4.3895e-02 m  tip U=(6.283e-04, -3.038e-17, -4.389e-02) m
#:   A_proj=8.99012  A_drag=8.97747 m^2  scallop=4.858e-04 m  t=18.0s
#: 
#: --- Run 025/036 d=2.5 mm alt=250 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A250: Analysis Input File Processor completed successfully.
#: Job D2p5_A250: Abaqus/Standard completed successfully.
#: Job D2p5_A250 completed successfully. 
#:   Job D2p5_A250 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=4.50046e-02 N  max_disp=8.5328e-02 m  tip U=(2.374e-03, -5.971e-17, -8.529e-02) m
#:   A_proj=8.96270  A_drag=8.91513 m^2  scallop=1.838e-03 m  t=18.0s
#: 
#: --- Run 026/036 d=2.5 mm alt=225 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A225: Analysis Input File Processor completed successfully.
#: Job D2p5_A225: Abaqus/Standard completed successfully.
#: Job D2p5_A225 completed successfully. 
#:   Job D2p5_A225 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=8.38560e-02 N  max_disp=1.5838e-01 m  tip U=(8.179e-03, -1.138e-16, -1.582e-01) m
#:   A_proj=8.87161  A_drag=8.71072 m^2  scallop=6.354e-03 m  t=18.0s
#: 
#: --- Run 027/036 d=2.5 mm alt=200 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A200: Analysis Input File Processor completed successfully.
#: Job D2p5_A200: Abaqus/Standard completed successfully.
#: Job D2p5_A200 completed successfully. 
#:   Job D2p5_A200 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.65071e-01 N  max_disp=3.0709e-01 m  tip U=(3.074e-02, -2.219e-16, -3.055e-01) m
#:   A_proj=8.51907  A_drag=7.95643 m^2  scallop=2.424e-02 m  t=18.0s
#: Saved: sail_outline_d2p5mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 028/036 d=3 mm alt=400 km ---
#: Job D3_A400: Analysis Input File Processor completed successfully.
#: Job D3_A400: Abaqus/Standard completed successfully.
#: Job D3_A400 completed successfully. 
#:   Job D3_A400 (analysis) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.63184e-03 N  max_disp=1.4944e-03 m  tip U=(7.283e-07, -1.079e-18, -1.494e-03) m
#:   A_proj=8.99999  A_drag=8.99997 m^2  scallop=5.980e-07 m  t=17.9s
#: 
#: --- Run 029/036 d=3 mm alt=375 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A375: Analysis Input File Processor completed successfully.
#: Job D3_A375: Abaqus/Standard completed successfully.
#: Job D3_A375 completed successfully. 
#:   Job D3_A375 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.81599e-03 N  max_disp=2.5788e-03 m  tip U=(2.169e-06, -1.853e-18, -2.579e-03) m
#:   A_proj=8.99997  A_drag=8.99992 m^2  scallop=1.677e-06 m  t=18.0s
#: 
#: --- Run 030/036 d=3 mm alt=350 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A350: Analysis Input File Processor completed successfully.
#: Job D3_A350: Abaqus/Standard completed successfully.
#: Job D3_A350 completed successfully. 
#:   Job D3_A350 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=4.11403e-03 N  max_disp=3.7675e-03 m  tip U=(4.629e-06, -2.698e-18, -3.768e-03) m
#:   A_proj=8.99993  A_drag=8.99983 m^2  scallop=3.603e-06 m  t=18.0s
#: 
#: --- Run 031/036 d=3 mm alt=325 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A350.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A325: Analysis Input File Processor completed successfully.
#: Job D3_A325: Abaqus/Standard completed successfully.
#: Job D3_A325 completed successfully. 
#:   Job D3_A325 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=6.86555e-03 N  max_disp=6.2873e-03 m  tip U=(1.289e-05, -4.522e-18, -6.287e-03) m
#:   A_proj=8.99980  A_drag=8.99954 m^2  scallop=9.952e-06 m  t=18.0s
#: 
#: --- Run 032/036 d=3 mm alt=300 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A325.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A300: Analysis Input File Processor completed successfully.
#: Job D3_A300: Abaqus/Standard completed successfully.
#: Job D3_A300 completed successfully. 
#:   Job D3_A300 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.13214e-02 N  max_disp=1.0368e-02 m  tip U=(3.505e-05, -7.540e-18, -1.037e-02) m
#:   A_proj=8.99945  A_drag=8.99874 m^2  scallop=2.709e-05 m  t=18.0s
#: 
#: --- Run 033/036 d=3 mm alt=275 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A300.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A275: Analysis Input File Processor completed successfully.
#: Job D3_A275: Abaqus/Standard completed successfully.
#: Job D3_A275 completed successfully. 
#:   Job D3_A275 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.31357e-02 N  max_disp=2.1185e-02 m  tip U=(1.464e-04, -1.499e-17, -2.118e-02) m
#:   A_proj=8.99770  A_drag=8.99475 m^2  scallop=1.132e-04 m  t=18.0s
#: 
#: --- Run 034/036 d=3 mm alt=250 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A275.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A250: Analysis Input File Processor completed successfully.
#: Job D3_A250: Abaqus/Standard completed successfully.
#: Job D3_A250 completed successfully. 
#:   Job D3_A250 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=4.50912e-02 N  max_disp=4.1279e-02 m  tip U=(5.557e-04, -3.024e-17, -4.127e-02) m
#:   A_proj=8.99127  A_drag=8.98007 m^2  scallop=4.296e-04 m  t=18.0s
#: 
#: --- Run 035/036 d=3 mm alt=225 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A250.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A225: Analysis Input File Processor completed successfully.
#: Job D3_A225: Abaqus/Standard completed successfully.
#: Job D3_A225 completed successfully. 
#:   Job D3_A225 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=8.44668e-02 N  max_disp=7.7254e-02 m  tip U=(1.946e-03, -5.590e-17, -7.723e-02) m
#:   A_proj=8.96942  A_drag=8.93038 m^2  scallop=1.506e-03 m  t=18.0s
#: 
#: --- Run 036/036 d=3 mm alt=200 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A200: Analysis Input File Processor completed successfully.
#: Job D3_A200: Abaqus/Standard completed successfully.
#: Job D3_A200 completed successfully. 
#:   Job D3_A200 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.69234e-01 N  max_disp=1.5419e-01 m  tip U=(7.752e-03, -1.142e-16, -1.540e-01) m
#:   A_proj=8.87831  A_drag=8.72562 m^2  scallop=6.021e-03 m  t=18.1s
#: Saved: sail_outline_d3mm.png
#: 
#: All 36 runs complete. Total time: 650.7 s
#: Results saved to: factorial_results_2.0.csv
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb'])
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A225.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A225.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-200', frame=29)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.41672, 
    farPlane=3.86661, width=2.29317, height=0.87208, viewOffsetX=0.0618903, 
    viewOffsetY=0.0356915)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.40556, 
    farPlane=3.87777, width=2.28568, height=0.869232, viewOffsetX=0.012378, 
    viewOffsetY=0.00804926)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A400.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/D3_A400.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-200', frame=29)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb'])
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A400.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D3_A375.odb')
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/adzheng/Solar-Sail-FEA/D3_A375.odb'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-375', frame=29)
o1 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D1p5_A400.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A400.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-400', frame=29)
o1 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D1p5_A375.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A375.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-375', frame=29)
o1 = session.openOdb(name='C:/Users/adzheng/Solar-Sail-FEA/D1p5_A200.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
