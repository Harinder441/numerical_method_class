import numpy as np
from sympy import *
d=int(input("enter decimal value="))# decimal point
def f(x): # defining equation
   y=x**3+2*x**2+50*x+7
   return y

# chosing interval

x=symbols("x")
# ITERATIONs
i=0
lx=[] # list for values of x
lx.extend([x0,x1])
while(i<=20):
   if(lx[i]!=lx[i+1]):
       m=(f(x1)-f(x0))/(x1-x0)
       x2= x0-f(x0)/m
       x2r=np.round(x2,d)
       print("x",i+2,"=",x2r)
       x0=x1
       x1=x2r
       lx.append(x2r)
   else:
        print("answer =", lx[i])
        break
   i=i+1
print("found after",i,"iteration")
