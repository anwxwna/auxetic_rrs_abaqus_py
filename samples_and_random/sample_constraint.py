   mdb.models[modelName].parts['RefPoint1'].Set(name='SetRefPoint1',
   referencePoints=(mdb.models[modelName].parts['RefPoint1'].referencePoints[1], ))

   mdb.models[modelName].parts['RefPoint2'].Set(name='SetRefPoint2',
   referencePoints=(mdb.models[modelName].parts['RefPoint2'].referencePoints[1], ))
   mdb.models[modelName].rootAssembly.regenerate()

   #node sets
   #left wall
   a=[]
   for i in mdb.models[modelName].parts[partName].sets['sL'].nodes:
       a=a+[(i.coordinates[1],i.label)]
   a.sort()
   rep=1
   for i in a:
       mdb.models[modelName].parts[partName].Set(name='Node-'+str(rep), nodes=
           mdb.models[modelName].parts[partName].nodes[(i[1]-1):(i[1])])
       rep=rep+2

   #right wall
   a=[]
   for i in mdb.models[modelName].parts[partName].sets['sR'].nodes:
       a=a+[(i.coordinates[1],i.label)]
   a.sort()
   rep=2
   for i in a:
       mdb.models[modelName].parts[partName].Set(name='Node-'+str(rep), nodes=
           mdb.models[modelName].parts[partName].nodes[(i[1]-1):(i[1])])
       rep=rep+2
   LenAV=len(a)

   #bottom wall
   a=[]
   for i in mdb.models[modelName].parts[partName].sets['BOTTOM'].nodes:
       a=a+[(i.coordinates[0],i.label)]
   a.sort()
   rep=2*LenAV+1
   for i in a:
       mdb.models[modelName].parts[partName].Set(name='Node-'+str(rep), nodes=
           mdb.models[modelName].parts[partName].nodes[(i[1]-1):(i[1])])
       rep=rep+2

   #top wall
   a=[]
   for i in mdb.models[modelName].parts[partName].sets['TOP'].nodes:
       a=a+[(i.coordinates[0],i.label)]
   a.sort()
   rep=2*LenAV+2
   for i in a:
       mdb.models[modelName].parts[partName].Set(name='Node-'+str(rep), nodes=
           mdb.models[modelName].parts[partName].nodes[(i[1]-1):(i[1])])
       rep=rep+2
   LenAH=len(a)

   #constraints

   rep=1
   for i in range(0,LenAH):
       mdb.models[modelName].Equation(name='Constraint-x-'+str(i+1),
           terms=((1.0, instName+'.Node-'+str(rep), 1),(-1.0, instName+'.Node-'+str(rep+1), 1),
           (1.0, 'RefPoint1-1.SetRefPoint1', 1),(0, 'RefPoint1-1.SetRefPoint1', 1)))
       rep=rep+2

   rep=1
   for i in range(0,LenAH):
       mdb.models[modelName].Equation(name='Constraint-y-'+str(i+1),
           terms=((1.0, instName+'.Node-'+str(rep), 2),(-1.0, instName+'.Node-'+str(rep+1), 2),
           (1.0, 'RefPoint1-1.SetRefPoint1', 2),(0, 'RefPoint1-1.SetRefPoint1', 2)))
       rep=rep+2
   val=1
   test=mdb.models[modelName].parts[partName].vertices.findAt((0,0,0),)
   if test==None:
       val=0
   time.sleep(1)



   rep=2*LenAH+1+2*val
   for i in range(LenAH,LenAV+LenAH-val):
       mdb.models[modelName].Equation(name='Constraint-x-'+str(i+1),
           terms=((1.0, instName+'.Node-'+str(rep), 1),(-1.0, instName+'.Node-'+str(rep+1), 1),
           (1.0, 'RefPoint1-2.SetRefPoint2', 1),(0, 'RefPoint1-2.SetRefPoint2', 1)))
       rep=rep+2
       j=i+1


   rep=2*LenAH+1+2*val
   for i in range(LenAH,LenAV+LenAH-val):
       mdb.models[modelName].Equation(name='Constraint-y-'+str(i+1),
           terms=((1.0, instName+'.Node-'+str(rep), 2),(-1.0, instName+'.Node-'+str(rep+1), 2),
           (1.0, 'RefPoint1-2.SetRefPoint2', 2),(0, 'RefPoint1-2.SetRefPoint2', 2)))
       rep=rep+2
