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
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(32.5, 0.0), point2=(
    41.25, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    34.1676597595215, -6.62362194061279), value=4.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 16.25), point2=
    (37.25, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 16.25), point2=
    (0.0, 20.4808349609375))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -4.93093109130859, 16.855396270752), value=4.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(50.0, 0.0), point2=(
    -50.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 50.0), point2=(
    0.0, -50.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], ))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7])
mdb.models['Model-1'].sketches['__profile__'].VerticalDimension(textPoint=(
    -5.36343765258789, 2.26732921600342), value=12.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7])
mdb.models['Model-1'].sketches['__profile__'].VerticalDimension(textPoint=(
    -3.6355094909668, 3.53203392028809), value=12.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 12.0), point2=(
    0.0, 16.7790679931641))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].VerticalDimension(textPoint=(
    -3.33052825927734, 16.4747314453125), value=4.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(41.25, 0.0), point2=
    (53.75, 30.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalDimension(textPoint=(
    48.9879150390625, -13.5875854492188), value=12.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(53.25, 28.8),
    point2=(53.25, 34.5790634155273))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(53.25, 28.8),
    point2=(53.25, 37.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    58.0045585632324, 32.0303421020508), value=4.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[10])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 16.0), point2=(
    12.5, 50.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(12.5, 50.0), point2=
    (19.8828239440918, 50.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(19.8828239440918,
    50.0), point2=(53.25, 32.8))
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    20.0990791320801, 62.5791854858398), value=4.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[11], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[12])
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='rigid_rotating_square'
    , type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['rigid_rotating_square'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 10.0), point2=(
    0.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 0.0), point2=(
    15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 0.0), point2=(
    0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, 15.0), point2=
    (20.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 15.0), point2=(
    10.0, 30.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(10.0, 30.0), point2=
    (15.0, 30.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 30.0), point2=
    (30.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, 20.0), point2=
    (30.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-2', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-2'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['rigid_rotating_square']
mdb.models['Model-1'].parts.changeKey(fromName='Part-2', toName=
    'rigid_rotating_square_1')
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['rigid_rotating_square_1'].features['Shell planar-1'].sketch)
mdb.models['Model-1'].parts['rigid_rotating_square_1'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'],
    upToFeature=
    mdb.models['Model-1'].parts['rigid_rotating_square_1'].features['Shell planar-1'])
# Save by anwch on 2018_06_04-13.14.23; build 6.14-1 2014_06_05-03.41.02 134264
