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

iteration_count=1
#Parameters---------------------------------------------------------------------

ln=30.0     #length of a quarter of the unit cells
ln1=10.0
ln2=5.0
nx=3         #number of unit cells x direction
ny=3         #number of unit cells in y direction
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
#abaqus statements start here-------------------------------------------------
session.viewports['Viewport:1'].setValues(displayedObject=None)

##Create Model------------------------------------------------------------------
part_sketch_name='rrs'
model_name='rrs'+repr(iteration_count)
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
        #print(pq)
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
    for i in range(1,nx+2):
        nh=i
        for k in range(1,ny+2):
            nv=k
            pf=[[nh*ln,nv*ln-ln1],[nh*ln-lnm,nv*ln],[nh*ln,nv*ln+ln1],[nh*ln+lnm,nv*ln]]
            pt=[[nh*ln,nv*ln-lnm],[nh*ln-ln1,nv*ln],[nh*ln,nv*ln+lnm],[nh*ln+ln1,nv*ln]]
            if(i==k or (i-k)==2 or (k-i)==2):
                sketch1.Line(point1=tuple(pf[j-1]), point2=tuple(pf[j]))
                if j==3:
                    sketch1.Line(point1=tuple(pf[3]), point2=tuple(pf[0]))
            elif ((i-k)==1 or (k-i)==1):
                #print(nh,nv)
                sketch1.Line(point1=tuple(pt[j-1]), point2=tuple(pt[j]))
                if j==3:
                    sketch1.Line(point1=tuple(pt[3]), point2=tuple(pt[0]))


AuxPatt=AuxPattM.Part(dimensionality=TWO_D_PLANAR, name=part_sketch_name, type=DEFORMABLE_BODY)
AuxPatt.BaseShell(sketch=sketch1)


##Create material---------------------------------------------------------------
AuxMaterial=AuxPattM.Material(name='Steel')
elastic_properties=(Ex,v)
AuxMaterial.Elastic(table=(elastic_properties,))
#Create Section
AuxSection= AuxPattM.HomogeneousShellSection(name='rrs_section',idealization=NO_IDEALIZATION,integrationRule=SIMPSON,material='Steel',thickness=0.01)

#defining the region for section assignment
face_point_s=(lnm,ln*0.5,0.0)
face_region_s=AuxPatt.faces.findAt((face_point_s,))
region_patt=(face_region_s,)

#SectionAssignment-------------------------------------
AuxPatt.SectionAssignment(offset=0.0,offsetType=MIDDLE_SURFACE,region=region_patt,sectionName='rrs_section')

#Create the assembly----------------------------------------------------------
AuxAssembly=AuxPattM.rootAssembly
AuxInstance=AuxAssembly.Instance(name='Plate_Instance',part=AuxPatt,dependent=ON)

#Creating the STEP--------------------------------------------------------------
#static general step for displacement BC at right edge
AuxPattM.StaticStep(name='Disp_step',previous='Initial',description='Apply Displacement at right boundary',
                    nlgeom=ON)

#Create Field Output Request--------------------------------------------------
AuxPattM.fieldOutputRequests.changeKey(fromName='F-Output-1', toName='Output stresses and displacements')
AuxPattM.fieldOutputRequests['Output stresses and displacements'].setValues(variables=('S','UT'))

#BOUNDARY CONDITIONS-----------------------------------------------------------
#allnodes=AuxAssembly.nodes

#function to find midpoints of all the flat edges along the initial outer edges
def midpoints(pq,peq,nq=nx):
    midpoint_q=[]
    for i  in range(nq):
        inq=inc*i               #the increment for coordinate for each unit cell
        pq=[x+inq for x in pq]  #incrementing the unit cell
        loq=xy_dir(nq,pq,peq,i)  #the list of coordinates at each unit cell
        if nq==ny:              #if ny then reverse the contents of the loq list
            for x in range(len(loq)):
                loq[x][0].reverse()
                loq[x][1].reverse()
        flat_edges=list(loq[t] for t in [1,4]) #list containing only the flat edges
        mid_one=[[] for s in range(2)]
        for g in range(2):
            for j in range(2):
                mid_one[g].append((flat_edges[g][0][j]+flat_edges[g][1][j])/2) #calculating midpoints
            midpoint_q.append(mid_one[g])
    return midpoint_q

