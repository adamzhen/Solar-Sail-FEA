# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2025 replay file
# Internal Version: 2024_09_20-08.00.46 RELr427 198590
# Run by adzheng on Tue Oct 20 20:53:53 2026
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
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].view.setValues(width=2.59535, height=0.987, 
    viewOffsetX=-0.0380515, viewOffsetY=-0.02709)
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
session.viewports['Viewport: 1'].view.setValues(width=2.03116, height=0.772441, 
    viewOffsetX=0.0427627, viewOffsetY=0.00540709)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.30448, 
    farPlane=3.95545, width=3.45653, height=1.3145, viewOffsetX=-0.0699016, 
    viewOffsetY=-0.0436658)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.28871, 
    farPlane=3.97122, width=3.44003, height=1.30823, viewOffsetX=0.0744945, 
    viewOffsetY=-0.11323)
session.viewports['Viewport: 1'].view.setValues(width=3.65943, height=1.39166, 
    viewOffsetX=0.0633453, viewOffsetY=-0.127976)
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.30448, 
    farPlane=3.95545, width=3.45653, height=1.3145, viewOffsetX=-0.0689687, 
    viewOffsetY=-0.0397448)
execfile('C:/Users/adzheng/Solar-Sail-FEA/polygon_sail_study_v2.py', 
    __main__.__dict__)
