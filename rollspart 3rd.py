from sympy import *
x=symbols("x")

def f(x):
    return x**3-4*x
a=-2
b=2
if(f(a)==f(b)):
    print("3rd satisfy")
else:
    print("not equal")
