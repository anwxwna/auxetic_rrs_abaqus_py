# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-50.0, 35.0),
    point2=(55.0, -50.0))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-50.0, -50.0),
    point2=(55.0, 35.0))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=20.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].features['Solid extrude-1'].setValues(
    depth=10.0)
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1',
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#4 ]', ), ), name='Set-1')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial',
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-1',
    region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=SET, u2=SET,
    u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-1'].features['Solid extrude-1']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-25.0, -15.0),
    point2=(30.0, 15.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-2', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-2'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-1']
mdb.models['Model-1'].parts['Part-2'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
del mdb.models['Model-1'].parts['Part-2'].features['Shell planar-1']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(20.0, 20.0),
    point2=(-20.0, -20.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='hinge', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['hinge'].BaseSolidExtrude(depth=40.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-2']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=3.46, name='__profile__',
    sheetSize=138.56, transform=
    mdb.models['Model-1'].parts['hinge'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['hinge'].faces[4],
    sketchPlaneSide=SIDE1,
    sketchUpEdge=mdb.models['Model-1'].parts['hinge'].edges[0],
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 40.0)))
mdb.models['Model-1'].parts['hinge'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(40.0, 20.0), point2=
    (20.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 20.0), point2=
    (20.0, -20.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, -20.0),
    point2=(40.0, -20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(40.0,
    0.0), direction=CLOCKWISE, point1=(40.0, 20.0), point2=(40.0, -20.0))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    40.0, 0.0), point1=(50.0, 0.0))
mdb.models['Model-1'].parts['hinge'].SolidExtrude(depth=20.0,
    flipExtrudeDirection=ON, sketch=
    mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT,
    sketchPlane=mdb.models['Model-1'].parts['hinge'].faces[4], sketchPlaneSide=
    SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['hinge'].edges[0])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['hinge'].PartitionCellByExtendFace(cells=
    mdb.models['Model-1'].parts['hinge'].cells.getSequenceFromMask(('[#1 ]', ),
    ), extendFace=mdb.models['Model-1'].parts['hinge'].faces[3])
mdb.models['Model-1'].parts['hinge'].PartitionCellByPlanePointNormal(cells=
    mdb.models['Model-1'].parts['hinge'].cells.getSequenceFromMask(('[#1 ]', ),
    ), normal=mdb.models['Model-1'].parts['hinge'].edges[20], point=
    mdb.models['Model-1'].parts['hinge'].vertices[5])
mdb.models['Model-1'].parts['hinge'].PartitionCellByPlanePointNormal(cells=
    mdb.models['Model-1'].parts['hinge'].cells.getSequenceFromMask(('[#2 ]', ),
    ), normal=mdb.models['Model-1'].parts['hinge'].edges[21], point=
    mdb.models['Model-1'].parts['hinge'].InterestingPoint(
    mdb.models['Model-1'].parts['hinge'].edges[15], MIDDLE))
#* Feature creation failed.
mdb.models['Model-1'].parts['hinge'].PartitionCellByPlanePointNormal(cells=
    mdb.models['Model-1'].parts['hinge'].cells.getSequenceFromMask(('[#2 ]', ),
    ), normal=mdb.models['Model-1'].parts['hinge'].edges[16], point=
    mdb.models['Model-1'].parts['hinge'].InterestingPoint(
    mdb.models['Model-1'].parts['hinge'].edges[15], MIDDLE))
mdb.models['Model-1'].parts['hinge'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF,
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD),
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['hinge'].cells.getSequenceFromMask(('[#f ]', ),
    ), ))
