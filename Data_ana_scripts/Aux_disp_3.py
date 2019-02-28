# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:01:36 2018

@author: anwch
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from ast import literal_eval
from mpl_toolkits.mplot3d import Axes3D
import csv

filename='C:\\Users\\anwch\\Documents\\IITK\\auxetic\\NumVsThetaVsDisp_t.csv'



def cleaner():
    list_of_rows=[]
    list_of_rows1=[]
    data_dict={}

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
            list_of_rows.append(r)
        list_of_rows1=[x for x in list_of_rows if x]
        
        
        for ind,row in enumerate(list_of_rows1):
            for i,r in enumerate(row):
                disps=[]
                
                if isinstance(literal_eval(r),float)== True:
                    
                    if literal_eval(r)==1.0:
                        num=literal_eval(row[i+1])
                        #putting the initial locations
                        locs=[literal_eval(x) for x in list_of_rows1[ind-1] ]
                        data_dict.setdefault(num,{})['iniloc']= locs
                        
                    
                    for t in range(i):
                        disps.append(literal_eval(row[t]))
                        data_dict[num].setdefault('thetaVsDisp',{})[literal_eval(r)]=disps
        
        return data_dict

data_dict=cleaner()
#print(data_dict)

        #iniloc is list of tuples
        #thetavsdsip is a dictionary

def GetDfFromDict(data_dict):    
    col_inds=[]
    df=pd.DataFrame()
    for t in data_dict.keys():
        
        for u in data_dict[t].keys():
            for ii,y in enumerate(data_dict[t]['iniloc']):
                col_inds.append((t,y))
            
            if isinstance(data_dict[t][u],dict):
                df1=pd.DataFrame.from_dict(data_dict[t][u],orient='index')
                df1=df1.transpose()
                df1.index=pd.MultiIndex.from_tuples([(t, a) for a in df1.index])
                df=df.append(df1.dropna())
    
    
    
    for ind in df.columns :
        df[[repr(ind)+'x',repr(ind)+'y']]=df[ind].apply(pd.Series)
        df=df.drop(ind,1)
    return df, col_inds

df,col_inds=GetDfFromDict(data_dict)

colsy=[y for y in df.columns if y[-1]=='y']
#df.loc[4].plot(y=colsy[60:89],use_index=True)

print(df.loc[2][::-1])

#fig=plt.figure(figsize=(7,7))
#ax=fig.add_axes([0,0,1,1])
#
#n=4
#color=iter(cm.rainbow(np.linspace(0,1,n)))
#c=next(color)
#for i in range(n):
#    ax.plot(df.loc[4][colsy[0:10]])

#plt.xlabel('locations')
#plt.ylabel('displacements')
#plt.legend(loc='upper left', bbox_to_anchor=(1, 1))


