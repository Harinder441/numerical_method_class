'''import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
def f(x, y):
    return (x+y)/(x-y)

x = np.linspace(-10, 10, 30)
y = np.linspace(-10, 10, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50)
plt.show()'''
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x= np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x,y = np.meshgrid(x, y)

z=x**2+y**2
z1=y/x**2


surf = ax.plot_surface(x,y, z1, linewidth=0)
#surf = ax.plot_surface(x,y, z,cmap=cm.coolwarm, linewidth=0)
#ax.set_zlim(10,40)
plt.show()
