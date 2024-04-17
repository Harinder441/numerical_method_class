import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
t= np.arange(0, np.pi+0.2, 0.25)
s = np.arange(0, 2*np.pi, 0.25)
s,t = np.meshgrid(s, t)
a=1

y=np.sin(t)*np.cos(s)
x=np.cos(t)*np.cos(s)
z=2*np.sin(s)
surf = ax.plot_surface(x,y,z)
ax.set_ylim(-2,2)
ax.set_xlim(-2,2)
plt.show()
