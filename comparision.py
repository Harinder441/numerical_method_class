from Numerical_Integration import NI
from sympy import log,symbols,sqrt
import numpy as np
x=symbols("x")
f= 1/(sqrt(1+x**2+x**4))
A=NI(f,6,0,6)
A.Trap()
A.simp38()
A.simp13()
A.widdles()
