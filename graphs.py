import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4,1000)
y = np.linspace(-4,4,1000)
x,y =np.meshgrid(x,y)
a=1
z=(x+y)/(x-y)
ax = plt.gca()
ax.contour(x, y,z)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.show()
