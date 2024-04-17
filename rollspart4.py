from sympy import *
x,c=symbols("x c")
def f(x):
    return (x**3-4*x)
a=-2
b=2
f1x=Derivative(f(x),x).doit()
f1c=f1x.subs({x:c})
rhs=0
c=solve(f1c-rhs)
print("c=",c[0])
if(a<c[0]<b):
    print("c lies in (a,b)")
else:
    print("not satisfy")
