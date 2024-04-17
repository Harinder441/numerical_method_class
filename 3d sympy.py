def f(x,y):
    return y/x**2
from sympy import *
from sympy.plotting import plot3d # for 3D plotting
x,y=symbols('x y')
p=plot3d(f(x,y),show=False,title='Plot Surface in 3D',xlabel='x axis',ylabel='y axis',)#zlim=(-50,50)#for 3D plotting
p.show()
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-10,10,100)
Y = np.linspace(-10,10,100)
x, y = np.meshgrid(X,Y)
z=f(x,y)
levels = []
for i in range (-5,5):
    levels.append(i)
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

c = plt.contour(x, y, z, levels, colors='k')#color for lines of levels(k is for black)
plt.clabel(c)#clabel is for labelling the levels
#c_filled = plt.contourf(x, y, z, levels)

plt.title('Level curves at the given height')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
