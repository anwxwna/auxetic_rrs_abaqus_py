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
#Parameters---------------------------------------------------------------------
ln=30.0
ln1=10.0
ln2=5.0
st1=50
st2=-50
p1h=ln-(p1v)
p2=ln-ln1
p1v=ln12

#Unit Cell Pattern--------------------------------------------------------------
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)

#Sketch1=mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, ln1), point2=(
    0.0, p1v))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])

mdb.models['Model-1'].sketches['__profile__'].Line(point1=(ln1, ln), point2=
    (p1v, ln))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])

mdb.models['Model-1'].sketches['__profile__'].Line(point1=(ln, p1h), point2=
    (ln, p2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[4])

mdb.models['Model-1'].sketches['__profile__'].Line(point1=(p1h, 0.0), point2=(
    p2, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])

mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, ln1), point2=(
    p1h, 0.0))

mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, p1v), point2=(
    ln1, ln))

mdb.models['Model-1'].sketches['__profile__'].Line(point1=(p2, 0.0), point2=(
    ln, p1h))

mdb.models['Model-1'].sketches['__profile__'].Line(point1=(ln, p2), point2=
    (p1v, ln))
# Save by anwch on 2018_06_04-13.24.23; build 6.14-1 2014_06_05-03.41.02 134264

mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
    DEFORMABLE_BODY)

#saving the sketch as a 2D shell
mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

#Change of name
mdb.models['Model-1'].parts.changeKey(fromName='Part-1', toName=
    'rigid_rot_square_2')

#editing the sketch with name __edit__
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['rigid_rot_square_2'].features['Shell planar-1'].sketch)
mdb.models['Model-1'].parts['rigid_rot_square_2'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'],
    upToFeature=
    mdb.models['Model-1'].parts['rigid_rot_square_2'].features['Shell planar-1'])


# mirror vertical
mdb.models['Model-1'].sketches['__edit__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__edit__'].geometry[2], objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[2],
    mdb.models['Model-1'].sketches['__edit__'].geometry[3],
    mdb.models['Model-1'].sketches['__edit__'].geometry[4],
    mdb.models['Model-1'].sketches['__edit__'].geometry[5],
    mdb.models['Model-1'].sketches['__edit__'].geometry[6],
    mdb.models['Model-1'].sketches['__edit__'].geometry[7],
    mdb.models['Model-1'].sketches['__edit__'].geometry[8],
    mdb.models['Model-1'].sketches['__edit__'].geometry[9]))

#mirror horizontal
mdb.models['Model-1'].sketches['__edit__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__edit__'].geometry[5], objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[2],
    mdb.models['Model-1'].sketches['__edit__'].geometry[3],
    mdb.models['Model-1'].sketches['__edit__'].geometry[4], #
    mdb.models['Model-1'].sketches['__edit__'].geometry[5],
    mdb.models['Model-1'].sketches['__edit__'].geometry[6], #
    mdb.models['Model-1'].sketches['__edit__'].geometry[7],
    mdb.models['Model-1'].sketches['__edit__'].geometry[8], #
    mdb.models['Model-1'].sketches['__edit__'].geometry[9],
    mdb.models['Model-1'].sketches['__edit__'].geometry[11], #
    mdb.models['Model-1'].sketches['__edit__'].geometry[12],
    mdb.models['Model-1'].sketches['__edit__'].geometry[13], #
    mdb.models['Model-1'].sketches['__edit__'].geometry[14],
    mdb.models['Model-1'].sketches['__edit__'].geometry[15], #
    mdb.models['Model-1'].sketches['__edit__'].geometry[16],
    mdb.models['Model-1'].sketches['__edit__'].geometry[17], #
    mdb.models['Model-1'].sketches['__edit__'].geometry[18])) #35

for i in range(2,8):
    if i%2==0:
        objectList_1.append(mdb.models['Model-1'].sketches['__edit__'].geometry[i])
objectList_1=tuple(objectList_1)
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=objectList_1)
for i in range(11,19):
    if i%2!=0:
        objectList_1.append(mdb.models['Model-1'].sketches['__edit__'].geometry[i])
objectList_2=tuple(objectList_2)
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=objectList_2)
