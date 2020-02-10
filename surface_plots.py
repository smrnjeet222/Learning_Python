import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.arange(-1, 1,0.02)
b = a

# b = np.array([4, 5, 6,7])

a,b = np.meshgrid(a,b)

# print(a)
# print(b)

fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2, cmap= 'coolwarm')

fig2 = plt.figure()
axes = fig2.gca(projection='3d')
axes.contour(a,b,a**2+b**2, cmap= 'rainbow')

plt.show()

