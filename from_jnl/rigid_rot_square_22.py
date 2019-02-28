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
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 10.0), point2=(
    0.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 10.0), point2=(
    15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 0.0), point2=(
    20.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 15.0), point2=(
    10.0, 30.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(10.0, 30.0), point2=
    (15.0, 30.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 0.0), point2=(
    30.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, 15.0), point2=
    (30.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, 20.0), point2=
    (15.0, 30.0))
# Save by anwch on 2018_06_04-13.24.23; build 6.14-1 2014_06_05-03.41.02 134264
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
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts.changeKey(fromName='Part-1', toName=
    'rigid_rot_square_2')
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['rigid_rot_square_2'].features['Shell planar-1'].sketch)
mdb.models['Model-1'].parts['rigid_rot_square_2'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'],
    upToFeature=
    mdb.models['Model-1'].parts['rigid_rot_square_2'].features['Shell planar-1'])
mdb.models['Model-1'].sketches['__edit__'].Line(point1=(0.0, 35.0), point2=(
    0.0, -35.0))
mdb.models['Model-1'].sketches['__edit__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__edit__'].geometry[10])
mdb.models['Model-1'].sketches['__edit__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[10], ))
mdb.models['Model-1'].sketches['__edit__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__edit__'].geometry[10], objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[2],
    mdb.models['Model-1'].sketches['__edit__'].geometry[3],
    mdb.models['Model-1'].sketches['__edit__'].geometry[4],
    mdb.models['Model-1'].sketches['__edit__'].geometry[5],
    mdb.models['Model-1'].sketches['__edit__'].geometry[6],
    mdb.models['Model-1'].sketches['__edit__'].geometry[7],
    mdb.models['Model-1'].sketches['__edit__'].geometry[8],
    mdb.models['Model-1'].sketches['__edit__'].geometry[9],
    mdb.models['Model-1'].sketches['__edit__'].geometry[10]))
mdb.models['Model-1'].sketches['__edit__'].Line(point1=(-35.0, 0.0), point2=(
    35.0, 0.0))
mdb.models['Model-1'].sketches['__edit__'].HorizontalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__edit__'].geometry[20])
mdb.models['Model-1'].sketches['__edit__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[20], ))
mdb.models['Model-1'].sketches['__edit__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__edit__'].geometry[20], objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[2],
    mdb.models['Model-1'].sketches['__edit__'].geometry[3],
    mdb.models['Model-1'].sketches['__edit__'].geometry[4],
    mdb.models['Model-1'].sketches['__edit__'].geometry[5],
    mdb.models['Model-1'].sketches['__edit__'].geometry[6],
    mdb.models['Model-1'].sketches['__edit__'].geometry[7],
    mdb.models['Model-1'].sketches['__edit__'].geometry[8],
    mdb.models['Model-1'].sketches['__edit__'].geometry[9],
    mdb.models['Model-1'].sketches['__edit__'].geometry[10],
    mdb.models['Model-1'].sketches['__edit__'].geometry[11],
    mdb.models['Model-1'].sketches['__edit__'].geometry[12],
    mdb.models['Model-1'].sketches['__edit__'].geometry[13],
    mdb.models['Model-1'].sketches['__edit__'].geometry[14],
    mdb.models['Model-1'].sketches['__edit__'].geometry[15],
    mdb.models['Model-1'].sketches['__edit__'].geometry[16],
    mdb.models['Model-1'].sketches['__edit__'].geometry[17],
    mdb.models['Model-1'].sketches['__edit__'].geometry[18],
    mdb.models['Model-1'].sketches['__edit__'].geometry[19],
    mdb.models['Model-1'].sketches['__edit__'].geometry[20]))
