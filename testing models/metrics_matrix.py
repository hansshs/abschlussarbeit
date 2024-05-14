import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score
from keras.models import load_model
from keras.utils import to_categorical

# Load the trained model
model = load_model(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\trained_model.h5")

# Load the data
data = np.load(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\testing models\Sandbox\data_party1.npz")
x_test = data['x_test']
x_train = data['x_train']
y_test = data['y_test']

print(len(x_test), len(x_train), len(x_test)+len(x_train))

# Evaluate the model
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)

confusion_mat = confusion_matrix(y_test, y_pred_classes)    

# Calculate Loss and Accuracy
num_classes = len(np.unique(y_test))
y_test_onehot = to_categorical(y_test, num_classes=num_classes)

loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

# Calculate precision, recall, and F1 score
precision = np.diag(confusion_mat) / np.sum(confusion_mat, axis=0)
recall = np.diag(confusion_mat) / np.sum(confusion_mat, axis=1)
f1_score_macro = f1_score(y_test, y_pred_classes, average='macro')
f1_score_micro = f1_score(y_test, y_pred_classes, average='micro')
f1_score = 2 * (precision * recall) / (precision + recall)

# Print other metrics
print(f"Loss: {loss}")
print(f"Accuracy: {accuracy}")
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1_score)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(confusion_mat, interpolation='nearest')
plt.title('Confusion Matrix Monolythic')
plt.colorbar()
tick_marks = np.arange(10)
plt.xticks(tick_marks, range(10))
plt.yticks(tick_marks, range(10))
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()