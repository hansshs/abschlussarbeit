#This script is a remodelling of the Kaggle version with functions only
#%% Libs
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score
from keras.models import load_model
from keras.utils import to_categorical
import csv


#Se precisar alterar algo no código, basta alterar as variáveis model_paths, data_paths e output_folder. O resto se resolve


#Paths
model_paths = []
for i in range(1, 6):
    model_paths.append(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0007\FedAvg\T_mnist{}\updated_model.h5".format(i))
output_folder = r"C:\Users\Hans Herbert Schulz\Desktop\New_MAT_Plots"


data_path   = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\testing models\Sandbox\data_party3.npz"

#%%
def open_model (model_path):
    model = load_model(model_path)
    print("\nModel opened sucessfully!\n")
    return model

def open_data(data_path):
    '''
    Opens the training data within the npz file

    data_path: path for the .npz file
    '''
    data = np.load(data_path)
    x_test = data['x_test']
    x_train = data['x_train']
    y_test = data['y_test']
    
    print("\nData opened sucessfully!\n")
    print(len(x_test), len(x_train), len(x_test)+len(x_train))
    return x_test, x_train, y_test

def evaluate_model(model, x_test):
    '''
    Evaluates the trained model with the npz data

    x_test: Acquired within the 'open_data' function
    '''
    y_pred = model.predict(x_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    return y_pred_classes

def loss_accuracy(y_test, x_test, model):
    '''
    Returns Loss and Accuracy metrics

    x_test: Acquired within the 'open_data' function
    y_test: Comes from the 'open_data' function
    model: Comes from 'open_model' function
    '''
    num_classes = len(np.unique(y_test))
    y_test_onehot = to_categorical(y_test, num_classes=num_classes)
    loss, accuracy = model.evaluate(x_test, y_test_onehot, verbose=0)
    return loss, accuracy

def other_metrics(confusion_mat, y_test, y_pred_classes):
    '''
    Returns the Precision, Recall and F1 Score

    y_test: Comes from the 'open_data' function
    y_pred_classes: Comes from the 'evaluate_model' function
    confusion_mat: Comes from the 'confusion_matrix' function
    '''
    precision = np.diag(confusion_mat) / np.sum(confusion_mat, axis=0)
    recall = np.diag(confusion_mat) / np.sum(confusion_mat, axis=1)
    #f1_score_macro = f1_score(y_test, y_pred_classes, average='macro')
    #f1_score_micro = f1_score(y_test, y_pred_classes, average='micro')
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score

def print_terminal(loss, accuracy, precision, recall, f1_score, title=None):
    # Print other metrics
    filename = f"new_metrics_npz0{title}.csv"

 # Prepare data for writing
    data = {
        "Metric": ["Loss", "Accuracy", "F1 Score (global)", "Precision (global)", "Recall (global)"],
        "Value": [f"{loss:.4f}", f"{accuracy:.4f}", f"{np.mean(f1_score):.4f}", f"{np.mean(precision):.4f}", f"{np.mean(recall):.4f}"]
    }
        # Add precision and recall to the data
    for i in range(len(precision)):
        data[f"Precision class {i}"] = [f"{precision[i]:.4f}"]
        data[f"Recall class {i}"] = [f"{recall[i]:.4f}"]
        data[f"F1 Score class {i}"] = [f"{f1_score[i]:.4f}"]

   # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Metric', 'Value'])
        for metric, value in data.items():
            writer.writerow([metric, value])

    print(f"Loss {title}: {loss:.4f}")
    print(f"Accuracy{title}: {accuracy:.4f}")
    for i in range(len(precision)):
        print(f"Precision class {i}: {precision[i]:.4f}")
        print(f"Recall class {i}: {recall[i]:.4f}")
        print(f"F1 Score class {i}: {f1_score[i]:.4f}")
    print(f"F1 Score global: {np.mean(f1_score):.4f}\n\n")

def plot_matrix(confusion_mat, f1_score_metric,output_path=None, title='Confusion Matrix'):
    '''
    Plots the final Confusion Matrix
    '''
    plt.figure(figsize=(8, 6))
    plt.imshow(confusion_mat, interpolation='nearest', cmap='Blues')
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(10)
    plt.xticks(tick_marks, range(10))
    plt.yticks(tick_marks, range(10))
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    #plt.show()
      # Annotate F1 scores
    for i in range(confusion_mat.shape[0]):
        plt.text(i, i, f"{f1_score_metric[i]:.2f}", ha='center', va='center', color='white')

        # Save plot if output_path is provided
    if output_path:
        plt.savefig(output_path)
        print(f"{title} saved succesfully!")
    else:
        print(f"Error saving plot {title}")