# Save by anwch on 2018_06_04-13.39.59; build 6.14-1 2014_06_05-03.41.02 134264
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
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[10],
    mdb.models['Model-1'].sketches['__edit__'].geometry[19],
    mdb.models['Model-1'].sketches['__edit__'].geometry[21],
    mdb.models['Model-1'].sketches['__edit__'].geometry[29],
    mdb.models['Model-1'].sketches['__edit__'].geometry[30],
    mdb.models['Model-1'].sketches['__edit__'].geometry[38],
    mdb.models['Model-1'].sketches['__edit__'].geometry[13],
    mdb.models['Model-1'].sketches['__edit__'].geometry[20],
    mdb.models['Model-1'].sketches['__edit__'].geometry[32],
    mdb.models['Model-1'].sketches['__edit__'].geometry[39],
    mdb.models['Model-1'].sketches['__edit__'].geometry[4],
    mdb.models['Model-1'].sketches['__edit__'].geometry[20],
    mdb.models['Model-1'].sketches['__edit__'].geometry[23],
    mdb.models['Model-1'].sketches['__edit__'].geometry[39],
    mdb.models['Model-1'].sketches['__edit__'].geometry[2],
    mdb.models['Model-1'].sketches['__edit__'].geometry[10],
    mdb.models['Model-1'].sketches['__edit__'].geometry[11],
    mdb.models['Model-1'].sketches['__edit__'].geometry[19],
    mdb.models['Model-1'].sketches['__edit__'].geometry[29],
    mdb.models['Model-1'].sketches['__edit__'].geometry[38]))
mdb.models['Model-1'].sketches['__edit__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__edit__'].geometry[8], objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[3],
    mdb.models['Model-1'].sketches['__edit__'].geometry[5],
    mdb.models['Model-1'].sketches['__edit__'].geometry[6],
    mdb.models['Model-1'].sketches['__edit__'].geometry[7],
    mdb.models['Model-1'].sketches['__edit__'].geometry[8],
    mdb.models['Model-1'].sketches['__edit__'].geometry[9],
    mdb.models['Model-1'].sketches['__edit__'].geometry[12],
    mdb.models['Model-1'].sketches['__edit__'].geometry[14],
    mdb.models['Model-1'].sketches['__edit__'].geometry[15],
    mdb.models['Model-1'].sketches['__edit__'].geometry[16],
    mdb.models['Model-1'].sketches['__edit__'].geometry[17],
    mdb.models['Model-1'].sketches['__edit__'].geometry[18],
    mdb.models['Model-1'].sketches['__edit__'].geometry[22],
    mdb.models['Model-1'].sketches['__edit__'].geometry[24],
    mdb.models['Model-1'].sketches['__edit__'].geometry[25],
    mdb.models['Model-1'].sketches['__edit__'].geometry[26],
    mdb.models['Model-1'].sketches['__edit__'].geometry[27],
    mdb.models['Model-1'].sketches['__edit__'].geometry[28],
    mdb.models['Model-1'].sketches['__edit__'].geometry[31],
    mdb.models['Model-1'].sketches['__edit__'].geometry[33],
    mdb.models['Model-1'].sketches['__edit__'].geometry[34],
    mdb.models['Model-1'].sketches['__edit__'].geometry[35],
    mdb.models['Model-1'].sketches['__edit__'].geometry[36],
    mdb.models['Model-1'].sketches['__edit__'].geometry[37]))
