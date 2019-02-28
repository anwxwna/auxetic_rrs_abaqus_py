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
from odbAccess import *

import os
#Parameters---------------------------------------------------------------------

ln=30.0     #length of a quarter of the unit cells
ln1=10.0
ln2=5.0
nx=2         #number of unit cells x direction
ny=2         #number of unit cells in y direction
ln12=ln1+ln2
lnm=ln-ln12
Ex=100
v=0.3
#pattern parameter relationships
pex={0:ln1,1:0,2:0,3:lnm,4:0,5:0}
pey={0:lnm,1:0,2:0,3:ln1,4:0,5:0}

ph=[0,lnm,ln-ln1,ln,ln+ln1,2*ln-lnm]
pv=[0,ln1,ln-lnm,ln,ln+lnm,2*ln-ln1]

#geometry counter
ctr=1

inc=2*ln
##Create Model------------------------------------------------------------------
part_sketch_name='rigid_rot_square_3'

AuxPattM=mdb.models['Auxetic']
AuxPattM.ConstrainedSketch(name=part_sketch_name, sheetSize=200.0)
sketch1=AuxPattM.sketches[part_sketch_name]


#GEOMETRY-------------------------------------------------------------------------------
#Generating the outer boundary of the auxetic Pattern---------------------------

# function to the list of list of points to draw the edges in the x direction
def xy_dir(nq,pq,peq,i):
    loq=[[[] for r in range(2)] for j in range(6)]
    #print(loq)
    for k in range(6):
        for w in range(2):
            if k!=5:
                loq[k][w]=[pq[k+w],peq[k+w]]
                #print(loq[k][w])
            elif k==5:
                loq[k][w]=[(pq[k-k*w]+inc*(i+1)*w),peq[k-k*w]]
                #print(pq[k-k*w]+inc*(i+1)*w)
                #print(loq[k][w])
    return loq

# function to sketch the outer boundary in the x direction
def sketcher_x(nq,pq,peq,ctr):
    for i in range(nq):
        inq=inc*i
        pq=[x+inq for x in pq]
        loq=xy_dir(nq,pq,peq,i)
        for l in loq:
            sketch1.Line(point1=tuple(l[0]),point2=tuple(l[1]))
            ctr=ctr+1
    return ctr

#function to sketch the outer boundary in the y direction
def sketcher_y(nq,pq,peq,ctr):
    for i in range(nq):
        inq=inc*i
        pq=[x+inq for x in pq]
        #print(pq)
        loq=xy_dir(nq,pq,peq,i)
        #print(loq)
        for l in loq[1:]:
            sketch1.Line(point1=tuple(l[0].reverse()),point2=tuple(l[1].reverse()))
            ctr=ctr+1
    return ctr

sketcher_x(nx,ph,pex,ctr)
sketcher_y(ny,pv,pey,ctr)
print(ctr)
