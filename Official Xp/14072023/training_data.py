import json
import os
import numpy as np
import matplotlib.pyplot as plt

#%% Folder containing the JSON files
party = '0311'
data_folder = f'MNIST-{party}'
output_folder = 'plots'

#%% Get the list of subfolders
subfolders = [subfolder for subfolder in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, subfolder))]

# Loop through the subfolders
for subfolder in subfolders:
    # Path to the JSON file
    json_file = os.path.join(data_folder, subfolder, f'{subfolder}_metrics_party{party}.json')

    # Read the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract metrics data
    rounds = []
    metrics = {}

    for item in data:
        round_no = item['round_no']
        rounds.append(round_no)

        post_train = item['post_train']
        for metric, value in post_train.items():
            if metric != 'ts':
                if metric not in metrics:
                    metrics[metric] = []
                metrics[metric].append(value)

    # Plot the metrics
    num_metrics = len(metrics)
    num_cols = 3
    num_rows = int(np.ceil(num_metrics / num_cols))

    plt.figure(figsize=(12, 4*num_rows))

    for i, (metric, values) in enumerate(metrics.items()):
        plt.subplot(num_rows, num_cols, i+1)
        plt.plot(rounds, values, marker='o')
        plt.title(metric)
        plt.xlabel('Round')
        plt.ylabel(metric)

    plt.tight_layout()

    # Save the figure
    output_file = os.path.join(output_folder, f'{subfolder}_metrics_plot.png')
    plt.savefig(output_file)
    plt.show()
