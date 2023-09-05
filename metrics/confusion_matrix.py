import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Load the JSON data
# Replace 'path_to_json_file' with the actual path to your JSON file
import json
with open('metrics_party0311.json', 'r') as file:
    data = json.load(file)

# Extract true labels and predicted classes
true_labels = []
predicted_classes = []
for entry in data:
    true_labels.extend(entry['true_labels'])
    predicted_classes.extend(entry['predicted_classes'])

# Create confusion matrix
cm = confusion_matrix(true_labels, predicted_classes)

# Plot confusion matrix
classes = np.unique(true_labels)
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)

plt.xlabel("Predicted label")
plt.ylabel("True label")

for i in range(len(classes)):
    for j in range(len(classes)):
        plt.text(j, i, str(cm[i, j]), ha="center", va="center", color="white" if cm[i, j] > cm.max() / 2 else "black")

plt.show()
