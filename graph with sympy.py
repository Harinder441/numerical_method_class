from sympy import *
x,a,b=symbols("x a b")
y=cos(a*x+b)
z=y.subs({a:2,b:3})
p=plot(z,(x,-10,10),xlable="x axis",ylable="y axis", title="graph")
