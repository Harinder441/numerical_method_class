from sympy import *
x=symbols('x  ')
s4=exp(x)/x
s5=exp(-x)/x
s6=x/(1+x)
s7=(x**2)*sin(1/x)
l1=limit(s4,x,oo)
l2=limit(s5,x,oo)
l3=limit(s6,x,oo)
l4=limit(s7,x,oo)
print("limit of function s4 when x tends to infinity is ",l1)
print("limit of function s5 when x tends to  infinity is ",l2)
print("limit of function s6  when x tends to  infinity  is ",l3)
print("limit of function s7  when x tends to  infinity  is ",l4)
p=plot(s4,(x,-10,10),xlable="x axis",ylable="y axis", title="graph of s4 ")
p1=plot(s5,(x,-10,10),xlable="x axis",ylable="y axis", title="graph of s5 ",ylim=[-10,10])
p2=plot(s6,(x,-10,10),xlable="x axis",ylable="y axis", title="graph of s6 ",ylim=[-10,10])
#p3=plot(s7,(x,-10,10),xlable="x axis",ylable="y axis", title="graph of s7 ",ylim=[-10,10])
