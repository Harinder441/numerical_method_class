from sympy import *
x=symbols("x")
y=x**2
d=Derivative(y,x,1).doit()
print(d)
