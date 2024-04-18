# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:48:04 2023

@author: jgb-hs
"""
#%% Libs
import pandas as pd
import matplotlib.pyplot as plt
import os

#Se for mudar algo, olhar somente em data_folder, output_folder, data do xp, cor gráfico


#%% Opening 
# Folder containing the CSV files
data_folder = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0311\FedAvg"

# Output folder for saving the plots
output_folder = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\hardware metrics\IPT0311\FedAvg"

# Get the list of folders (T_mnist1, T_mnist2, etc.)
subfolders = [subfolder for subfolder in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, subfolder))]
print(subfolders)
#%% Loop through the subfolders
for subfolder in subfolders:
    # Path to the CSV file
    csv_file = os.path.join(data_folder, subfolder, f'{subfolder}_260723system_monitor_data.csv')

    # Read the CSV file
    df1 = pd.read_csv(csv_file)
    df1 = df1.iloc[1:]
    ctg     = list(df1.columns)[1:] #Categories
    colors  = ['#179c7d', '#33b8ca', '#1f82c0','#f29400', 'r', 'g'] # [green, blue, dark blue, orange]
    contrast_colors = ['#FF5733', '#FFC300', '#C70039', '#900C3F', '#581845', '#00FF7F']

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Plot and save the images
    for i, category in enumerate(ctg):
        fig, ax = plt.subplots()
        ax.plot(df1['ElapsedSeconds'], df1[category], color=contrast_colors[i], lw=1.5)
        ax.set_xlabel('Elapsed Time [s]')
        ax.set_title(category)
        if i == 0:
            ax.set_ylabel('Usage [%]')
        elif (1<= i <=3):
            ax.set_ylabel('Usage [MB]')
        else:
            ax.set_ylabel('Usage [Mbps]')

        plt.savefig(os.path.join(output_folder, f'{subfolder}_{category}.png'))
        plt.close()
