
# Define the paths to your PNG files
#image_names = ['T_mnist1_confusion_matrix_npz1.png', 'T_mnist2_confusion_matrix_npz1.png', 'T_mnist3_confusion_matrix_npz2.png',
#               'T_mnist4_confusion_matrix_npz2.png', 'T_mnist5_confusion_matrix_npz3.png']
import os
import matplotlib.pyplot as plt

# Define the directory containing your PNG files
#directory = r'C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\testing models\Confusion Matrix Plots\IPT0007\IterAvg'
directory = r'C:\Users\Hans Herbert Schulz\Desktop\New_MAT_Plots\FedSDG'

# List all PNG files in the directory
image_files = [f for f in os.listdir(directory) if f.endswith('.png')]
print(image_files)

# Create a 2x2 subplot
fig, axes = plt.subplots(2,2 , figsize=(12, 8))  # Adjust figsize as needed

# Load and display each image in the subplot
for i, (image_file, ax) in enumerate(zip(image_files[1:5], axes.flatten())):
    image_path = os.path.join(directory, image_file)
    image = plt.imread(image_path)
    ax.imshow(image)
    ax.set_title(f'MNIST Experiment {i+2}')
    ax.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the figure as a PNG
plt.savefig('fedsdg_subplot_figure.png')

# Show the figure
plt.show()

