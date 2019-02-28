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
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(20.0, 20.0),
    point2=(-20.0, 20.0))
#* Rectangle cannot be created.
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(20.0, 20.0),
    point2=(-20.0, -20.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='plate', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['plate'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1,
    minSizeFactor=0.1, size=4.0)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((209000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION,
    integrationRule=SIMPSON, material='Steel', name='shell', numIntPts=5,
    poissonDefinition=DEFAULT, preIntegrate=OFF, temperature=GRADIENT,
    thickness=0.01, thicknessField='', thicknessModulus=None, thicknessType=
    UNIFORM, useDensity=OFF)
mdb.models['Model-1'].parts['plate'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models['Model-1'].parts['plate'].faces.getSequenceFromMask(mask=(
    '[#1 ]', ), )), sectionName='shell', thicknessAssignment=FROM_SECTION)

mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='plate-1', part=
    mdb.models['Model-1'].parts['plate'])

mdb.models['Model-1'].StaticStep(name='Load', previous='Initial')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial',
    distributionType=UNIFORM, fieldName='', localCsys=None, name='fixed',
    region=Region(
    edges=mdb.models['Model-1'].rootAssembly.instances['plate-1'].edges.getSequenceFromMask(
    mask=('[#2 ]', ), )), u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=
    UNSET)

mdb.models['Model-1'].ConcentratedForce(cf1=10000.0, createStepName='Load',
    distributionType=UNIFORM, field='', localCsys=None, name='load', region=
    Region(
    vertices=mdb.models['Model-1'].rootAssembly.instances['plate-1'].vertices.getSequenceFromMask(
    mask=('[#1 ]', ), )))
mdb.models['Model-1'].loads['load'].setValues(cf1=0.0, cf3=10000.0,
    distributionType=UNIFORM, field='')
mdb.models['Model-1'].loads['load'].setValues(cf3=-10000.0, distributionType=
    UNIFORM, field='')
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE,
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE,
    'clientHost': 'Anw', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE,
    'file': 'E:\\Temp\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE,
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE,
    'clientHost': 'Anw', 'handle': 17992, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1,
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0,
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0,
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 0, 'phase': STANDARD_PHASE,
    'equilibrium': 0})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE,
    'jobName': 'Job-1', 'memory': 24.0})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 1U',
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 0.0, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE,
    'equilibrium': 4})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 2U',
    'timeIncrement': 0.25, 'increment': 1, 'stepTime': 0.0, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE,
    'equilibrium': 4})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 3U',
    'timeIncrement': 0.0625, 'increment': 1, 'stepTime': 0.0, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE,
    'equilibrium': 4})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 4U',
    'timeIncrement': 0.015625, 'increment': 1, 'stepTime': 0.0, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE,
    'equilibrium': 4})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 5U',
    'timeIncrement': 0.00390625, 'increment': 1, 'stepTime': 0.0, 'step': 1,
    'jobName': 'Job-1', 'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE,
    'equilibrium': 4})
mdb.jobs['Job-1']._Message(ERROR, {'phase': STANDARD_PHASE,
    'message': 'Too many attempts made for this increment',
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ABORTED, {'phase': STANDARD_PHASE,
    'message': 'Analysis phase failed due to errors', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.',
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.',
    'jobName': 'Job-1'})
mdb.jobs.changeKey(fromName='Job-1', toName='plate')
del mdb.models['Model-1'].boundaryConditions['fixed']
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial',
    distributionType=UNIFORM, fieldName='', localCsys=None, name='fixed',
    region=Region(
    edges=mdb.models['Model-1'].rootAssembly.instances['plate-1'].edges.getSequenceFromMask(
    mask=('[#2 ]', ), )), u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
# Save by anwch on 2018_06_02-13.13.27; build 6.14-1 2014_06_05-03.41.02 134264
