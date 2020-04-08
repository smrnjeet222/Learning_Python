import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('./train.csv')

x = train.iloc[:, 0]
y = train.iloc[:, 1]

# Converted to numpy array
x = x.values
y = y.values

x = (x-x.mean())/x.std()


theta = np.load('./ThetaList.npy')

T0 = theta[:, 0]
T1 = theta[:, 1]

plt.ion()

for i in range(0, 60, 1):
    y_ = T1[i]*x + T0[i]
    plt.scatter(x, y)
    plt.plot(x, y_, color='red')
    plt.draw()
    plt.pause(0.1)
    plt.clf()
