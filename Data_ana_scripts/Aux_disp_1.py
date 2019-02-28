# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 17:31:31 2018

@author: anwch
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename='C:\\Users\\anwch\\Documents\\IITK\\auxetic\\DispOutputWNum.txt'
cols=['number', 'theta', 'pr']
df=pd.read_csv(filename,names=cols)

theta_list=np.arange(1,45.5,0.5).tolist()
number=[2,3,4,5]
num_list=[num for num in number for y in range(len(theta_list))]

theta_list_1=[t for r in range(len(number)) for t in theta_list]
hier=pd.MultiIndex.from_arrays([num_list,theta_list_1])
print(df)


#print(df.iloc[0:89]['theta'])
fig= plt.figure(figsize=(7,7))
ax=fig.add_axes([0,0,1,1])

ax.plot(df[df['number']== 2]['theta'],df[df['number']== 2]['pr'],'b',label='n=2')
ax.plot(df[df['number']== 3]['theta'],df[df['number']== 3]['pr'],'r',label='n=3')
ax.plot(df[df['number']== 4]['theta'],df[df['number']== 4]['pr'],'g',label='n=4')
ax.plot(df[df['number']== 5]['theta'],df[df['number']== 5]['pr'],'y',label='n=5')

ax.set_xlabel('Theta')
ax.set_ylabel('Poisson')
ax.legend()
fig.savefig("NumVsThetaVsPr.png")

