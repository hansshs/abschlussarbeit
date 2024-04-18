import functions_matrix as fm
import os

#Quando reitrando pros outros plots, mudar só nome do gráfico e FL Strategy

for model_path in fm.model_paths:

#Model and NPZ acquisition
    my_model = fm.open_model(model_path)
    title = os.path.basename(os.path.dirname(model_path))
    x_test, x_train, y_test = fm.open_data(fm.data_path)

#Evaluate Model
    y_classes = fm.evaluate_model(my_model, x_test)

#Generate Conf Matrix
    confusion_mat = fm.confusion_matrix(y_test, y_classes)
    output_path = os.path.join(fm.output_folder, f"{title}_confusion_matrix_npz_colortest.png")

# Generate Metrics and Print
    loss, accuracy = fm.loss_accuracy(y_test, x_test, my_model)
    precision, recall,f1_score = fm.other_metrics(confusion_mat, y_test, y_classes)
    fm.print_terminal(loss, accuracy, precision, recall, f1_score,title)

#Plot Matrix
    fm.plot_matrix(confusion_mat, output_path,title)