#: Study: 44 runs (4 diameters x 11 altitudes)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 001/044 d=1.5 mm alt=400 km ---
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
#:   A_proj=8.99707  A_drag=8.99331 m^2  scallop=1.441e-04 m  t=16.2s
#: 
#: --- Run 002/044 d=1.5 mm alt=375 km ---
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
#:   A_proj=8.99129  A_drag=8.98013 m^2  scallop=4.283e-04 m  t=18.1s
#: 
#: --- Run 003/044 d=1.5 mm alt=350 km ---
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
#:   A_proj=8.98149  A_drag=8.95780 m^2  scallop=9.111e-04 m  t=16.1s
#: 
#: --- Run 004/044 d=1.5 mm alt=325 km ---
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
#:   A_proj=8.94886  A_drag=8.88383 m^2  scallop=2.521e-03 m  t=16.1s
#: 
#: --- Run 005/044 d=1.5 mm alt=300 km ---
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
#:   A_proj=8.86432  A_drag=8.69454 m^2  scallop=6.717e-03 m  t=16.1s
#: 
#: --- Run 006/044 d=1.5 mm alt=275 km ---
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
#:   A_proj=8.47706  A_drag=7.87034 m^2  scallop=2.641e-02 m  t=16.1s
#: 
#: --- Run 007/044 d=1.5 mm alt=250 km ---
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
#:   A_proj=7.51770  A_drag=6.10940 m^2  scallop=7.895e-02 m  t=16.1s
#: 
#: --- Run 008/044 d=1.5 mm alt=225 km ---
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
#:   A_proj=6.23583  A_drag=4.29564 m^2  scallop=1.596e-01 m  t=16.1s
#: 
#: --- Run 009/044 d=1.5 mm alt=200 km ---
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
#:   A_proj=4.35358  A_drag=2.50817 m^2  scallop=3.109e-01 m  t=18.1s
#: 
#: --- Run 010/044 d=1.5 mm alt=175 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A175: Analysis Input File Processor completed successfully.
#: Job D1p5_A175: Abaqus/Standard completed successfully.
#: Job D1p5_A175 completed successfully. 
#:   Job D1p5_A175 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.08629e-01 N  max_disp=1.1485e+00 m  tip U=(4.271e-01, -6.926e-16, -1.066e+00) m
#:   A_proj=1.76806  A_drag=1.18440 m^2  scallop=6.209e-01 m  t=18.1s
#: 
#: --- Run 011/044 d=1.5 mm alt=150 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D1p5_A150: Analysis Input File Processor completed successfully.
#: Job D1p5_A150: Abaqus/Standard completed successfully.
#: Job D1p5_A150 completed successfully. 
#:   Job D1p5_A150 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D1p5_A150.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=1.51470e-01 N  max_disp=1.3613e+00 m  tip U=(5.973e-01, -6.653e-16, -1.223e+00) m
#:   A_proj=0.83038  A_drag=0.71594 m^2  scallop=6.508e-01 m  t=18.0s
#: Saved: sail_outline_d1p5mm.png
#: Saved: wire_profile_d1p5mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 012/044 d=2 mm alt=400 km ---
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
#:   A_proj=8.99971  A_drag=8.99933 m^2  scallop=1.446e-05 m  t=16.0s
#: 
#: --- Run 013/044 d=2 mm alt=375 km ---
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
#:   A_proj=8.99913  A_drag=8.99801 m^2  scallop=4.294e-05 m  t=18.2s
#: 
#: --- Run 014/044 d=2 mm alt=350 km ---
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
#:   A_proj=8.99814  A_drag=8.99574 m^2  scallop=9.167e-05 m  t=18.1s
#: 
#: --- Run 015/044 d=2 mm alt=325 km ---
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
#:   A_proj=8.99481  A_drag=8.98816 m^2  scallop=2.551e-04 m  t=18.1s
#: 
#: --- Run 016/044 d=2 mm alt=300 km ---
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
#: --- Run 017/044 d=2 mm alt=275 km ---
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
#: --- Run 018/044 d=2 mm alt=250 km ---
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
#:   A_proj=8.78667  A_drag=8.52369 m^2  scallop=1.060e-02 m  t=16.0s
#: 
#: --- Run 019/044 d=2 mm alt=225 km ---
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
#:   A_proj=8.33573  A_drag=7.58652 m^2  scallop=3.380e-02 m  t=16.1s
#: 
#: --- Run 020/044 d=2 mm alt=200 km ---
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
#:   A_proj=7.10886  A_drag=5.46917 m^2  scallop=1.032e-01 m  t=16.0s
#: 
#: --- Run 021/044 d=2 mm alt=175 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A175: Analysis Input File Processor completed successfully.
#: Job D2_A175: Abaqus/Standard completed successfully.
#: Job D2_A175 completed successfully. 
#:   Job D2_A175 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=2.36871e-01 N  max_disp=9.0605e-01 m  tip U=(2.666e-01, -6.067e-16, -8.659e-01) m
#:   A_proj=4.87796  A_drag=2.91772 m^2  scallop=2.636e-01 m  t=18.1s
#: 
#: --- Run 022/044 d=2 mm alt=150 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2_A150: Analysis Input File Processor completed successfully.
#: Job D2_A150: Abaqus/Standard completed successfully.
#: Job D2_A150 completed successfully. 
#:   Job D2_A150 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2_A150.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=3.73139e-01 N  max_disp=1.2029e+00 m  tip U=(4.681e-01, -6.834e-16, -1.108e+00) m
#:   A_proj=1.39590  A_drag=1.01237 m^2  scallop=6.519e-01 m  t=18.1s
#: Saved: sail_outline_d2mm.png
#: Saved: wire_profile_d2mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 023/044 d=2.5 mm alt=400 km ---
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
#:   A_proj=8.99995  A_drag=8.99989 m^2  scallop=2.419e-06 m  t=16.0s
#: 
#: --- Run 024/044 d=2.5 mm alt=375 km ---
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
#:   A_proj=8.99985  A_drag=8.99967 m^2  scallop=7.191e-06 m  t=18.0s
#: 
#: --- Run 025/044 d=2.5 mm alt=350 km ---
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
#:   A_proj=8.99969  A_drag=8.99929 m^2  scallop=1.540e-05 m  t=16.1s
#: 
#: --- Run 026/044 d=2.5 mm alt=325 km ---
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
#:   A_proj=8.99913  A_drag=8.99801 m^2  scallop=4.285e-05 m  t=16.1s
#: 
#: --- Run 027/044 d=2.5 mm alt=300 km ---
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
#:   A_proj=8.99763  A_drag=8.99459 m^2  scallop=1.165e-04 m  t=16.1s
#: 
#: --- Run 028/044 d=2.5 mm alt=275 km ---
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
#:   A_proj=8.99012  A_drag=8.97747 m^2  scallop=4.858e-04 m  t=16.1s
#: 
#: --- Run 029/044 d=2.5 mm alt=250 km ---
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
#:   A_proj=8.96270  A_drag=8.91513 m^2  scallop=1.838e-03 m  t=16.0s
#: 
#: --- Run 030/044 d=2.5 mm alt=225 km ---
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
#:   A_proj=8.87161  A_drag=8.71072 m^2  scallop=6.354e-03 m  t=16.1s
#: 
#: --- Run 031/044 d=2.5 mm alt=200 km ---
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
#:   A_proj=8.51907  A_drag=7.95643 m^2  scallop=2.424e-02 m  t=16.0s
#: 
#: --- Run 032/044 d=2.5 mm alt=175 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A175: Analysis Input File Processor completed successfully.
#: Job D2p5_A175: Abaqus/Standard completed successfully.
#: Job D2p5_A175 completed successfully. 
#:   Job D2p5_A175 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=3.44595e-01 N  max_disp=6.0323e-01 m  tip U=(1.185e-01, -4.524e-16, -5.915e-01) m
#:   A_proj=7.16633  A_drag=5.55549 m^2  scallop=9.973e-02 m  t=18.1s
#: 
#: --- Run 033/044 d=2.5 mm alt=150 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D2p5_A150: Analysis Input File Processor completed successfully.
#: Job D2p5_A150: Abaqus/Standard completed successfully.
#: Job D2p5_A150 completed successfully. 
#:   Job D2p5_A150 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D2p5_A150.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=7.10476e-01 N  max_disp=1.0398e+00 m  tip U=(3.506e-01, -6.604e-16, -9.789e-01) m
#:   A_proj=3.41470  A_drag=1.91756 m^2  scallop=4.095e-01 m  t=18.1s
#: Saved: sail_outline_d2p5mm.png
#: Saved: wire_profile_d2p5mm.png
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- Run 034/044 d=3 mm alt=400 km ---
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
#:   A_proj=8.99999  A_drag=8.99997 m^2  scallop=5.980e-07 m  t=18.0s
#: 
#: --- Run 035/044 d=3 mm alt=375 km ---
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
#:   A_proj=8.99997  A_drag=8.99992 m^2  scallop=1.677e-06 m  t=17.1s
#: 
#: --- Run 036/044 d=3 mm alt=350 km ---
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
#:   A_proj=8.99993  A_drag=8.99983 m^2  scallop=3.603e-06 m  t=16.0s
#: 
#: --- Run 037/044 d=3 mm alt=325 km ---
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
#:   A_proj=8.99980  A_drag=8.99954 m^2  scallop=9.952e-06 m  t=16.0s
#: 
#: --- Run 038/044 d=3 mm alt=300 km ---
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
#: --- Run 039/044 d=3 mm alt=275 km ---
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
#:   A_proj=8.99770  A_drag=8.99475 m^2  scallop=1.132e-04 m  t=16.0s
#: 
#: --- Run 040/044 d=3 mm alt=250 km ---
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
#:   A_proj=8.99127  A_drag=8.98007 m^2  scallop=4.296e-04 m  t=16.1s
#: 
#: --- Run 041/044 d=3 mm alt=225 km ---
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
#:   A_proj=8.96942  A_drag=8.93038 m^2  scallop=1.506e-03 m  t=16.1s
#: 
#: --- Run 042/044 d=3 mm alt=200 km ---
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
#:   A_proj=8.87831  A_drag=8.72562 m^2  scallop=6.021e-03 m  t=18.0s
#: 
#: --- Run 043/044 d=3 mm alt=175 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A175: Analysis Input File Processor completed successfully.
#: Job D3_A175: Abaqus/Standard completed successfully.
#: Job D3_A175 completed successfully. 
#:   Job D3_A175 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=3.77908e-01 N  max_disp=3.3758e-01 m  tip U=(3.715e-02, -2.575e-16, -3.355e-01) m
#:   A_proj=8.41941  A_drag=7.75351 m^2  scallop=2.941e-02 m  t=18.1s
#: 
#: --- Run 044/044 d=3 mm alt=150 km ---
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A175.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#: Job D3_A150: Analysis Input File Processor completed successfully.
#: Job D3_A150: Abaqus/Standard completed successfully.
#: Job D3_A150 completed successfully. 
#:   Job D3_A150 (restart) completed.
#: Model: C:/Users/adzheng/Solar-Sail-FEA/D3_A150.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   F=9.91574e-01 N  max_disp=7.8765e-01 m  tip U=(2.017e-01, -6.061e-16, -7.614e-01) m
#:   A_proj=5.89249  A_drag=3.89964 m^2  scallop=1.838e-01 m  t=16.2s
#: Saved: sail_outline_d3mm.png
#: Saved: wire_profile_d3mm.png
#: 
#: All 44 runs complete. Total time: 747.3 s
#: Results saved to: factorial_results_2.0.csv
execfile('C:/Users/adzheng/Solar-Sail-FEA/mesh_convergence_study.py', 
    __main__.__dict__)