mdb.models['Model-1'].parts['hinge'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=4.0)
mdb.models['Model-1'].parts['hinge'].generateMesh()
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((209000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Steel', name=
    'SolidSection', thickness=1.0)
mdb.models['Model-1'].parts['hinge'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['hinge'].cells.getSequenceFromMask(mask=(
    '[#f ]', ), )), sectionName='SolidSection', thicknessAssignment=
    FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
#* FeatureError: Regeneration failed
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='hinge-1', part=
    mdb.models['Model-1'].parts['hinge'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='hinge-2', part=
    mdb.models['Model-1'].parts['hinge'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='hinge-3', part=
    mdb.models['Model-1'].parts['hinge'])
del mdb.models['Model-1'].rootAssembly.features['hinge-2']
del mdb.models['Model-1'].rootAssembly.features['hinge-3']
del mdb.models['Model-1'].rootAssembly.features['Part-1-1']
mdb.models['Model-1'].StaticStep(name='Load', previous='Initial')
mdb.models['Model-1'].StaticStep(name='Load-2', previous='Load')
mdb.models['Model-1'].rootAssembly.Set(name='Monitor', vertices=
    mdb.models['Model-1'].rootAssembly.instances['hinge-1'].vertices.getSequenceFromMask(
    ('[#10000 ]', ), ))
mdb.models['Model-1'].steps['Load'].Monitor(dof=1, frequency=1, node=Region(
    vertices=mdb.models['Model-1'].rootAssembly.instances['hinge-1'].vertices.getSequenceFromMask(
    mask=('[#10000 ]', ), )))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial',
    distributionType=UNIFORM, fieldName='', localCsys=None, name='Fixed',
    region=Region(
    faces=mdb.models['Model-1'].rootAssembly.instances['hinge-1'].faces.getSequenceFromMask(
    mask=('[#80000 ]', ), )), u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET,
    ur3=UNSET)
del mdb.models['Model-1'].boundaryConditions['BC-1']
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Load',
    distributionType=UNIFORM, field='', magnitude=-1.0, name='Pressure',
    region=Region(
    side1Faces=mdb.models['Model-1'].rootAssembly.instances['hinge-1'].faces.getSequenceFromMask(
    mask=('[#200a10 ]', ), )))
mdb.models['Model-1'].ConcentratedForce(cf1=10000.0, createStepName='Load',
    distributionType=UNIFORM, field='', localCsys=None, name='Load', region=
    Region(
    vertices=mdb.models['Model-1'].rootAssembly.instances['hinge-1'].vertices.getSequenceFromMask(
    mask=('[#4 ]', ), )))
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
    multiprocessingMode=DEFAULT, name='PullHinge', nodalOutputPrecision=SINGLE,
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['PullHinge'].submit(consistencyChecking=OFF)
mdb.jobs['PullHinge']._Message(STARTED, {'phase': BATCHPRE_PHASE,
    'clientHost': 'Anw', 'handle': 0, 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
    'file': 'E:\\Temp\\PullHinge.odb', 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(STARTED, {'phase': STANDARD_PHASE,
    'clientHost': 'Anw', 'handle': 8468, 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 0, 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0,
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1,
    'jobName': 'PullHinge', 'severe': 0, 'iterations': 0,
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['PullHinge']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'PullHinge', 'memory': 43.0})
mdb.jobs['PullHinge']._Message(MONITOR_DATA, {'node': 22, 'dof': 1,
    'value': 0.00123684208613316, 'jobName': 'PullHinge', 'time': 1.0,
    'phase': STANDARD_PHASE, 'nset': 'ASSEMBLY__PICKEDSET12',
    'procedure': 'StaticStep'})
mdb.jobs['PullHinge']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 1, 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1,
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1,
    'jobName': 'PullHinge', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['PullHinge']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 2,
    'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
    'frame': 0, 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(STATUS, {'totalTime': 1.0, 'attempts': 0,
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 2,
    'jobName': 'PullHinge', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['PullHinge']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'PullHinge', 'memory': 43.0})
mdb.jobs['PullHinge']._Message(MONITOR_DATA, {'node': 22, 'dof': 1,
    'value': 0.00123684208613313, 'jobName': 'PullHinge', 'time': 2.0,
    'phase': STANDARD_PHASE, 'nset': 'ASSEMBLY__PICKEDSET12',
    'procedure': 'StaticStep'})
mdb.jobs['PullHinge']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 1,
    'frame': 1, 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(STATUS, {'totalTime': 2.0, 'attempts': 1,
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 2,
    'jobName': 'PullHinge', 'severe': 0, 'iterations': 1,
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['PullHinge']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 2,
    'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(COMPLETED, {'phase': STANDARD_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'PullHinge'})
mdb.jobs['PullHinge']._Message(JOB_COMPLETED, {
    'time': 'Sat Jun 02 11:28:35 2018', 'jobName': 'PullHinge'})
# Save by anwch on 2018_06_02-11.58.30; build 6.14-1 2014_06_05-03.41.02 134264
