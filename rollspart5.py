from sympy import *
x=symbols("x")
a=-2
b=2
c=2*sqrt(3)/3
def f(x):
    return(x**3-4*x)
f1x=Derivative(f(x),x).doit()
f1c=f1x.subs({x:c})
y=f1c*(x-c)+f(c)
p=plot(f(x),y,(x,a,b))
#4 condition of langranfe therpfg
