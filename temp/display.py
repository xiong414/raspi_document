import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__=='__main__':
    raw_data = []
    with open('./record/20210514.txt', 'r')as f:
        reader = csv.reader(f)
        for row in reader:
            raw_data.append(row)
    data = np.array(raw_data)
    temp_data = data[:, 1].astype(float)
    hum_data = data[:, 2].astype(float)
    plt.plot(range(len(temp_data)), temp_data, 'r-')
    plt.plot(range(len(hum_data)), hum_data, 'b-')
    plt.show()