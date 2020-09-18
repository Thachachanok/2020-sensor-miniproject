#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:20:45 2020

@author: ece-student
"""

import numpy as np
import pandas as pd
import ast
from astropy.time import Time
import matplotlib.pyplot as plt

file = '/home/ece-student/2020-sensor-miniproject/data.txt'

def readData(file):
    sensorData = open(file,'r').read().splitlines()
    
    dat0 = ast.literal_eval(sensorData[0])
    col = list(dat0[list(dat0.keys())[0]].keys())
    col.append('room')
    
    df = pd.DataFrame(columns=col)
    
    for dat in sensorData:
        dat_dic = a=ast.literal_eval(dat)
        temp = dat_dic[list(dat_dic.keys())[0]]
        temp2 = {}
        
        for e in temp.keys():
            if type(temp[e]) == list:
                temp2[e] = temp[e][0]
            else:
                temp2[e] = temp[e]
        
        temp2['room'] = list(dat_dic.keys())[0]
        
        df = df.append(temp2, ignore_index=True)
    return df

#####################################
############ Part 2 #################
#####################################

df = readData(file)

########## med and var of temp ###########
print('Temperature data')
print('median = '+str(np.median(df['temperature'])))
print('variance = '+str(np.std(df['temperature'])**2))
print('-----------------')

########## med and var of occup ###########
print('Occupancy data')
print('median = '+str(np.median(df['occupancy'])))
print('variance = '+str(np.std(df['occupancy'])**2))
print('-----------------')

########## Plot of probability density ##########
class1Data = df[df['room']=='class1']

quantity = ['temperature', 'occupancy', 'co2']
i=1
for q in quantity:
    plt.figure()
    plt.hist(class1Data[q], density=True, bins=20)
    plt.title('Probability density of '+q)
    plt.xlabel(q)
    plt.ylabel('Probabilty Density')
    plt.savefig('Figure'+str(i)+'.png')
    i=i+1
    
######### Time Interval ##########

time = []

for i in range (0,len(df)):
    t = Time(df['time'][i], format='isot')
    time.append(t.jd)

interval = (np.array(time[1:-1])-np.array(time[0:-2]))*24*3600
print('Time data')
print('median = '+str(np.median(interval)))
print('variance = '+str(np.std(interval)**2))
print('-----------------')
plt.figure()
plt.title('Time Interval Distribution')
plt.xlabel('Time Interval')
plt.ylabel('Probabilty Density')
plt.savefig('Figure4.png')
plt.hist(interval, density=True, bins=50)

#####################################
############ Part 3 #################
#####################################

lab1 = df[df['room']=='lab1'].reset_index()
class1 = df[df['room']=='class1'].reset_index()
office = df[df['room']=='office'].reset_index()

rooms = [lab1, class1, office]

anomaly = '/home/ece-student/2020-sensor-miniproject/anomaly.txt'
x = open(anomaly, 'w')

for room in rooms:
    std_temp = np.std(room['temperature'])
    mean_temp = np.mean(room['temperature'])
    for i in range (0,len(room)):
        if np.abs(room['temperature'][i] - mean_temp)/std_temp > 3:
            x.write(str(room.iloc[i,:])+'\n')
            x.write('\n')
