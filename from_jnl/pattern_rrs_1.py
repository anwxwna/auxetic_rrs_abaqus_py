#X dir (2-nx*6)
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
        sketch1.Line(point1=(0, ln1+(i*2*ln)), point2=(0,ln12+(i*2*ln)))
        sketch1.Line(point1=(0,ln12+(i*2*ln)), point2=(ln1,ln+(i*2*ln)))
        sketch1.Line(point1=(ln1,ln+(i*2*ln)), point2=(0,ln+ln1+(i*2*ln)))
        sketch1.Line(point1=(0,ln+ln1+(i*2*ln)), point2=(0,ln+ln12+(i*2*ln)))
        sketch1.Line(point1=(0,ln+ln12+(i*2*ln)), point2=(lnm,2*ln+(i*2*ln)))
    else:
        sketch1.Line(point1=(0, ln1+(i*2*ln)), point2=(lnm,0+(i*2*ln)))
        sketch1.Line(point1=(0, ln1+(i*2*ln)), point2=(0,ln12+(i*2*ln)))
        sketch1.Line(point1=(0,ln12+(i*2*ln)), point2=(ln1,ln+(i*2*ln)))
        sketch1.Line(point1=(ln1,ln+(i*2*ln)), point2=(0,ln+ln1+(i*2*ln)))
        sketch1.Line(point1=(0,ln+ln1+(i*2*ln)), point2=(0,ln+ln12+(i*2*ln)))
        sketch1.Line(point1=(0,2*ln-lnm+(i*2*ln)), point2=(lnm,2*ln+(i*2*ln)))

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

#--------------------------------------------------------------------
## Making the diamond inclusions inside
##
nh=0
nv=0

#FDiamond
pf=[[nh*ln,nv*ln-ln1],[nh*ln-lnm,nv*ln],[nh*ln,nv*ln+ln1],[nh*ln+lnm,nv*ln]]
#TDiamond
pt=[[nh*ln,nv*ln-lnm],[nh*ln,nv*ln],[nh*ln,nv*ln+lnm],[nh*ln,nv*ln]]

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
