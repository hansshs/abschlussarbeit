# Abschluss Arbeit (Bachelor Thesis)

## Code Descriptions

### Main

- `data_processing.py`: Plots the information received from `pid_data_acq.py`.
- `network_acq.py`: Acquire the network benchmark metrics such as bandwidth, jitter and others. DISCLAIMER: It is not working propperly.
- `pid_data_acq.py`: Acquire the necessary monitoring data such as CPU usage, network traffic and memory usage.

### /Official Xp/14072023

- `training_data.py`: Plots the results acquired trough the training json exported file.
- `pc_data.py`: Updated version of `data_processing.py`. Plots the hardware usage troughout the training.

### /testing models

- `metrics_matrix.py` [Outdated]: Plots the confusion matrix and gives the overall value of the main metrics (Accuracy, Loss and F1).
- `/Sandbox/ functions_matrix.py`: Library containing functions to open model, data, evaluate and plot the confusion matrix.
- `/Sandbox/ main_matrices.py`: Main script running the created `fm` library.

Obs:

    0311: npz0, npz3(tmnist2), npz4
    0007: npz1, npz2, npz3(tmnist1)

## Updates

Last updated on 18/04/2024
