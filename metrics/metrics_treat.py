import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import itertools

# Open and read the JSON file
with open('metrics_party0311.json', 'r') as file:
    data = json.load(file)

# Initialize lists to store metrics
rounds = []
eval_losses = []
eval_accs = []
eval_f1_micros = []
conf_matrices = []

# Extract metrics data
for item in data:
    round_no = item['round_no']
    rounds.append(round_no)

    post_train = item['post_train']
    eval_loss = post_train['eval:loss']
    eval_acc = post_train['eval:acc']
    eval_f1_micro = post_train['eval:f1 micro']
    eval_losses.append(eval_loss)
    eval_accs.append(eval_acc)
    eval_f1_micros.append(eval_f1_micro)

    # Extract confusion matrix data if available
    if 'confusion_matrix' in post_train:
        conf_matrix_data = post_train['confusion_matrix']
        conf_matrix = np.array(conf_matrix_data['matrix'])
        conf_matrices.append(conf_matrix)

# Plot global accuracy, loss, and F1 score
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(rounds, eval_accs, marker='o')
plt.title('Global Accuracy')
plt.xlabel('Round')
plt.ylabel('Accuracy')

plt.subplot(1, 3, 2)
plt.plot(rounds, eval_losses, marker='o')
plt.title('Loss')
plt.xlabel('Round')
plt.ylabel('Loss')

plt.subplot(1, 3, 3)
plt.plot(rounds, eval_f1_micros, marker='o')
plt.title('F1 Score (Micro)')
plt.xlabel('Round')
plt.ylabel('F1 Score')

plt.tight_layout()
plt.show()

# Plot confusion matrices
if conf_matrices:
    plt.figure(figsize=(12, 6 * len(rounds)))

    for i, conf_matrix in enumerate(conf_matrices):
        classes = np.unique(conf_matrix)
        tick_marks = np.arange(len(classes))
        plt.subplot(len(rounds), 1, i + 1)
        plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title(f'Confusion Matrix (Round {rounds[i]})')
        plt.colorbar()

        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        thresh = conf_matrix.max() / 2.
        for i, j in itertools.product(range(conf_matrix.shape[0]), range(conf_matrix.shape[1])):
            plt.text(j, i, format(conf_matrix[i, j], 'd'),
                     horizontalalignment="center",
                     color="white" if conf_matrix[i, j] > thresh else "black")

        plt.tight_layout()

    plt.show()
else:
    print("Confusion matrix data not available.")
