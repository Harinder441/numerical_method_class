import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.linspace(0,3, 1000)

y= x**(0.5)
z= x**2


ax = plt.gca()
ax.plot(x, y)
ax.plot(x, z)
#ax.plot(x, w)
#ax.set_ylim(-5,10)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')


plt.show()
