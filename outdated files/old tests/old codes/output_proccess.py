import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#%% DataFrame Creation
dev1 = pd.read_csv('resource_usage_dev1.csv')
dev2 = pd.read_csv('resource_usage_dev2.csv')

a = list(dev1)
for i in range (len(a)):
    print(a[i], '\n')

def plot_func(category, ylabel, xlabel, title, device):
    if device == 1:
        plt.plot(dev1['Timestamp'], dev1[category], color = 'blue')
    else:
        plt.plot(dev2['Timestamp'], dev2[category], color = 'green')
    
    #plt.plot(dev1['Timestamp'], dev2[category], color = 'orange')

    #Select Time interval
    num_ticks = 25  # Adjust the number of ticks as needed
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
    plt.xticks(rotation='30')

    #Plot Title and Legend
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.title(title)
    plt.show()

for i in range (len(a)):
    plot_func(a[i+2], 'Kilobytes', 'Timestamp', a[i+2], 1)
    plot_func(a[i+2], 'Kilobytes', 'Timestamp', a[i+2], 2)
