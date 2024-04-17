'''import numpy as np

import matplotlib.pyplot as plt
plt.axes(projection = 'polar')
# creating an array containing the
# radian values
rads = np.arange(0, (2 * np.pi), 0.01)
# plotting the circle
for rad in rads:
    r=np.cos(rad)
    plt.polar(rad, r, 'g.')
# display the Polar plot
plt.show()'''
from typing import Any, Union

import numpy as np

import matplotlib.pyplot as plt

plt.axes(projection='polar')
# creating an array containing the
# radian values
rads = np.arange(0,  2*(np.pi), 0.001)
# plotting the circle
for rad in rads:
    r= np.abs(1+2*np.cos(rad))
    plt.polar(rad, r, 'g.')
# plt.polar(rad, r2, 'g.')
# display the Polar plot
plt.show()
