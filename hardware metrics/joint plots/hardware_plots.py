import os
import matplotlib.pyplot as plt

directory = r'C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\hardware metrics\IPT0311\IterAvg'

image_files = [f for f in os.listdir(directory) if f.endswith('.png')]
print(image_files)

# Create a 2x2 subplot
fig, axes = plt.subplots(2,2 , figsize=(15, 9))  # Adjust figsize as needed
plot_title = ['CPU Usage [%]', 'RAM Usage [MB]', 'Network Traffic [Mbps]']

# Load and display each image in the subplot
for i, (image_file, ax) in enumerate(zip(image_files[12:15], axes.flatten())):
    image_path = os.path.join(directory, image_file)
    image = plt.imread(image_path)
    ax.imshow(image)
    ax.set_title(f'{plot_title[i]}')
    ax.axis('off')

# Adjust layout to prevent overlap
fig.delaxes(axes[1,1])

plt.tight_layout()

# Save the figure as a PNG
plt.savefig('0311_fedSDG_xp5.png')

# Show the figure
plt.show()