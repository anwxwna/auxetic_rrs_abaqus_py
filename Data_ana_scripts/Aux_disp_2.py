# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:13:22 2018

@author: anwch
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval
from mpl_toolkits.mplot3d import Axes3D

filename='E:\\Temp\\timeloct_1.csv'
df=pd.read_csv(filename,names=[0,1,2,3,4,5,6,7,8,9,10,11,'time'])
names=[0,1,2,3,4,5,6,7,8,9,10,11,'time']

newn=['loc'+repr(names[i]) for i in range(12) ]
newn.append('time')
df.columns=newn
df.drop(df.index[:1],inplace=True)
for ind in newn:
    df[ind]=[literal_eval(x) for x in df[ind]]
    if ind!= 'time':
        df[[ind+'x',ind+'y']]=df[ind].apply(pd.Series)

newn.remove('time')
df.drop(newn, inplace=True,axis=1)
newnx=[i+'x'for i in newn]
newny=[i+'y'for i in newn]

##The right boundary
filenamer='E:\\Temp\\timelocr_1.csv'
dfr=pd.read_csv(filenamer,names=[0,1,2,3,4,5,6,7,8,9,10,11,'time'])
namesr=[0,1,2,3,4,5,6,7,8,9,10,11,'time']

newnr=['loc'+repr(namesr[i]) for i in range(12) ]
newnr.append('time')
dfr.columns=newnr
dfr.drop(dfr.index[:1],inplace=True)
for ind in newnr:
    dfr[ind]=[literal_eval(x) for x in dfr[ind]]
    if ind!= 'time':
        dfr[[ind+'x',ind+'y']]=dfr[ind].apply(pd.Series)

newnr.remove('time')
dfr.drop(newnr, inplace=True,axis=1)
newnrx=[i+'x'for i in newnr]
newnry=[i+'y'for i in newnr]

coods=["(167.0, 200.0)","(165.0, 200.0)","(135.0, 200.0)","(133.0, 200.0)","(67.0, 200.0)","(65.0, 200.0)","(35.0, 200.0)","(33.0, 200.0)","(166.0, 200.0)","(134.0, 200.0)","(66.0, 200.0)","(34.0, 200.0)"]
coods=[literal_eval(x) for x in coods]
coodsx=[i[0] for i in coods]
#coodsx=pd.Series(coodsx).values.reshape(1,12)
#top5=df.loc[[5],newny].tolist()
#print(df.loc[[5],newny])


##PLOTTING
#df.plot(x='time',y=newnrx)
fig=plt.figure(figsize=(8,8))
ax= fig.add_axes([0,0,1,1])
ax.plot(df['time'],df[newny])

#ax.plot(coodsx,df.loc[[50],newny].values.reshape(12,1))
#x=df[newny]
#y=dfr[newnrx]
#X,Y=np.meshgrid(x,y)
#Z=df['time']

#ax1=fig.add_subplot(111,projection='3d')
#ax1.plot_surface(X,Y,Z)

