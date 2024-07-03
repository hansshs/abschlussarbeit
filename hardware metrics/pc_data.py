# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:48:04 2023

@author: jgb-hs
"""
#%% Libs
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sb

#Se for mudar algo, olhar somente em data_folder, output_folder, data do xp, cor gráfico
#Quando mudar os parties, mudar as cores


#%% Opening 
# Folder containing the CSV files
data_folder = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0311\FedAvg"

# Output folder for saving the plots
#output_folder = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\hardware metrics\IPT0311\FedAvg"
output_folder = r"C:\Users\Hans Herbert Schulz\Desktop\Plots pro PPT"

# Get the list of folders (T_mnist1, T_mnist2, etc.)
subfolders = [subfolder for subfolder in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, subfolder))]
print(subfolders)
#%% Loop through the subfolders
for subfolder in subfolders:
    # Path to the CSV file
    csv_file = os.path.join(data_folder, subfolder, f'{subfolder}_260723system_monitor_data.csv') #As vezes tem que mudar aqui também

    # Read the CSV file
    df1 = pd.read_csv(csv_file)
    df1 = df1.iloc[1:]
    ctg     = list(df1.columns)[1:] #Categories

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    #Plot Presets
    #contrast_colors = sb.color_palette("Reds", 3*len(ctg))[5:] #FOR IPT-0007
    contrast_colors = sb.color_palette("Blues", 2*len(ctg))[3:] #FOR IPT-0311
    contrast_colors = ['#148c70', '#106d57', '#0b4e3e', '#148c70', '#106d57', '#0b4e3e']
    #sb.set_style("darkgrid")
    
    # Plot and save the images
    for i, category in enumerate(ctg):
        fig, ax = plt.subplots()
        ax.plot(df1['ElapsedSeconds'], df1[category], color=contrast_colors[i], lw=1.5)
        ax.set_xlabel('Elapsed Time [s]',fontsize=12)
        ax.set_title(category, fontsize=12, fontweight='bold')
        
        if i == 0:
            ax.set_ylabel('Usage [%]', fontsize=12)
        elif (1<= i <=3):
            ax.set_ylabel('Usage [MB]', fontsize=12)
        else:
            ax.set_ylabel('Traffic [Mbps]', fontsize=12)
        
        plt.grid(True, which='both', linestyle='--')
        plt.savefig(os.path.join(output_folder, f'FedAvg_0311_{subfolder}_{category}.png'))
        plt.close()
