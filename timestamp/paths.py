avg_path0007 = [] #0
avg_path0311 = [] #1

iter_path0007 = [] #2
iter_path0311 = [] #3

for i in range(1, 6):
    avg_path0007.append(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0007\FedAvg\T_mnist{}\T_mnist{}_260723system_monitor_data.csv".format(i, i))
    iter_path0007.append(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0007\IterAvg\Tmnist{}\Tmnist{}_270723system_monitor_data.csv".format(i, i))

    avg_path0311.append(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0311\FedAvg\T_mnist{}\T_mnist{}_260723system_monitor_data.csv".format(i, i))
    iter_path0311.append(r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\Official Xp\26072023\MNIST-0311\IterAvg\Tmnist{}\Tmnist{}_270723system_monitor_data.csv".format(i, i))

output_folder = r"C:\Users\Hans Herbert Schulz\Desktop\UFSC\TCC\2_gits\abschlussarbeit\timestamp"

title = ['fedavg_0007.xlsx', ' iteravg_0007.xlsx', 'fedavg_0311.xlsx', ' iteravg_0311.xlsx']