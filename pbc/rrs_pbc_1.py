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
import regionToolset
import mesh
import subprocess
import sys
import os
import math
import csv
import numpy as np
from datetime import datetime

iteration_count=4
#PARAMETERS---------------------------------------------------------------------
###-------------------------------------------------------------------------
#the hinge width
ln2=2.0
#edge length of a square
#l=50.0
## ln1 and ln will be changed as a function of theta
#theta=[]
#ln and ln1 determine the initial rotated state of the rrs of the solid piece
#ln1=math.cos(math.radian(theta))*(l-2*ln2*math.cos(math.radian(theta)))   #length of a quarter of the unit cells
#ln=(l-2*ln2*math.cos(math.radian(theta)))(math.cos(math.radian(theta))+math.sin(math.radian(theta))) +ln2
ln1=15.0
ln=50.0
#number of unit cells-----------------------------
nx=1        #number of unit cells x direction
ny=1        #number of unit cells in y direction
#some commonly used relationships----------------
ln12=ln1+ln2
lnm=ln-ln12

#pattern parameter relationships------------------
#points above the horizontal axis having the points for the edge inclusions
pex={0:ln1,1:0,2:0,3:lnm,4:0,5:0}
pey={0:lnm,1:0,2:0,3:ln1,4:0,5:0}
# points along the horizontal axis
ph=[0,lnm,ln-ln1,ln,ln+ln1,2*ln-lnm]
pv=[0,ln1,ln-lnm,ln,ln+lnm,2*ln-ln1]

#geometry counter
ctr=1
#displacement at right boundary
right_disp=10
inc=2*ln
#Material properties-----------------------------------------------
Ex=200E9  #youngs modulus of the material used
v=0.29   #poissons ratio of the materials used
rho=7872
#Mesh Constraints
mesh_size=1

##CREATE MODEL------------------------------------------------------------------
part_sketch_name='rrs'
model_name=part_sketch_name +repr(nx)+'by'+ repr(ny)+ 'pbc'
print(model_name)
AuxPattM=mdb.Model(name=model_name)
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
        loq=xy_dir(nq,pq,peq,i)
        #print(loq)
        for l in loq[1:]:
            sketch1.Line(point1=tuple(l[0].reverse()),point2=tuple(l[1].reverse()))
            ctr=ctr+1
    return ctr

#sketcher_x(nx,ph,pex,ctr)
#sketcher_y(ny,pv,pey,ctr)
#print(ctr)

#X dir (2-nx*6)---- this is the first manual attempt
for i in range(nx):
    sketch1.Line(point1=(0+i*2*ln,ln1), point2=(lnm+(i*2*ln),0))
    sketch1.Line(point1=(lnm+(i*2*ln),0), point2=(ln-ln1+(i*2*ln),0))
    sketch1.Line(point1=(ln-ln1+(i*2*ln),0), point2=(ln+(i*2*ln),lnm))
    sketch1.Line(point1=(ln+(i*2*ln),lnm), point2=(ln1+ln+(i*2*ln),0))
    sketch1.Line(point1=(ln1+ln+(i*2*ln),0), point2=(ln+ln12+(i*2*ln),0))
    sketch1.Line(point1=(ln+ln12+(i*2*ln),0),point2= (2*ln+ (i*2*ln),ln1))

#Y dir (nx*6+1 -(nx+ny)*6)
for i in range(ny):
    if i==0:
        sketch1.Line(point1=(0, ln1+(i*2*ln)), point2=(0,ln-lnm+(i*2*ln)))
        sketch1.Line(point1=(0,ln12+(i*2*ln)), point2=(ln1,ln+(i*2*ln)))
        sketch1.Line(point1=(ln1,ln+(i*2*ln)), point2=(0,ln+lnm+(i*2*ln)))
        sketch1.Line(point1=(0,ln+lnm+(i*2*ln)), point2=(0,2*ln-ln1+(i*2*ln)))
        sketch1.Line(point1=(0,2*ln-ln1+(i*2*ln)), point2=(lnm,2*ln+(i*2*ln)))
    else:
        sketch1.Line(point1=(0, ln1+(i*2*ln)), point2=(lnm,0+(i*2*ln)))
        sketch1.Line(point1=(0, ln1+(i*2*ln)), point2=(0,ln-lnm+(i*2*ln)))
        sketch1.Line(point1=(0,ln-lnm+(i*2*ln)), point2=(ln1,ln+(i*2*ln)))
        sketch1.Line(point1=(ln1,ln+(i*2*ln)), point2=(0,ln+lnm+(i*2*ln)))
        sketch1.Line(point1=(0,ln+lnm+(i*2*ln)), point2=(0,2*ln-ln1+(i*2*ln)))
        sketch1.Line(point1=(0,2*ln-ln1+(i*2*ln)), point2=(lnm,2*ln+(i*2*ln)))

#mirroring the x direction pattern------------------------------------------------
if ny%2==0 :
    sketch1.Line(point1=(lnm,((ny/2)*2*ln)), point2=(2*ln+ ((nx-1)*2*ln),((ny/2)*2*ln)))
    sketch1.setAsConstruction(objectList=(sketch1.geometry[((nx+ny)*6+1+1-1)],)) #((nx+ny)*6+1+1-1) ctr+1
    #ctr=ctr+1
