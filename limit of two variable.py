
from sympy import *

x,y,m =symbols('x y m',positive =True)
def N(x,y):
    return x-y
def D(x,y):
    return (x**2+y**2)**(0.5)
def f(x,y):
    return N(x,y)/D(x,y)

print("f(x,y):",f(x,y))
a=int(input("x tends to"))
b=int(input("y tends to"))
if(D(a,b)!=0):
    print("limit of f(x,y) when (x,y) tends to (",a,b,") is",f(a,b))
else:
    print("$$checking limit in different paths$$")
    print("path chosen....",m*(x-a)+b)
    s1=f(x,m*(x-a)+b)
    f1=simplify(s1)
    l=[]
    for i in range (-4,5):
        f2=f1.subs({m:i})
        l1=limit(f2,x,a).doit()
        l2=limit(f2,x,a,dir="-").doit()
        if(l1==l2):
             l.append(l1)
             if(i==4):
                 d=0
        else:
            print("limit does not exist in path y=",i*(x-a)+b)
            d=1
            break
    if(d==0):
         print("List of limits of f(x,y) at different values of m",l)
         for i in range (1,9):
              if(l[i-1]==l[i]):
                  if(i==8):
                       print("Need further test")
              else:
                  print("limit does not exist")
                  break

