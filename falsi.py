from numpy import round
from sympy import *
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
   a,b=b,a
x0=a;x1=b
print("interval choosen [",a,b,"]")
# ITERATIONs
i=0
lx=[x0] # list for values of x
while True :
   m=(f(b)-f(a))/(b-a)
   tr= a-f(a)/m
   t=round(tr,d)
   if(f(t)>0):
      b=t
      print("x"+str(i),i,"=",b)
      br=round(b,d)
      lx.append(br)
   elif(f(t)<0):
      a=t
      print("x"+str(i),"=",a)
      ar=round(a,d)
      lx.append(ar)
   else:
      pass
   if(lx[i]==lx[i+1]):
      print ("answer =",lx[i])
      break
   i=i+1
print("found after",i,"iteration")
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

p=plot(f(x),(x,x0,x1),title="graph showing iterations",show=False)
for i in range(int(len(lx)/2)):
    p1=plot(l(lx[i],x),(x,x0,x1),show=False)
    p.append(p1[0])
p[0].line_color="r"
p.show()
