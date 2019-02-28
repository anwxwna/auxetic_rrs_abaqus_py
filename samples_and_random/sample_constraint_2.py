# Creating nodes set at the edges
mdb.models['Model-1'].parts['Part-1'].Set(edges= mdb.models['Model-1'].parts['Part-1'].edges.findAt(((-0.5,0.25,0),),), name='leftUpperEdge1')
mdb.models['Model-1'].parts['Part-1'].Set(name='LeftUpperNodes1',nodes=mdb.models['Model-1'].parts['Part-1'].sets['leftUpperEdge1'].nodes)

mdb.models['Model-1'].parts['Part-1'].Set(edges= mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.5,0.25,0),),),name='RightUpperEdge1')
mdb.models['Model-1'].parts['Part-1'].Set(name='RightUpperNodes1',nodes=mdb.models['Model-1'].parts['Part-1'].sets['RightUpperEdge1'].nodes)

mdb.models['Model-1'].parts['Part-1'].Set(edges= mdb.models['Model-1'].parts['Part-1'].edges.findAt(((-0.5,-0.25,0),),),name='LeftLowerEdge1')
mdb.models['Model-1'].parts['Part-1'].Set(name='LeftLowerNodes1',nodes=mdb.models['Model-1'].parts['Part-1'].sets['LeftLowerEdge1'].nodes)

mdb.models['Model-1'].parts['Part-1'].Set(edges= mdb.models['Model-1'].parts['Part-1'].edges.findAt(((0.5,-0.25,0),),),name='RightLowerEdge1')
mdb.models['Model-1'].parts['Part-1'].Set(name='RightLowerNodes1',nodes=mdb.models['Model-1'].parts['Part-1'].sets['RightLowerEdge1'].nodes)


 # Creating individual nodes
 # Nodes at left upper region12
 a=[]
 for i in mdb.models['Model-1'].parts['Part-1'].sets['LeftUpperNodes1'].nodes:
     a=a+[(i.coordinates[1],i.label)]
 a.sort()
 nodeno1=1
 for i in a:
     mdb.models['Model-1'].parts['Part-1'].Set(name='LeftNode-'+str(nodeno1), nodes=
     mdb.models['Model-1'].parts['Part-1'].nodes[(i[1]-1):(i[1])])
     nodeno1=nodeno1+1


 # Nodes at left lower region
 b=[]
 for i in mdb.models['Model-1'].parts['Part-3']:
     b=b+[(i.coordinates[1],i.label)]

 b.sort()
 nodeno3=1
 for i in b:
     mdb.models['Model-1'].parts['Part-3'].Set(name='LeftNode-'+str(nodeno3), nodes=
     mdb.models['Model-1'].parts['Part-3'].nodes[(i[1]-1):(i[1])])
     nodeno3=nodeno3+1


 # Nodes at right upper region
 c=[]
 for i in mdb.models['Model-1'].parts['Part-2'].sets['RightUpperNodes1'].nodes:
     c=c+[(i.coordinates[1],i.label)]
 c.sort()
 nodeno2=1
 for i in c:
     mdb.models['Model-1'].parts['Part-2'].Set(name='RightNode-'+str(nodeno2), nodes=
     mdb.models['Model-1'].parts['Part-2'].nodes[(i[1]-1):(i[1])])
     nodeno2=nodeno2+1


 # Nodes at right lower region
 d=[]
 for i in mdb.models['Model-1'].parts['Part-4'].sets['RightLowerNodes1'].nodes:
     d=d+[(i.coordinates[1],i.label)]
 d.sort()
 nodeno4=1
 for i in d:
     mdb.models['Model-1'].parts['Part-4'].Set(name='RightNode-'+str(nodeno4), nodes=
     mdb.models['Model-1'].parts['Part-4'].nodes[(i[1]-1):(i[1])])
     nodeno4=nodeno4+1


 #Applying constraint equation to each node for PBC
 for num1 in range(1,nodeno1):
    leftnodename = 'Part-1-1.LeftNode-%d'%(num1)
    rightnodename = 'Part-2-1.RightNode-%d'%(num1)
    mdb.models['Model-1'].Equation(name="Constraint-%d"%(num1), terms=((1.0,leftnodename, 1), (-1.0, rightnodename, 1)))

 for num2 in range(1,nodeno2):
    leftnodename = 'Part-3-1.LeftNode-%d'%(num2)
    rightnodename = 'Part-4-1.RightNode-%d'%(num2)
    mdb.models['Model-1'].Equation(name="Constraint-%d"%(nodeno1), terms=((1.0,leftnodename, 1), (-1.0, rightnodename, 1)))
    nodeno1=nodeno1+1
