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
#PARAMETERS---------------------------------------------------------------------
###
#Independent of iterated values--ln and ln2-------------------------------------------------------------------------
#the hinge width
ln2=2.0E-3
#edge length of a square
l=50.0E-3
## ln1 and ln will be changed as a function of theta
theta_list=[15]

#ln1=15.0
#ln=50.0
#number of unit cells-----------------------------
nx=3      #number of unit cells x direction
ny=3         #number of unit cells in y direction

#geometry counter
ctr=1
#displacement at right boundary
right_disp=20
#inc=2*ln
#Material properties-----------------------------------------------
Ex=200E9  #youngs modulus of the material used
v=0.29   #poissons ratio of the materials used
rho=7872
#Mesh Constraints
mesh_size=1



theta_poi_dict={}
#theta_poi_dict_m={}
###------------------------------------------------------------------------------------------
###------------BEGINNING ITERATION-----------------------------------------------------------
###------------------------------------------------------------------------------------------
for iter in range(len(theta_list)):
    ## PARAMETERS ITERATED THROUGH----------------------------------------------
    theta=theta_list[iter]

    #ln and ln1 determine the initial rotated state of the rrs of the solid piece
    ln1=math.cos(math.radians(theta))*(l-ln2*(math.cos(math.radians(theta))+math.sin(math.radians(theta))))   #length of a quarter of the unit cells
    ln=(math.cos(math.radians(theta))+math.sin(math.radians(theta)))*(l-ln2*(math.cos(math.radians(theta))+math.sin(math.radians(theta)))) + ln2

    print('ln1,ln are',ln1,ln)

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

    inc=2*ln
    ####-----MAIN PROGRAM-------------------------------------------------------
    ############################################################################
    ##CREATE MODEL--------------------------------------------------------------
    part_sketch_name='rrs'
    model_name='rrs'+repr(theta)
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

    #Create the assembly----------------------------------------------------------
    AuxAssembly=AuxPattM.rootAssembly
    AuxInstance=AuxAssembly.Instance(name='Plate_Instance',part=AuxPatt,dependent=ON)

    #Creating the STEP--------------------------------------------------------------
    #static general step for displacement BC at right edge
    AuxPattM.StaticStep(name='Disp_step',previous='Initial',description='Apply Displacement at right boundary',nlgeom=ON)

    #Create Field Output Request--------------------------------------------------
    AuxPattM.fieldOutputRequests.changeKey(fromName='F-Output-1', toName='Displacements')
    AuxPattM.fieldOutputRequests['Displacements'].setValues(variables=('S','UT'))

    #BOUNDARY CONDITIONS----------------------------------------------------------------------------------------------------------
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```

    #function to find midpoints of all the flat edges along the initial outer edges
    def midpoints(pq,peq,nq=nx):
        midpoint_q=[]
        for i  in range(nq):
            if i==0:
                inq=inc*i              #the increment for coordinate for each unit cell
            else:
                inq=inc
            pq=[x+inq for x in pq]  #incrementing the unit cell
            loq=xy_dir(nq,pq,peq,i)  #the list of coordinates at each unit cell
            flat_edges=list(loq[t] for t in [1,4]) #list containing only the flat edges
            mid_one=[[] for s in range(2)]
            for g in range(2):
                for j in range(2):
                    mid_one[g].append((flat_edges[g][0][j]+flat_edges[g][1][j])/2) #calculating midpoints
                midpoint_q.append(mid_one[g])
        return midpoint_q

    #midpoints for flat edges along y dir outer edges
    def midpointsy(pq,peq,nq):
        midpoint_q=[]
        for i  in range(nq):
            if i==0:
                inq=inc*i              #the increment for coordinate for each unit cell
            else:
                inq=inc
            pq=[x+inq for x in pq]  #incrementing the unit cell
            loq=xy_dir(nq,pq,peq,i)  #the list of coordinates at each unit cell
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
            findat_edges.append(((tuple(midpoint_q[m],),)))
        #print('findat_edges',tuple(findat_edges))
        return tuple(findat_edges)

    #shifting the midoints of y dir line from origin to the rightedge
    def midpoints_shift(midpoint_q,nq):
        midpointss=[]
        for m in range(len(midpoint_q)):
            midpoint_q[m][0]+=(nq)*inc   #shift the cooridanates of the y dir flat edges by inc
            midpointss.append(((tuple(midpoint_q[m],),)))
        #print(midpoint_q)
        return tuple(midpointss)

    midpoints_x=midpoints(ph,pex,nx)
    midpoints_y=midpointsy(pv,pey,ny)
    fx=findAt_seq(midpoints_x)
    fy=findAt_seq(midpoints_y)

    #Setting displacement boundary condition
    for x in range(2*nx):
        x_edges_bc= AuxInstance.edges.findAt(fx[x])
        x_edge_region=regionToolset.Region(edges=x_edges_bc)
        AuxPattM.DisplacementBC(name='Edge_x'+repr(x),createStepName='Initial',region=x_edge_region,u2=SET,amplitude=UNSET, distributionType=UNIFORM, fieldName='',localCsys=None)

    for y in range(2*ny):
        y_edges_bc= AuxInstance.edges.findAt(fy[y])
        y_edge_region=regionToolset.Region(edges=y_edges_bc)
        AuxPattM.DisplacementBC(name='Edge_y'+repr(y),createStepName='Initial',region=y_edge_region,u1=SET,amplitude=UNSET, distributionType=UNIFORM, fieldName='',localCsys=None)

    #APPLY DISPLACEMENT BOUNDARY CONDITION AT RIGHT EGDES-----------------------------------------------------------------------------------

    fr=midpoints_shift(midpoints_y,nx)

    for r in range(2*ny):
        r_edges_bc= AuxInstance.edges.findAt(fr[r])
        r_edge_region=regionToolset.Region(edges=r_edges_bc)
        AuxPattM.DisplacementBC(name='Edge_r'+repr(r),createStepName='Disp_step',region=r_edge_region,u1=right_disp,amplitude=UNSET, distributionType=UNIFORM, fieldName='',localCsys=None)

    #HISTORY OUTPUTS-----------------------------------------------------------------------------------------------------------------------------------------
    #Creating sets for measuring displacement history output -------------------------------------------------
    #--------------------------------------------------------------------------------------------------------
    def midpoints_shifty(midpoint_q,nq):
        midpointss=[]
        for m in range(len(midpoint_q)):
            midpoint_q[m][1]+=(nq)*inc   #shift the cooridanates of the y dir flat edges by inc
            midpointss.append(((tuple(midpoint_q[m],),)))
        #print(midpoint_q)
        return tuple(midpointss)     #shifting mid points of x dir line in y dir
    ft= midpoints_shifty(midpoints_x,ny)

    #HISTORY OUTPUT SETS-------------------------------------------------------------------------------------------
    AuxPattM.historyOutputRequests.changeKey(fromName='H-Output-1',toName='right_disp_output')
    for ri in range(len(fr)):
        disp_set_right=AuxInstance.edges.findAt(fr[ri])
        right_disp_point_region=regionToolset.Region(edges=disp_set_right)
        AuxPattM.HistoryOutputRequest(name='right_disp_output' + repr(ri), createStepName= 'Disp_step', variables=('U1',),frequency=1,region=right_disp_point_region,sectionPoints=DEFAULT,rebar=EXCLUDE)

    #top_disp_point_region=AuxAssembly.sets['disp_set_top']
    for to in range(len(ft)):
        disp_set_top=AuxInstance.edges.findAt(ft[to])
        top_disp_point_region=regionToolset.Region(edges=disp_set_top)
        AuxPattM.HistoryOutputRequest(name='top_disp_output' + repr(to),createStepName='Disp_step',variables=('U2',),frequency=1,region=top_disp_point_region,sectionPoints=DEFAULT,rebar=EXCLUDE)


    #MESH---------------------------------------------------------------------------------------------------------------------------------------

    #global seeds
    AuxPatt.seedPart(size=mesh_size,deviationFactor=0.1, minSizeFactor=0.1)
    AuxPatt.generateMesh()

    #RUN JOB------------------------------------------------------------------------
    job_name=model_name
    mdb.Job(name=job_name,model=model_name,type=ANALYSIS,description='Simulates the displacement of the auxetic rrs pattern w displacement BC')
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
    mdb.jobs[job_name].waitForCompletion()

    #POST PROCESSING----------------------------------------------------------------


    #Read displacement from report-------------------------------------------------
    ##READ FROM ODB FILE---------------------------------------------------------------------------------------------------------------
    Aux_path=job_name + '.odb'
    Aux_odb_object=session.openOdb(name=Aux_path)
    disp1=Aux_odb_object.steps['Disp_step']

    #print('this is the history region position',disp1.historyRegions.values()[0].position)
    #['Node PLATE_INSTANCE.2978', 'Node PLATE_INSTANCE.2979', 'Node PLATE_INSTANCE.3399', 'Node PLATE_INSTANCE.3400', 'Node PLATE_INSTANCE.28411', 'Node PLATE_INSTANCE.29064']

    dispkeys=[]
    DispData=[]
    r_u1=[]
    t_u2=[]
    for i in range(3*(4*nx)+1):    ##this range here is mesh size dependent (here for mesh size=1. for mesh size=3 it does not have 48 but 32 nodes in case of nx=4)
        dispkeys.append(disp1.historyRegions.values()[i].historyOutputs.keys())
        print(disp1.historyRegions.values()[i].historyOutputs.keys())
    for t in range(3*(4*nx)+1):
        D=disp1.historyRegions.values()[t].historyOutputs[dispkeys[t][0]]
        DispData.append(D.data)
        print(D)


    #DISPLACEMENTS AT THE RIGHT BOUNDARY AND THE TOP BOUNDARY-------------------------------------------------------------------------------
    for r in range(3*(4*nx)-2*nx,3*(4*nx)-2*nx*2,-1):
        print(r)
        r_u1.append(DispData[r][1][1]) #DispData[U1][displacement at step 1][displacement]
    for t in range(3*(4*nx),3*(4*nx)-nx*2,-1):
        print(t)
        t_u2.append(DispData[t][1][1])


    print('r_u1',r_u1)
    print('t_u2',t_u2)

    r_u1_m=np.array(r_u1).mean()
    print('mean r',r_u1_m)
    t_u2_m=np.array(t_u2).mean()
    print('mean t',t_u2_m)

    Poisson_rrs =-1*(t_u2_m/r_u1_m)
    theta_poi_dict.setdefault(theta,{})['theta']=theta
    theta_poi_dict[theta]['poissons_ratio']=Poisson_rrs

    with open('DispOutput.txt','a') as f:
        #fields=['theta','poissons_ratio']
        writer=csv.DictWriter(f,fieldnames=fields)
        writer.writeheader()
        writer.writerow(theta_poi_dict[theta])
    Aux_odb_object.close()



#Writing to file
