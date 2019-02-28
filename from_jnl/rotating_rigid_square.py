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
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-35.0, -35.0), 
    point2=(35.0, 35.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 35.0), point2=(
    0.0, 1.25))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 35.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    -35.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 35.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[6],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    35.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(35.0, 0.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[9],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, -35.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[11])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -35.0), point2=
    (0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[11],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    -35.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-40.0, -40.0),
    point2=(40.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[2],
    mdb.models['Model-1'].sketches['__profile__'].geometry[3],
    mdb.models['Model-1'].sketches['__profile__'].geometry[4],
    mdb.models['Model-1'].sketches['__profile__'].geometry[5]))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 3.75), point2=(
    0.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 40.0), point2=(
    -40.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 40.0),
    point2=(-40.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, -40.0),
    point2=(0.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -40.0), point2=
    (0.0, -3.75))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 3.75), point2=(
    0.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[11])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[6],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[11])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 40.0), point2=(
    40.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(40.0, 40.0), point2=
    (40.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(40.0, -40.0),
    point2=(0.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -40.0), point2=
    (0.0, -3.75))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[15])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[15])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -40.0), point2=
    (0.0, -3.75))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[16])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[16])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
#* Nothing to undo.
mdb.models['Model-1'].sketches['__profile__'].undo()
#* Nothing to undo.
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 40.0),
    point2=(0.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6])
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], ))
mdb.models['Model-1'].sketches['__profile__'].rotate(angle=15.0, centerPoint=(
    -40.0, 40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[2],
    mdb.models['Model-1'].sketches['__profile__'].geometry[4],
    mdb.models['Model-1'].sketches['__profile__'].geometry[5]))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-40.0, 40.0),
    point2=(38.75, -40.0))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 40.0),
    point2=(-40.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].rotate(angle=15.0, centerPoint=(
    -40.0, 40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].rotate(angle=5.0, centerPoint=(
    -40.0, 40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[2],
    mdb.models['Model-1'].sketches['__profile__'].geometry[4],
    mdb.models['Model-1'].sketches['__profile__'].geometry[5],
    mdb.models['Model-1'].sketches['__profile__'].constraints[20],
    mdb.models['Model-1'].sketches['__profile__'].constraints[21]))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 40.0),
    point2=(-40.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].rotate(angle=5.0, centerPoint=(
    5.0, 0.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=5.0,
    centerPoint=(-40.0, 40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 0.0), point2=
    (-40.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[8],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=-5.0,
    centerPoint=(-40.0, -40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, -40.0),
    point2=(0.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=5.0,
    centerPoint=(-40.0, -40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=5.0,
    centerPoint=(-40.0, -40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=-5.0,
    centerPoint=(-40.0, -40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 40.0), point2=(
    40.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(40.0, 40.0), point2=
    (40.0, 1.25))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[15])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[15])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(40.0, 0.0), point2=(
    40.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[15])
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=5.0,
    centerPoint=(40.0, 40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[14],
    mdb.models['Model-1'].sketches['__profile__'].geometry[15]))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=-5.0,
    centerPoint=(40.0, 40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[14],
    mdb.models['Model-1'].sketches['__profile__'].geometry[15]))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -40.0), point2=
    (40.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[18])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[12],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[18])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(40.0, -40.0),
    point2=(40.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[19])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[18], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[19])
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=-5.0,
    centerPoint=(40.0, -40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[18],
    mdb.models['Model-1'].sketches['__profile__'].geometry[19]))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=5.0,
    centerPoint=(40.0, -40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[18],
    mdb.models['Model-1'].sketches['__profile__'].geometry[19]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[8],
    mdb.models['Model-1'].sketches['__profile__'].geometry[10],
    mdb.models['Model-1'].sketches['__profile__'].geometry[12],
    mdb.models['Model-1'].sketches['__profile__'].geometry[18],
    mdb.models['Model-1'].sketches['__profile__'].geometry[19],
    mdb.models['Model-1'].sketches['__profile__'].geometry[15],
    mdb.models['Model-1'].sketches['__profile__'].geometry[14]))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    -0.152212076330181, -43.4862297099063))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.152212076330181, -43.4862297099063))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 0.0), point2=
    (0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[22])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0),
    point2=(-40.0, 40.0))
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=5.0,
    centerPoint=(-40.0, 40.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[25],
    mdb.models['Model-1'].sketches['__profile__'].geometry[22],
    mdb.models['Model-1'].sketches['__profile__'].geometry[24],
    mdb.models['Model-1'].sketches['__profile__'].geometry[23]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[24],
    mdb.models['Model-1'].sketches['__profile__'].geometry[25],
    mdb.models['Model-1'].sketches['__profile__'].geometry[22],
    mdb.models['Model-1'].sketches['__profile__'].geometry[23]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.152212076330181,
    43.4862297099063), point2=(0.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[30], ))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[30], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[28],
    mdb.models['Model-1'].sketches['__profile__'].geometry[29],
    mdb.models['Model-1'].sketches['__profile__'].geometry[26],
    mdb.models['Model-1'].sketches['__profile__'].geometry[27]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[30], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 0.0), point2=
    (40.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[35])
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[35], ))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[35], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[16],
    mdb.models['Model-1'].sketches['__profile__'].geometry[17],
    mdb.models['Model-1'].sketches['__profile__'].geometry[26],
    mdb.models['Model-1'].sketches['__profile__'].geometry[27],
    mdb.models['Model-1'].sketches['__profile__'].geometry[28],
    mdb.models['Model-1'].sketches['__profile__'].geometry[29],
    mdb.models['Model-1'].sketches['__profile__'].geometry[31],
    mdb.models['Model-1'].sketches['__profile__'].geometry[32],
    mdb.models['Model-1'].sketches['__profile__'].geometry[33],
    mdb.models['Model-1'].sketches['__profile__'].geometry[34]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[35], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 40.0), point2=(
    0.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[30])
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[30], ))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[28], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[27],
    mdb.models['Model-1'].sketches['__profile__'].geometry[26],
    mdb.models['Model-1'].sketches['__profile__'].geometry[29]))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[30], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[28],
    mdb.models['Model-1'].sketches['__profile__'].geometry[29],
    mdb.models['Model-1'].sketches['__profile__'].geometry[26],
    mdb.models['Model-1'].sketches['__profile__'].geometry[27]))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 0.0), point2=
    (40.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[35])
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[35], ))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[35], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[16],
    mdb.models['Model-1'].sketches['__profile__'].geometry[17],
    mdb.models['Model-1'].sketches['__profile__'].geometry[26],
    mdb.models['Model-1'].sketches['__profile__'].geometry[27],
    mdb.models['Model-1'].sketches['__profile__'].geometry[28],
    mdb.models['Model-1'].sketches['__profile__'].geometry[30],
    mdb.models['Model-1'].sketches['__profile__'].geometry[31],
    mdb.models['Model-1'].sketches['__profile__'].geometry[32],
    mdb.models['Model-1'].sketches['__profile__'].geometry[33],
    mdb.models['Model-1'].sketches['__profile__'].geometry[29],
    mdb.models['Model-1'].sketches['__profile__'].geometry[34]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[30],
    mdb.models['Model-1'].sketches['__profile__'].geometry[35],
    mdb.models['Model-1'].sketches['__profile__'].geometry[30],
    mdb.models['Model-1'].sketches['__profile__'].geometry[30]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[42], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[43],
    mdb.models['Model-1'].sketches['__profile__'].geometry[38]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[31],
    mdb.models['Model-1'].sketches['__profile__'].geometry[26]))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.5137702900937,
    0.152212076330179), point2=(-36.5005834944895, 0.00148631352931261))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[28],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[47])
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[47], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.5137702900937,
    0.152212076330179), point2=(-36.5004534590897, 0.0))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[28],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[48])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.500453458964,
    0.0), point2=(-36.5137702900937, -0.152212076330179))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.5137702900937,
    0.152212076330179), point2=(-36.500453458964, 0.0))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[28],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[50])
