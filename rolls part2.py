from sympy import *
x=symbols("x")

def f(x):
    return x**3-4*x
d=Derivative(f(x),x).doit()

i=-1.9
while(i<2):
    D=d.subs({x:i})
    if(D==oo):
        print("2nd not")
        break
    else:
        print("derivative exit  at",i)

    i=i+0.5
print("2nd satisfy")
