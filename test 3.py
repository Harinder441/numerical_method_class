#Name -Harinder Singh ,uid-192606051
from sympy import *
x=symbols('x')
def simp13(f,ul,ll,n):
    r=5 # for rounding off
    y=[]
    h1=(ul-ll)/n
    h=round(h1,r)
    i=ll;j=0
    print("No.      X values    Y values")
    print("-----------------------------")
    #calculating y0,y1,y2......  yn
    while(i<=ul):
        y.append(round(f.subs(x,i),r))
        print(j,"      ",round(i,r),"      ",round(f.subs(x,i),r))
        i=i+h
        j=j+1
    print("------------------------------")
    sum1=y[0]+y[-1]
    sum2=0 #will store y2+y4+y6....
    sum3=0 #will store y1+y3+y5.....
    for j in range(1,len(y)-1):
        if(j%2==0):
            sum2=sum2 +y[j]
        else:
            sum3=sum3 +y[j]
    #Simpson formula
    y=(h/3)*(sum1+4*sum3+2*sum2)
    print("By Simpson 1/3 rule Intigration of f(x)=",round(y,4))
#user inputs
f=1/(1+x**2)
n=6
ul=6
ll=0
simp13(f,ul,ll,n)