mdb.models['Model-1'].sketches['__profile__'].dragEntity(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[48], points=((
    -36.511667122585, 0.128172761704749), (-36.5152473449707,
    0.127859532833099), (-36.4840927124023, 0.116200357675552), (
    -36.4581260681152, 0.104541182518005), (-36.4750061035156,
    0.103245735168457), (-36.4905815124512, 0.103245735168457), (
    -36.5074577331543, 0.105836659669876), (-36.516544342041,
    0.107132136821747)))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].autoDimension(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[48], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=95.0,
    centerPoint=(-36.500453458964, 0.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[48], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=95.0,
    centerPoint=(-36.500453458964, 0.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[48], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].copyRotate(angle=-95.0,
    centerPoint=(-36.500453458964, 0.0), objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[48], ))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0,
    3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[58], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[29])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0,
    -3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[59], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[41])
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[41],
    mdb.models['Model-1'].sketches['__profile__'].geometry[29],
    mdb.models['Model-1'].sketches['__profile__'].geometry[34],
    mdb.models['Model-1'].sketches['__profile__'].geometry[46]))
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0,
    40.0), point2=(0.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[51])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 40.0), point2=(
    0.0, -40.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[51])
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], ))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[49],
    mdb.models['Model-1'].sketches['__profile__'].geometry[50],
    mdb.models['Model-1'].sketches['__profile__'].geometry[48]))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.3476599572302,
    0.0), point2=(0.0, 3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.152212076330181,
    43.4862297099063), point2=(-1.91477130301808, 43.3320257587781))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[27],
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[56])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[68], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[27])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -4.87793970108032, 37.4401016235352), value=38.5, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[31], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[29])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    7.88405227661133, 33.0788078308105), value=38.5, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[19], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[20])
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[32], ))
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -12.9399185180664, -31.6178894042969), value=38.5, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[14], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[15])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    14.6614532470703, -51.1969985961914), value=38.5, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[23], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[25])
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[39],
    mdb.models['Model-1'].sketches['__profile__'].geometry[36]))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[44], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-1.6465041234678,
    43.3554960957848), point2=(0.0, 3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-1.6465041234678,
    43.3554960957848), point2=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[67], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[60], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[61], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[67])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
