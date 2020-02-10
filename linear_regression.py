import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = np.array([.1, .2, .3, .4, .5, .6, .7, .8, .9])
Y = np.array([2, 3.2, 6.8, 8.5, 8.7, 11.5, 13.1, 13.3, 16])

# X = X.values
# Y = Y.values

mu = X.mean()
std = X.std()
print(mu, std)


def hypothesis(x, theta):
    y_ = theta[0] + theta[1]*x
    return y_


def gradient(X, Y, theta):
    m = X.shape[0]
    grad = np.zeros((2,))
    for i in range(m):
        x = X[i]
        y_ = hypothesis(x, theta)
        y = Y[i]
        grad[0] += (y_ - y)
        grad[1] += (y_ - y)*x
    return grad/m


def error(X, Y, theta):
    m = X.shape[0]
    total_error = 0.0
    for i in range(m):
        y_ = hypothesis(X[i], theta)
        total_error = (y_ - Y[i])**2

    return total_error/m


def grad_descent(X, Y, lr=0.1, max_steps=1000):
    theta = np.zeros((2,))
    error_list = []
    for i in range(max_steps):
        grad = gradient(X, Y, theta)
        e = error(X, Y, theta)
        error_list.append(e)

        theta[0] = theta[0] - lr*grad[0]
        theta[1] = theta[1] - lr*grad[1]

    return theta, error_list


theta, error_list = grad_descent(X, Y)

print(theta)

y_ = hypothesis(X, theta)

# print(y_)

plt.style.use('seaborn')
plt.scatter(X, Y)
plt.plot(X,y_ ,  color='orange', label='Prediction')
plt.legend()

plt.show()