mdb.models['Model-1'].sketches['__edit__'].undo()
mdb.models['Model-1'].sketches['__edit__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__edit__'].geometry[3],
    mdb.models['Model-1'].sketches['__edit__'].geometry[5],
    mdb.models['Model-1'].sketches['__edit__'].geometry[6],
    mdb.models['Model-1'].sketches['__edit__'].geometry[7],
    mdb.models['Model-1'].sketches['__edit__'].geometry[8],
    mdb.models['Model-1'].sketches['__edit__'].geometry[9],
    mdb.models['Model-1'].sketches['__edit__'].geometry[12],
    mdb.models['Model-1'].sketches['__edit__'].geometry[14],
    mdb.models['Model-1'].sketches['__edit__'].geometry[15],
    mdb.models['Model-1'].sketches['__edit__'].geometry[16],
    mdb.models['Model-1'].sketches['__edit__'].geometry[17],
    mdb.models['Model-1'].sketches['__edit__'].geometry[18],
    mdb.models['Model-1'].sketches['__edit__'].geometry[22],
    mdb.models['Model-1'].sketches['__edit__'].geometry[24],
    mdb.models['Model-1'].sketches['__edit__'].geometry[25],
    mdb.models['Model-1'].sketches['__edit__'].geometry[26],
    mdb.models['Model-1'].sketches['__edit__'].geometry[27],
    mdb.models['Model-1'].sketches['__edit__'].geometry[28],
    mdb.models['Model-1'].sketches['__edit__'].geometry[31],
    mdb.models['Model-1'].sketches['__edit__'].geometry[33],
    mdb.models['Model-1'].sketches['__edit__'].geometry[34],
    mdb.models['Model-1'].sketches['__edit__'].geometry[35],
    mdb.models['Model-1'].sketches['__edit__'].geometry[36],
    mdb.models['Model-1'].sketches['__edit__'].geometry[37]), number1=4,
    number2=4, spacing1=60.0, spacing2=60.0, vertexList=())
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[15],
    mdb.models['Model-1'].sketches['__edit__'].geometry[132],
    mdb.models['Model-1'].sketches['__edit__'].geometry[128],
    mdb.models['Model-1'].sketches['__edit__'].geometry[158],
    mdb.models['Model-1'].sketches['__edit__'].geometry[42],
    mdb.models['Model-1'].sketches['__edit__'].geometry[150],
    mdb.models['Model-1'].sketches['__edit__'].geometry[44],
    mdb.models['Model-1'].sketches['__edit__'].geometry[74],
    mdb.models['Model-1'].sketches['__edit__'].geometry[72],
    mdb.models['Model-1'].sketches['__edit__'].geometry[180],
    mdb.models['Model-1'].sketches['__edit__'].geometry[68],
    mdb.models['Model-1'].sketches['__edit__'].geometry[98],
    mdb.models['Model-1'].sketches['__edit__'].geometry[96],
    mdb.models['Model-1'].sketches['__edit__'].geometry[204],
    mdb.models['Model-1'].sketches['__edit__'].geometry[27],
    mdb.models['Model-1'].sketches['__edit__'].geometry[62],
    mdb.models['Model-1'].sketches['__edit__'].geometry[224],
    mdb.models['Model-1'].sketches['__edit__'].geometry[254],
    mdb.models['Model-1'].sketches['__edit__'].geometry[144],
    mdb.models['Model-1'].sketches['__edit__'].geometry[252],
    mdb.models['Model-1'].sketches['__edit__'].geometry[248],
    mdb.models['Model-1'].sketches['__edit__'].geometry[278],
    mdb.models['Model-1'].sketches['__edit__'].geometry[140],
    mdb.models['Model-1'].sketches['__edit__'].geometry[170],
    mdb.models['Model-1'].sketches['__edit__'].geometry[120],
    mdb.models['Model-1'].sketches['__edit__'].geometry[228],
    mdb.models['Model-1'].sketches['__edit__'].geometry[164],
    mdb.models['Model-1'].sketches['__edit__'].geometry[194],
    mdb.models['Model-1'].sketches['__edit__'].geometry[162],
    mdb.models['Model-1'].sketches['__edit__'].geometry[270]))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[272],
    mdb.models['Model-1'].sketches['__edit__'].geometry[302],
    mdb.models['Model-1'].sketches['__edit__'].geometry[192],
    mdb.models['Model-1'].sketches['__edit__'].geometry[300],
    mdb.models['Model-1'].sketches['__edit__'].geometry[186],
    mdb.models['Model-1'].sketches['__edit__'].geometry[294]))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[8],
    mdb.models['Model-1'].sketches['__edit__'].geometry[50],
    mdb.models['Model-1'].sketches['__edit__'].constraints[19],
    mdb.models['Model-1'].sketches['__edit__'].constraints[204]))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[6], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[126], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[48], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[156], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[66], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[174], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[90], ))
# Save by anwch on 2018_06_04-16.36.30; build 6.14-1 2014_06_05-03.41.02 134264