# Save by anwch on 2018_06_03-20.23.27; build 6.14-1 2014_06_05-03.41.02 134264
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
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
#* Nothing to undo.
mdb.models['Model-1'].sketches['__profile__'].redo()
mdb.models['Model-1'].sketches['__profile__'].redo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.3476599572302,
    0.0), point2=(0.0, -3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(40.0, 0.0), point2=(
    -40.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55])
mdb.models['Model-1'].sketches['__profile__'].setAsConstruction(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.3476599572302,
    0.0), point2=(0.0, -3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.500453458964,
    0.0), point2=(0.0, -3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, 0.0), point2=
    (0.0, -3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-40.0, -40.0),
    point2=(-40.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[56])
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,
    -3.34675303930307), point2=(-31.25, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[70], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[56], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], textPoint=(
    -9.874680519104, -0.333072662353516), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,
    -3.34675303930307), point2=(-32.9574394226074, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[70], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[56], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], textPoint=(
    -17.5884132385254, -0.682961463928223), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-31.25, 0.0),
    point2=(0.0, -3.34675303930307))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[69], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[56], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], textPoint=(
    -13.7705402374268, -1.83001697063446), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].VerticalDimension(textPoint=(
    7.93014144897461, -2.11720108985901), value=6.69350607860614, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[59], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[58])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,
    -3.34675303930307), point2=(-28.75, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[70], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[56], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], textPoint=(
    -11.3359756469727, -1.11491417884827), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-36.3476599572302,
    0.0), point2=(0.0, -6.25))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[69], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[56], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], textPoint=(
    -16.4719161987305, -2.28822422027588), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,
    -3.18000819195376), point2=(-2.2667777585195, -43.3012291844338))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[70], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[39])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[57], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], textPoint=(
    -0.496700525283813, -30.5629901885986), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[57], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], textPoint=(
    -1.10937333106995, -38.4937515258789), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[40],
    mdb.models['Model-1'].sketches['__profile__'].geometry[39]))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13], point1=(
    -1.89092183113098, -43.23095703125))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[51],
    mdb.models['Model-1'].sketches['__profile__'].geometry[57],
    mdb.models['Model-1'].sketches['__profile__'].geometry[56]))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[61],
    mdb.models['Model-1'].sketches['__profile__'].geometry[60],
    mdb.models['Model-1'].sketches['__profile__'].geometry[56],
    mdb.models['Model-1'].sketches['__profile__'].geometry[57]))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].dragEntity(entity=
    mdb.models['Model-1'].sketches['__profile__'].vertices[69], points=((0.0,
    -3.18000819195376), (0.0, -3.18000819195376), (0.766905069351196,
    -3.28489828109741), (0.834991693496704, -3.31887006759644)))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].dragEntity(entity=
    mdb.models['Model-1'].sketches['__profile__'].vertices[69], points=((0.0,
    -3.18000819195376), (0.0, -3.75), (2.5, -3.75), (3.75, -5.0), (5.0, -5.0),
    (7.5, -5.0), (8.75, -5.0), (10.0, -5.0), (11.25, -6.25), (13.75, -6.25), (
    13.75, -7.5), (16.25, -8.75), (17.5, -10.0), (20.0, -13.75), (21.25,
    -15.0), (22.5, -17.5), (23.75, -20.0), (27.5, -25.0), (27.5, -27.5), (
    28.75, -28.75)))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,
    -3.18000819195376), point2=(0.0, -3.29849314689636))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[57])
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[70], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51])
mdb.models['Model-1'].sketches['__profile__'].VerticalDimension(textPoint=(
    0.17171910405159, -3.21462941169739), value=0.15, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[70], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[69])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,
    -3.33000819195376), point2=(-4.56851922753626, -43.0998528995273))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[71], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[58], line2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], textPoint=(
    -1.39049434661865, -37.0016860961914), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[13], ))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[39], point1=(
    -2.34733200073242, -43.3812370300293))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[58],
    mdb.models['Model-1'].sketches['__profile__'].geometry[56]))
