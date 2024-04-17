import numpy as np
from sympy import *
x ,c= symbols('x c ')
def h(x):
    return (x*(x-1)*(x-2))
pl = (float)(round(limit(h(x), x,0, dir="+"), 2))
print(pl)