elif ny%2!=0:
    sketch1.Line(point1=(ln1,ln+((ny/2)*2*ln)), point2=(2*ln+ ((nx-1)*2*ln),ln+((ny/2)*2*ln)))
    sketch1.setAsConstruction(objectList=(sketch1.geometry[((nx+ny)*6+1+1-1)],)) #((nx+ny)*6+1+1-1)
    #ctr=ctr+1

objectlist1=[]
objectlistx=[]
for i in range(3,(nx*6)+1):
    objectlistx.append(sketch1.geometry[i])


objectlist1=tuple(objectlistx)
objectlist1
sketch1.copyMirror(mirrorLine=sketch1.geometry[((nx+ny)*6-1+1+1)], objectList=objectlist1)

#mirroring the y direction pattern------------------------------------------
if nx%2==0:
    sketch1.Line(point1=((nx/2)*2*ln,0), point2=((nx/2)*2*ln,(ny*2*ln)))
    sketch1.setAsConstruction(objectList=(sketch1.geometry[(1+(nx+ny)*6-1+1)+nx*6-1],))
elif nx%2!=0:
    sketch1.Line(point1=(ln+(nx/2)*2*ln,0), point2=(ln+(nx/2)*2*ln,(ny*2*ln)))
    sketch1.setAsConstruction(objectList=(sketch1.geometry[(1+(nx+ny)*6-1+1)+nx*6-1],))

objectlist2=[]
objectlisty=[]
for i in range((nx*6)+2,(nx*6)+1+ny*6):
    objectlisty.append(sketch1.geometry[i])

objectlist2=tuple(objectlisty)
objectlist2
sketch1.copyMirror(mirrorLine=sketch1.geometry[(1+(nx+ny)*6)-1+1+nx*6-1], objectList=objectlist2)


#Making the diamond inclusions inside---------------------

nh=0
nv=0

#FDiamond
pf=[[nh*ln,nv*ln-ln1],[nh*ln-lnm,nv*ln],[nh*ln,nv*ln+ln1],[nh*ln+lnm,nv*ln]]
#TDiamond
pt=[[nh*ln,nv*ln-lnm],[nh*ln,nv*ln],[nh*ln,nv*ln+lnm],[nh*ln,nv*ln]]

#function for sketching rhombus inclusions
for j in range(1,4):
    for i in range(1,nx*2):
        nh=i
        for k in range(1,ny*2):
            nv=k
            pf=[[nh*ln,nv*ln-ln1],[nh*ln-lnm,nv*ln],[nh*ln,nv*ln+ln1],[nh*ln+lnm,nv*ln]]
            pt=[[nh*ln,nv*ln-lnm],[nh*ln-ln1,nv*ln],[nh*ln,nv*ln+lnm],[nh*ln+ln1,nv*ln]]
            if((k%2!=0 and i%2!=0) or (k%2==0 and i%2==0)):
                sketch1.Line(point1=tuple(pf[j-1]), point2=tuple(pf[j]))
                if j==3:
                    sketch1.Line(point1=tuple(pf[3]), point2=tuple(pf[0]))
            else:
                #print(nh,nv)
                sketch1.Line(point1=tuple(pt[j-1]), point2=tuple(pt[j]))
                if j==3:
                    sketch1.Line(point1=tuple(pt[3]), point2=tuple(pt[0]))

AuxPatt=AuxPattM.Part(dimensionality=TWO_D_PLANAR, name=part_sketch_name, type=DEFORMABLE_BODY)
AuxPatt.BaseShell(sketch=sketch1)

##CREATE MATERIAL ----------------------------------------------------------------
AuxMaterial=AuxPattM.Material(name='Steel')
elastic_properties=(Ex,v)
density=(rho,)

AuxMaterial.Elastic(table=(elastic_properties,))
AuxMaterial.Density(table=(density,))

#CREATE SECTION-----------------------------------------------------------------
AuxSection= AuxPattM.HomogeneousSolidSection(name='rrs_section',material='Steel',thickness=0.01)

#Defining the region for section assignment------------
face_point_s=(lnm,ln1,0.0)
face_region_s=AuxPatt.faces.findAt((face_point_s,))
region_patt=(face_region_s,)

#SECTION ASSIGNMENT-------------------------------------
AuxPatt.SectionAssignment(offset=0.0,offsetType=MIDDLE_SURFACE,region=region_patt,sectionName='rrs_section')

#MESH---------------------------------------------------------------------------------------------------------------------------------------

#global seeds
AuxPatt.seedPart(size=mesh_size,deviationFactor=0.1, minSizeFactor=0.1)
AuxPatt.generateMesh()

#Create the assembly----------------------------------------------------------
AuxAssembly=AuxPattM.rootAssembly
AuxAssembly.DatumCsysByDefault(CARTESIAN)
AuxInstance=AuxAssembly.Instance(name='Plate_Instance',part=AuxPatt,dependent=ON)