#putting the midpoints in a tuple for findAt function to read easily
def findAt_seq(midpoint_q):
    #print(midpoint_q)
    findat_edges=[]
    for m in range(len(midpoint_q)):
        midpoint_q[m].append(0)
        findat_edges.append((tuple(midpoint_q[m]),))
    #print('findat_edges',tuple(findat_edges))
    return tuple(findat_edges)

#shifting the midoints of y dir line from origin to the rightedge
def midpoints_shift(midpoint_q,nq):
    for m in range(len(midpoint_q)):
        midpoint_q[m][0]+=(nq)*inc   #shift the cooridanates of the y dir flat edges by inc
    #print(midpoint_q)
    return midpoint_q

midpoints_x=midpoints(ph,pex,nx)
midpoints_y=midpoints(pv,pey,ny)
fx=findAt_seq(midpoints_x)
fy=findAt_seq(midpoints_y)

x_edges_bc= AuxInstance.edges.findAt(fx)
y_edges_bc= AuxInstance.edges.findAt(fy)

x_edge_region=regionToolset.Region(edges=x_edges_bc)
y_edge_region=regionToolset.Region(edges=y_edges_bc)

#Setting displacement boundary condition
AuxPattM.DisplacementBC(name='Edge_x',createStepName='Initial',region=x_edge_region,u2=SET,u3=SET,ur1=SET,ur2=SET,ur3=SET,amplitude=SET, distributionType=UNIFORM, fieldName='',localCsys=None)
AuxPattM.DisplacementBC(name='Edge_y',createStepName='Initial',region=y_edge_region,u1=SET,u3=SET,ur1=SET,ur2=SET,ur3=SET,amplitude=SET, distributionType=UNIFORM, fieldName='',localCsys=None)

#APPLY DISPLACEMENT BOUNDARY CONDITION AT RIGHT EGDES---------------------------
midpoints_r=midpoints_shift(midpoints_y,nx)
fr=findAt_seq(midpoints_r)

r_edges_bc= AuxInstance.edges.findAt(fr)
r_edge_region=regionToolset.Region(edges=r_edges_bc)

right_disp=20

AuxPattM.DisplacementBC(name='Edge_r',createStepName='Disp_step',region=r_edge_region,u1=right_disp,amplitude=SET, distributionType=UNIFORM, fieldName='',localCsys=None)


#MESH--------------------------------------------------------------------------
#plate_face
face_point=(nx*2*ln,ny*2*ln,0.0)
plate_face=AuxPatt.faces.findAt((face_point),)
plate_region=(plate_face,)

#set element type
plate_mesh_region= plate_region
elemType1=mesh.ElemType(elemCode=S8R, elemLibrary=STANDARD)
AuxPatt.setElementType(regions=plate_mesh_region,elemTypes=(elemType1,))

#seed edges by number
#mesh_edge_x=
#mesh_edge_y=
#number of seeds
#mx=
#my=

AuxPatt.seedEdgeByNumber(edges=mesh_edge_x, number=mx)
AuxPatt.seedEdgeByNumber(edges=mesh_edge_y, number=my)

AuxPatt.generateMesh()



#RUN JOB -----------------------------------------------------------------------
job_name= 'rrs'+ repr(iteration_count)
mdb.Job(name=job_name,model='rrs displacement model',type=ANALYSIS,
        description='Simulates the displacement of the auxetic rrs pattern w displacement BC')
mdb.jobs[job_name].submit(consistencyChecking=OFF)
mdb.jobs[job_name].waitForCompletion()

##
##Post Processing---------------------------------------------------------------
##Deformed state with contours

#Aux_viewport=session.Viewport('rrs viewport')
Aux_path=job_name + '.odb'
Aux_odb_object=session.openOdb(name=Aux_path)

session.viewports['Viewport: 1'].setValues(displayedObject=Aux_odb_object)

Aux_viewport.setValues(displayedObject=an_odb_object)
Aux_viewport.odbDisplay.display.setvalues(plotState=(CONTOURS_ON_DEF,))

#REPORTING DISPLACEMENTS------------------------------------------------------

#REPORT-----------------------------------------
report_name='rrs_1'
report_path='E:/rrs/'
report_name_and_path=report name+ report_path + '.rpt'
try:
    os.makedirs(report_path)
except:
    print("Directory exixts")

session.writeFieldReport(filename=report_name_and_path, append=OFF, sortItem=''
                        odb=an_odb_object,step=0, frame=1,)
