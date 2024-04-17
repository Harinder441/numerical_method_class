from sympy import *
x=symbols("x")
#a=int(input("enter the value of a="))
def f(x):
    return log(x)
l=[]
y=log(x)
i=0.5
while (i<=0.7):
     l1=limit(f(x),x,i,"+")
     l.append(l1)
     i=i+0.1
print(l)