mdb.models['Model-1'].sketches['__profile__'].copyMirror(mirrorLine=
    mdb.models['Model-1'].sketches['__profile__'].geometry[55], objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[56],
    mdb.models['Model-1'].sketches['__profile__'].geometry[58],
    mdb.models['Model-1'].sketches['__profile__'].geometry[61],
    mdb.models['Model-1'].sketches['__profile__'].geometry[60]))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[27], point1=(
    -0.905808448791504, 43.434497833252))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[16], point1=(
    1.70158290863037, 43.1843147277832))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[32], point1=(
    2.00243663787842, 43.3344268798828))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[20], point1=(
    2.14177513122559, -43.2855415344238))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[36], point1=(
    1.43664360046387, -43.4419059753418))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[44], point1=(
    1.90672874450684, -43.4419059753418))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[69], point1=(
    19.2324714660645, -42.2196884155273))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[70], point1=(
    13.8766975402832, -42.4105606079102))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[21], point1=(
    37.3455848693848, -14.0881118774414))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[37], point1=(
    36.7478370666504, -16.4740676879883))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[17], point1=(
    38.8399391174316, 19.3152160644531))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[33], point1=(
    37.644458770752, 19.9116973876953))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[67], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[59], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[71], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[45], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[33], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[66], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[68], ))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[54], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[50], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[51], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[57], ))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[58], point1=(
    -3.48967051506042, -43.2064476013184))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[61], point1=(
    3.48844742774963, -43.2043800354004))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[63], point1=(
    -3.48937177658081, 43.2012138366699))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[65], point1=(
    3.48903560638428, 43.200798034668))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='square', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['square'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['square'].features['Shell planar-1'].sketch)
mdb.models['Model-1'].parts['square'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'],
    upToFeature=
    mdb.models['Model-1'].parts['square'].features['Shell planar-1'])
# Save by anwch on 2018_06_03-20.56.50; build 6.14-1 2014_06_05-03.41.02 134264
# Save by anwch on 2018_06_04-02.08.47; build 6.14-1 2014_06_05-03.41.02 134264
