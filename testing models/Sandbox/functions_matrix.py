#This script is a remodelling of the Kaggle version with functions only
#%% Libs
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score
from keras.models import load_model
from keras.utils import to_categorical


#Se precisar alterar algo no código, basta alterar as variáveis model_paths, data_paths e output_folder. O resto se resolve


#Paths
model_paths = []
for i in range(1, 6):
    model_paths.append(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0311\IterAvg\Tmnist{}\updated_model.h5".format(i))
output_folder = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\testing models\Confusion Matrix Plots\IPT0007\IterAvg"


data_path   = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\testing models\Sandbox\data_party2.npz"

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
    filename = f"metrics_npz0_{title}.txt"
    with open(filename, "w") as file:
        # Print other metrics to the file
        file.write(f"Loss {title}: {loss:.4f}\n")
        file.write(f"Accuracy {title}: {accuracy:.4f}\n")
        file.write(f"Precision {title}: {precision[0]:.4f}\n")
        file.write(f"Recall {title}: {recall[0]:.4f}\n")
        file.write(f"F1 Score {title}: {f1_score[0]:.4f}\n")

    print(f"Loss {title}: {loss:.4f}")
    print(f"Accuracy{title}: {accuracy:.4f}")
    print(f"Precision {title}: {precision[0]:.4f}")
    print(f"Recall {title}: {recall[0]:.4f}")
    print(f"F1 Score {title}: {f1_score[0]:.4f}")

def plot_matrix(confusion_mat, output_path=None, title='Confusion Matrix'):
    '''
    Plots the final Confusion Matrix
    '''
    plt.figure(figsize=(8, 6))
    plt.imshow(confusion_mat, interpolation='nearest', cmap='Greens')
    plt.title(f"Confusion Matrix FedSDG {title}")
    plt.colorbar()
    tick_marks = np.arange(10)
    plt.xticks(tick_marks, range(10))
    plt.yticks(tick_marks, range(10))
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    #plt.show()

        # Save plot if output_path is provided
    if output_path:
        plt.savefig(output_path)
        print(f"{title} saved succesfully!")
    else:
        print(f"Error saving plot {title}")