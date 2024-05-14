# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:16:43 2023

@author: jgb-hs
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
#%% Opening File
df_sys = pd.read_csv('csv/mnist6_05072023_system_monitor_data.csv')
df_sys = df_sys.iloc[1:]

output_dir = 'C:/Users/jgb-hs/Desktop/Bachelor Thesis updated/bachelor-thesis/figs'

#%% Plotting Configs
ctg     = list(df_sys.columns)[1:] #Categories
colors  = ['#179c7d', '#33b8ca', '#1f82c0','#f29400', 'r', 'g'] # [green, blue, dark blue, orange]

for i in range(len(ctg)):
    fig, ax = plt.subplots()
    ax.plot(df_sys['ElapsedSeconds'], df_sys[ctg[i]], color = colors[i])
    ax.set_xlabel('Elapsed Time [s]')
    ax.set_title(ctg[i])
    if (i == 0):
        ax.set_ylabel('Usage [%]')
    else:
        ax.set_ylabel('Usage [MB]')
    
    #plt.show()
    plt.savefig(os.path.join(output_dir, f'plot_{ctg[i]}_i.png'))
    plt.close()
    
#%% Plotting the Network against each other for only 15 seconds

df_sys_subset = df_sys[:60]
plt.plot(df_sys_subset['ElapsedSeconds'], df_sys_subset['Network Receive Traffic (Mbps)'], color = 'blue')
plt.plot(df_sys_subset['ElapsedSeconds'], df_sys_subset['Network Send Traffic (Mbps)'], 'r--')
plt.show()