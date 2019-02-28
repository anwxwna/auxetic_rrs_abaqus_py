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
import cmath
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
theta_list=[15,20,25,30,35,40]

#ln1=15.0
#ln=50.0
#number of unit cells-----------------------------
nx=2      #number of unit cells x direction
ny=2         #number of unit cells in y direction

#geometry counter
ctr=1
#inc=2*ln
#Material properties-----------------------------------------------
Ex=200E9  #youngs modulus of the material used
v=0.29   #poissons ratio of the materials used
rho=7872
#Mesh Constraints
mesh_size=10E-3

#divisions
div=100.0

###------------------------------------------------------------------------------------------
###------------BEGINNING ITERATION-----------------------------------------------------------
###------------------------------------------------------------------------------------------
for iter in range(len(theta_list)):


	kx=math.pi*0.2
	ky=math.pi*0.3
	## PARAMETERS ITERATED THROUGH----------------------------------------------
	theta=theta_list[iter]

	#ln and ln1 determine the initial rotated state of the rrs of the solid piece
	ln1=math.cos(math.radians(theta))*(l-ln2*(math.cos(math.radians(theta))+math.sin(math.radians(theta))))   #length of a quarter of the unit cells
	ln=(math.cos(math.radians(theta))+math.sin(math.radians(theta)))*(l-ln2*(math.cos(math.radians(theta))+math.sin(math.radians(theta)))) + ln2



	#some commonly used relationships----------------
	ln12=ln1+ln2
	lnm=ln-ln12

	#('ln,ln1,ln12,lnm', 60.2372435695794, 45.930265910669, 47.930265910669, 12.3069776589105)

	#print('ln1,ln,ln12,lnm are',ln1,ln,ln12,lnm)
	#pattern parameter relationships------------------

	#points above the horizontal axis having the points for the edge inclusions
	pex={0:ln1,1:0,2:0,3:lnm,4:0,5:0}
	pey={0:lnm,1:0,2:0,3:ln1,4:0,5:0}
	# points along the horizontal axis
	ph=[0,lnm,ln-ln1,ln,ln+ln1,2*ln-lnm]
	pv=[0,ln1,ln-lnm,ln,ln+lnm,2*ln-ln1]

	inc=2*ln

	#Constraint equation variables
	#mux=cmath.exp(-1*kx*2*ln*1j)
	#muy=cmath.exp(-1*ky*2*ln*1j)

	####-----MAIN PROGRAM-------------------------------------------------------
	############################################################################
	##CREATE MODEL AND NAMES--------------------------------------------------------------

	fracx,wholex=math.modf(kx)
	fracy,wholey=math.modf(ky)
	model_name='rrs_pbc'+repr(theta) + '__' + repr(int(wholex))+ '_' + repr(int(fracx*div)) +'__'+repr(int(wholey))+'_'+repr(int(fracy*div))

	part_sketch_name='rrs'
	part_sketch_name_i=part_sketch_name+'_i'

	instance_name=part_sketch_name+ '_inst'
	instance_name_i=part_sketch_name_i+ '_inst'

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

	#DEFINING THE REAL AND IMAGINARY PARTS----------------------------------------------------------------------
	AuxPatt=AuxPattM.Part(dimensionality=TWO_D_PLANAR, name=part_sketch_name, type=DEFORMABLE_BODY)
	AuxPatti=AuxPattM.Part(dimensionality=TWO_D_PLANAR, name=part_sketch_name_i, type=DEFORMABLE_BODY)

	AuxPatt.BaseShell(sketch=sketch1)
	AuxPatti.BaseShell(sketch=sketch1)

	##CREATE MATERIAL -----------------------------------------------------------------------------------------------
	AuxMaterial=AuxPattM.Material(name='Steel')
	elastic_properties=(Ex,v)
	density=(rho,)
	AuxMaterial.Elastic(table=(elastic_properties,))
	AuxMaterial.Density(table=(density,))

	#CREATE SECTION-----------------------------------------------------------------
	AuxSection= AuxPattM.HomogeneousSolidSection(name='rrs_section',material='Steel',thickness=0.01)

	#Defining the regions------------
	face_point_lb=(lnm,ln1,0.0)

	face_region_lb=AuxPatt.faces.findAt((face_point_lb,))
	face_region_lb_i=AuxPatti.faces.findAt((face_point_lb,))

	#face_point_rb=(lnm+2*ln,ln1,0.0)
	#face_region_rb=AuxPatt.faces.findAt((face_point_rb,))
	#face_point_rt=(lnm+2*ln,ln1+2*ln,0.0)
	#face_region_rt=AuxPatt.faces.findAt((face_point_rt,))
	#face_point_lt=(lnm,ln1+2*ln,0.0)
	#face_region_lt=AuxPatt.faces.findAt((face_point_lt,))

	region_patt=(face_region_lb,)
	region_patt_i=(face_region_lb_i,)


	#Partioning Faces------------------------------------------------------------
	#AuxPatt.PartitionFaceByShortestPath(faces=face_region_lb,point1=((lnm,2*ln,0.0),),point2=((4*ln-lnm,2*ln,0.0),))
	#AuxPatt.PartitionFaceByShortestPath(faces=face_region_rt,point1=((2*ln,2*ln+ln1,0.0),),point2=((2*ln,4*ln-ln1,0.0),))
	#AuxPatt.PartitionFaceByShortestPath(faces=face_region_rb,point1=((2*ln,2*ln-ln1,0.0),),point2=((2*ln,ln1,0.0),))

	#SECTION ASSIGNMENT-------------------------------------
	AuxPatt.SectionAssignment(offset=0.0,offsetType=MIDDLE_SURFACE,region=region_patt,sectionName='rrs_section')
	AuxPatti.SectionAssignment(offset=0.0,offsetType=MIDDLE_SURFACE,region=region_patt_i,sectionName='rrs_section')

	#Create the assembly----------------------------------------------------------
	AuxAssembly=AuxPattM.rootAssembly
	AuxAssembly.Instance(name=instance_name,part=AuxPatt,dependent=ON)
	AuxAssembly.Instance(name=instance_name_i,part=AuxPatti,dependent=ON)



	#CREATE MESH----------------------------------------------------------------

	##REAL MESH##
	AuxPatt.setElementType(elemTypes=(ElemType(
		elemCode=CPS4R, elemLibrary=STANDARD, secondOrderAccuracy=OFF,
		hourglassControl=DEFAULT, distortionControl=DEFAULT), ElemType(
		elemCode=CPS3, elemLibrary=STANDARD)), regions=region_patt)
	#global seeds
	AuxPatt.seedPart(size=mesh_size,deviationFactor=0.1, minSizeFactor=0.1)
	AuxPatt.generateMesh()

	##IMAGINARY MESH##
	AuxPatti.setElementType(elemTypes=(ElemType(
		elemCode=CPS4R, elemLibrary=STANDARD, secondOrderAccuracy=OFF,
		hourglassControl=DEFAULT, distortionControl=DEFAULT), ElemType(
		elemCode=CPS3, elemLibrary=STANDARD)), regions=region_patt_i)
	#global seeds
	AuxPatti.seedPart(size=mesh_size,deviationFactor=0.1, minSizeFactor=0.1)
	AuxPatti.generateMesh()

	#CREATING STEP--------------------------------------------------------------
	#frequency step
	AuxPattM.FrequencyStep(limitSavedEigenvectorRegion=None, name=part_sketch_name+'_freq', numEigen=10, previous='Initial')

	###CREATING NODE SETS----------------------------------------------------------
	edges=AuxPatt.edges
	edges_i=AuxPatti.edges

	AuxNodes=AuxPatt.nodes
	AuxNodesi=AuxPatti.nodes
	w=10e-2


	def PointTraverser(nodeset):
		if nodeset[-1]=='i':
			part=AuxPatti
			inst=AuxAssembly.instances[instance_name]
		else:
			part=AuxPatt
			inst=AuxAssembly.instances[instance_name_i]

		adder={'lb':(0,0),'rb':(2*ln,0),'rt':(2*ln,2*ln),'lt':(0,2*ln)}

		a=adder[nodeset[:2]][0]
		b=adder[nodeset[:2]][1]
		for i in range(6):
			if i%3!=0:
				bpoint=(ph[i]+a,pex[i]+b,0)
				rpoint=(pey[i]+2*ln+a,pv[i]+b,0)
				tpoint=(ph[i]+a,pex[i]+2*ln+b,0)
				lpoint=(pey[i]+a,pv[i]+b,0)

				part.Set(vertices=part.vertices.findAt((bpoint,)),name='bset')
				part.Set(vertices=part.vertices.findAt((rpoint,)),name='rset')
				part.Set(vertices=part.vertices.findAt((tpoint,)),name='tset')
				part.Set(vertices=part.vertices.findAt((lpoint,)),name='lset')


				if nodeset[:2]=='lb':

					part.Set(name=nodeset+'_rset_'+repr(i),nodes=part.sets['rset'].nodes)
					part.Set(name=nodeset+'_tset_'+repr(i),nodes=part.sets['tset'].nodes)


				elif nodeset[:2]=='rb':

					part.Set(name=nodeset+'_rset_'+repr(i),nodes=part.sets['rset'].nodes)

				elif nodeset[:2]=='rt':
					part.Set(name=nodeset+'_rset_'+repr(i),nodes=part.sets['rset'].nodes)
					part.Set(name=nodeset+'_tset_'+repr(i),nodes=part.sets['tset'].nodes)

				elif nodeset[:2]=='lt':
					part.Set(name=nodeset+'_tset_'+repr(i),nodes=part.sets['tset'].nodes)

		return



	def NodeMaker(nodeset):
		nodeslr=[]
		if nodeset[-1]=='i':
			part=AuxPatti

		else:
			part=AuxPatt

		for i in part.sets[nodeset].nodes:
			nodeslr.append((i.coordinates[1],i.coordinates[0],i.label))
		nodeslr.sort()
		#print(nodeslr)
		lr_num=1
		for lr_node in nodeslr:
			part.Set(name=nodeset+repr(lr_num),nodes=part.nodes[(lr_node[2]-1):(lr_node[2])])
			lr_num=lr_num+1
		return lr_num

	PointTraverser('lb')
	PointTraverser('rb')
	PointTraverser('rt')
	PointTraverser('lt')

	PointTraverser('lbi')
	PointTraverser('rbi')
	PointTraverser('rti')
	PointTraverser('lti')

	#APPLYING CONSTRAINT EQUATIONS--------------------------------------------------
	for i in range(6):
		if i%3!=0:
			##X dir
			AuxPattM.Equation(name='Constraint-x-real_'+repr(i),terms=((-1.0,instance_name+'.rb_rset_'+repr(i),1),
																		(math.cos(kx*2*ln),instance_name+'.lb_rset_'+repr(i),1),
																		(-math.sin(kx*2*ln),instance_name_i+'.lbi_rset_'+repr(i),1)
																		))

			AuxPattM.Equation(name='Constraint-x-imag_'+repr(i),terms=((1.0,instance_name_i+'.rbi_rset_'+repr(i),1),
																		(-math.cos(kx*2*ln),instance_name_i+'.lbi_rset_'+repr(i),1),
																		(-math.sin(kx*2*ln),instance_name+'.lb_rset_'+repr(i),1)))
			##Y dir

			AuxPattM.Equation(name='Constraint-y-real_'+repr(i),terms=((-1.0,instance_name+'.lt_tset_'+repr(i),2),
																		(math.cos(ky*2*ln),instance_name+'.lb_tset_'+repr(i),2),
																		(-math.sin(ky*2*ln),instance_name_i+'.lbi_tset_'+repr(i),2)
																		))

			AuxPattM.Equation(name='Constraint-y-imag_'+repr(i),terms=((-1.0,instance_name_i+'.lti_tset_'+repr(i),2),
																		(math.cos(ky*2*ln),instance_name_i+'.lbi_tset_'+repr(i),2),
																		(math.sin(ky*2*ln),instance_name+'.lb_tset_'+repr(i),2)))
			###X+Y

			AuxPattM.Equation(name='Constraint-xd-real_'+repr(i),terms=((1.0,instance_name+'.rt_rset_'+repr(i),1),
																		(-math.cos((kx+ky)*2*ln),instance_name+'.lb_rset_'+repr(i),1),
																		(math.sin((kx+ky)*2*ln),instance_name_i+'.lbi_rset_'+repr(i),1)))

			AuxPattM.Equation(name='Constraint-xd-imag_'+repr(i),terms=((-1.0,instance_name_i+'.rti_rset_'+repr(i),1),
																		(math.cos((kx+ky)*2*ln),instance_name_i+'.lbi_rset_'+repr(i),1),
																		(math.sin((kx+ky)*2*ln),instance_name+'.lb_rset_'+repr(i),1)
																		))

			AuxPattM.Equation(name='Constraint-yd-real_'+repr(i),terms=((-1.0,instance_name+'.rt_tset_'+repr(i),2),
																		(math.cos((kx+ky)*2*ln),instance_name+'.lb_tset_'+repr(i),2),
																		(-math.sin((kx+ky)*2*ln),instance_name_i+'.lbi_tset_'+repr(i),2)
																		))

			AuxPattM.Equation(name='Constraint-yd-imag_'+repr(i),terms=((-1.0,instance_name_i+'.rti_tset_'+repr(i),2),
																		(math.cos((kx+ky)*2*ln),instance_name_i+'.lbi_tset_'+repr(i),2),
																		(math.sin((kx+ky)*2*ln),instance_name+'.lb_tset_'+repr(i),2)
																		))
	#Run Job--------------------------------------------------------------------
	job_name=model_name
	mdb.Job(name=job_name,model=model_name,type=ANALYSIS)
	mdb.jobs[job_name].submit(consistencyChecking=OFF)
	mdb.jobs[job_name].waitForCompletion()

	#READ FROM ODB FILE---------------------------------------------------------------
	Aux_path=job_name + '.odb'
	odb=session.openOdb(name=Aux_path)
	freq1=odb.steps[part_sketch_name+'_freq']
	filename='kxkyVsFreq'+str(theta) +'o.csv'

	frames=freq1.frames
	with open(filename,'a') as file:
		for f in range(len(frames)):
			freq=frames[f].frequency
			file.write('%f,'%(kx))
			file.write('%f,'%(ky))
			file.write('%f'%(freq))
			file.write('\n')
	odb.close(odb,write=TRUE)
