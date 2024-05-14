# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:53:11 2023

@author: jgb-hs
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#%% DataFrame Creation
dev1 = pd.read_csv('mnist_01_dev1.csv')
dev2 = pd.read_csv('mnist_01_dev2.csv')
a = list(dev1)

#%% Timestamp conversion to Elapsed Time
dev1['timestamp'] = pd.to_datetime(dev1['timestamp'])
dev2['timestamp'] = pd.to_datetime(dev1['timestamp'])

dev1['Elapsed Time'] = (dev1['timestamp'] - dev1['timestamp'].min()).dt.total_seconds()
dev2['Elapsed Time'] = (dev1['timestamp'] - dev1['timestamp'].min()).dt.total_seconds()

#%% Plot function
category = ['cpu_total', 'cpu_user', 'mem_active', 'mem_used']
names = ['[%]', 'Elapsed Time [s]', 'CPU', 'Memory']

def plot_func(category1, category2, ylabel, xlabel,  client, title):
    if client == 1:
        df = dev1
    else:
        df = dev2
        
    plt.plot(df['Elapsed Time'], df[category1], color = 'blue')
    plt.plot(df['Elapsed Time'], df[category2], color = 'orange')


    #Plot Title and Legend
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(labels = ['Total', 'Process'])
    plt.title(title)
    plt.show()

#%%PLOTS
#CPU Usage
plot_func(category[0], category[1], names[0], names[1],1, f'{names[2]} Usage Client 1')
plot_func(category[0], category[1], names[0], names[1],2, f'{names[2]} Usage Client 2')

#Memory Usage
plot_func(category[2], category[3], names[0], names[1],1, f'{names[3]} Usage Client 1')
plot_func(category[2], category[3], names[0], names[1],2, f'{names[3]} Usage Client 2')