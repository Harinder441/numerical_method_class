from sympy import *
x=symbols("x")
def f(x):
    return x**3-4*x
l1=[]
l2=[]
l3=[]
i=-2
while(i<=2):
    lhl=limit(f(x),x,i,"-")
    lhlr=round(lhl,2)
    l1.append(lhlr)
    rhl=limit(f(x),x,i,"+")
    rhlr=round(rhl,2)
    l2.append(rhlr)
    fir=round (f(x).subs({x:i}),2)
    l3.append(fir)
    i=i+0.5

print(l1)
print(l2)
print(l3)
if(l1==l2==l3):
    print("alll e")
else:
    print("not equal")
