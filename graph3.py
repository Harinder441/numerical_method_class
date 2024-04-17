import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.arange(-2,2,0.1)
y = x**2
z= x**3
#l=np.tan(x)
ax = plt.gca()
ax.plot(x, y)
ax.plot(x, z)
#ax.plot(x,l)
#plt.ylim(-5, 5)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')


plt.show()
