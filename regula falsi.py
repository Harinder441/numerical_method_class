import numpy as np
from sympy import *
#user input
d=int(input("enter decimal value=")) # decimal point
def f(x): # defining equation
   y=x**3+3*x-5
   return y

# chosing interval
for i in range(1,10):
   if(f(i)*f(i+1)<0):
      a=i
      b=i+1
      break
if(f(a)>0):
   c=a;a=b;b=c
x0=a;x1=b
print("interval choosen [",a,b,"]")
# ITERATIONs
i=0
lx=[0] # list for values of x
while(i<=20):
   m=(f(b)-f(a))/(b-a)
   t= a-f(a)/m
   ar=np.round(a,d)
   br=np.round(b,d)
   if(f(t)>0):
      b=t
      print("x"+str(i),i,"=",b)
      br=np.round(b,d)
      lx.append(br)
   elif(f(t)<0):
      a=t
      print("x"+str(i),"=",a)
      ar=np.round(a,d)
      lx.append(ar)
   if(lx[i]==lx[i+1]):
      print ("answer =",lx[i])
      break
   i=i+1
print("found after",i,"iteration")
#calculating error
E=np.abs(0-f(ar))
print("absolute error=",E)
# ploting graph
# equation of line segment
if(x0==a ): # setting fix point
    xf=x0
else:
    xf=x1

def l(t,x):
   m=(f(xf)-f(t))/(xf-t)
   r=m*(x-t)+f(t)
   return r
x=symbols("x")

p=plot(f(x) ,l(x0,x),l(lx[1],x),l(lx[2],x),l(lx[3],x),(x,x0,x1),title="graph showing iterations",show=False)
p[0].line_color="r"
p.show()
