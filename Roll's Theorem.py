from sympy import *
import numpy as np
x ,c= symbols('x c ')
def h(x):
    return (x-3)**4*(x-5)**3
print("Enter values for interval ")
a = float(input("enter the value for a ="))
b = float(input("enter the value for b ="))
print("$$$$Checking first condition$$$$")
i = a
l1 = []
l2 = []
l3 = []
while (i <= b):
    pl = round((float)(limit(h(x), x, i, dir="+")),2)
    nl = round((float)(limit(h(x), x, i, dir="-")),2)
    c_f =round(h(i), 2)
    l1.append(pl)
    l2.append(nl)
    l3.append(c_f)
    i = i + 0.2
    i = np.round(i, 2)
print("RHL=",l1)
print("LHL=",l2)
print("function values=",l3)
if (l1 == l2 == l3):
    r=1
    print("Function is continous in [", a ,",",  b , "]\n ---Hence first condition is satisfied---"  )
else:
    r=0
    print("Function is not continous in [", a ,",",  b , "]\n ---Hence first condition is not satisfied---"  )
#part 2
print("$$$Checking second condition$$$")
i=a+0.1
d=diff(h(x),x).doit()
while(i<b):
   val_diff=round(d.subs({x:i}),2)

   if(val_diff != zoo):

       if(i==(b-0.1)):
           s=1
           print("---Function is differntiable in interval (",a,b,")")
           print("---2nd condition satisfied---")
   else:
       s=0
       print("Function is not differentiable at",i)
       print("---Hence 2nd condition is not satisfied---")
       break
   i=i+0.1
   i=np.round(i,1)
print("$$ checking third condition $$")
if(h(a)==h(b)):
    print("---Third condition satisfied ,h(a)=h(b)=",h(a),"---")
    t=1
else:
    print("--Third condition not satisfied--")
    t=0

# part 3
if(r+s+t==3):
    print("Hence all conditions are satisfied. ")
    print("$$$Then finding c$$$")
    r=Derivative(h(c),c).doit()
    expr=r
    s=solve(expr)

    c=[]
    sl=len(s)
    for i in range (0,sl):
        if (a<s[i]<b):
              c.append(s[i])
    print("values of c is/are =",c)
    print("$$$ ploting graph$$$")
    h1=Derivative(h(x),x).doit()
    y1=h(c[0])

    p=plot(h(x),y1,(x,a,b),show=False,legend=True )
    p[0].line_color='b'
    p[1].line_color='r'
    p.show()
else:
    print("---Roll's theorem cannot be aplied as all conditions are not satiesfied---")