#: Mesh convergence: d=1.5 mm, alt=200 km
#: p=1.89504e-02 N/m^2, A_LOAD=4.2956 m^2, F=8.14031e-02 N, w_scale=6.48033e-03 N/m^2
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#: --- 3 elements (h = 0.5907 m) ---
#: The model "Mesh_3" has been created.
#: Job MeshConv_d1p5_A200_n3: Analysis Input File Processor completed successfully.
#: Job MeshConv_d1p5_A200_n3: Abaqus/Standard completed successfully.
#: Job MeshConv_d1p5_A200_n3 completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/MeshConv_d1p5_A200_n3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   tip U1=2.87801e-01  U3=-9.04428e-01  max|U|=9.49115e-01  S11max=2.2599e+07  A_drag=2.62418  t=18.1s
#: 
#: --- 6 elements (h = 0.2954 m) ---
#: The model "Mesh_6" has been created.
#: Job MeshConv_d1p5_A200_n6: Analysis Input File Processor completed successfully.
#: Job MeshConv_d1p5_A200_n6: Abaqus/Standard completed successfully.
#: Job MeshConv_d1p5_A200_n6 completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/MeshConv_d1p5_A200_n6.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   tip U1=2.96072e-01  U3=-9.09774e-01  max|U|=9.56738e-01  S11max=2.6892e+07  A_drag=2.53503  t=18.1s
#: 
#: --- 12 elements (h = 0.1477 m) ---
#: The model "Mesh_12" has been created.
#: Job MeshConv_d1p5_A200_n12: Analysis Input File Processor completed successfully.
#: Job MeshConv_d1p5_A200_n12: Abaqus/Standard completed successfully.
#: Job MeshConv_d1p5_A200_n12 completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/MeshConv_d1p5_A200_n12.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   tip U1=2.98281e-01  U3=-9.11261e-01  max|U|=9.58837e-01  S11max=2.9168e+07  A_drag=2.51228  t=18.1s
#: 
#: --- 24 elements (h = 0.0738 m) ---
#: The model "Mesh_24" has been created.
#: Job MeshConv_d1p5_A200_n24: Analysis Input File Processor completed successfully.
#: Job MeshConv_d1p5_A200_n24: Abaqus/Standard completed successfully.
#: Job MeshConv_d1p5_A200_n24 completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/MeshConv_d1p5_A200_n24.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   tip U1=2.98843e-01  U3=-9.11643e-01  max|U|=9.59375e-01  S11max=3.0315e+07  A_drag=2.50724  t=18.1s
#: 
#: --- 48 elements (h = 0.0369 m) ---
#: The model "Mesh_48" has been created.
#: Job MeshConv_d1p5_A200_n48: Analysis Input File Processor completed successfully.
#: Job MeshConv_d1p5_A200_n48: Abaqus/Standard completed successfully.
#: Job MeshConv_d1p5_A200_n48 completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/MeshConv_d1p5_A200_n48.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   tip U1=2.98983e-01  U3=-9.11739e-01  max|U|=9.59509e-01  S11max=3.0887e+07  A_drag=2.50643  t=18.1s
#: 
#: --- 96 elements (h = 0.0185 m) ---
#: The model "Mesh_96" has been created.
#: Job MeshConv_d1p5_A200_n96: Analysis Input File Processor completed successfully.
#: Job MeshConv_d1p5_A200_n96: Abaqus/Standard completed successfully.
#: Job MeshConv_d1p5_A200_n96 completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/MeshConv_d1p5_A200_n96.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   tip U1=2.99019e-01  U3=-9.11763e-01  max|U|=9.59543e-01  S11max=3.1172e+07  A_drag=2.50646  t=18.1s
#: 
#: --- 192 elements (h = 0.0092 m) ---
#: The model "Mesh_192" has been created.
#: Job MeshConv_d1p5_A200_n192: Analysis Input File Processor completed successfully.
#: Job MeshConv_d1p5_A200_n192: Abaqus/Standard completed successfully.
#: Job MeshConv_d1p5_A200_n192 completed successfully. 
#: Model: C:/Users/adzheng/Solar-Sail-FEA/MeshConv_d1p5_A200_n192.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
#:   tip U1=2.99027e-01  U3=-9.11769e-01  max|U|=9.59552e-01  S11max=3.1314e+07  A_drag=2.50659  t=18.2s
#: 
#: === Mesh convergence summary (d1p5mm_200km) ===
#: U1_tip (m)               order p=1.994  extrapolated=2.990303e-01  GCI_fine=1.240e-05
#: U3_tip (m)               order p=1.986  extrapolated=-9.117708e-01  GCI_fine=2.815e-06
#: max_deformation (m)      order p=1.990  extrapolated=9.595546e-01  GCI_fine=3.736e-06
#: max_stress_S11 (Pa)      order p=1.003  extrapolated=3.145543e+07  GCI_fine=5.645e-03
#: A_drag (m^2)             order p=-1.985  extrapolated=2.506422e+00  GCI_fine=-8.415e-05
#: Converged (<1.0% change on all metrics) at 48 elements
#: Saved: mesh_convergence_d1p5mm_200km.csv
#: Total time: 129.0 s
