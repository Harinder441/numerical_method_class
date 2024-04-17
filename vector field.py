import matplotlib.pyplot as plt
import numpy as np

#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
t= np.linspace(0,2* np.pi, 20)
s = np.linspace(-10, 10, 20)
s,t = np.meshgrid(s, t)
a=1

y=np.sin(t)
x=np.cos(t)
plt.quiver(s,t,x,y)
plt.ylim(-1,1)
plt.xlim(-1,1)

#surf = ax.plot_surface(x,y,z)
plt.show()
