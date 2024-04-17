import functions_matrix as fm
from sklearn.metrics import confusion_matrix
#Paths
model_path = "C:\\Users\\Hans Herbert Schulz\\Desktop\\UFSC\\TCC\\2_gits\\abschlussarbeit\\testing models\\Sandbox\\updated_model.h5"
data_path  = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\testing models\Sandbox\data_party1.npz"

#Model and NPZ acquisition
my_model = fm.open_model(model_path)
x_test, x_train, y_test   = fm.open_data(data_path)

#Evaluate Model
y_classes = fm.evaluate_model(my_model, x_test)

#Generate Conf Matrix
confusion_mat = confusion_matrix(y_test, y_classes)

#Plot Matrix
fm.plot_matrix(confusion_mat)