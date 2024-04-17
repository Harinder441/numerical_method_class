from sympy import *
#user inputs
#n=int(input("No. of sub interval="))
n=6
b=0.6
a=0
x=symbols("x")
f=exp(x)
def simp38(b,a,n):
    r=5 # for rounding off
    y=[]
    h1=(b-a)/n
    h=round(h1,r)
    i=a;j=0
    print("No.      X values    Y values")
    print("-----------------------------")
    while(i<=b+0.01):
        y.append(round(f.subs(x,i),r))
        print(j,"      ",round(i,r),"      ",round(f.subs(x,i),r))
        i=i+h
        j=j+1
    print("------------------------------")
    sum1=y[0]+y[-1]
    sum2=0
    sum3=0
    for j in range(1,len(y)-1):
        if(j%3==0):
            sum2=sum2 +y[j]
        else:
            sum3=sum3 +y[j]
    #Simpson formula
    y=(3*h/8)*(sum1+3*sum3+2*sum2)
    print("By Simpson 3/8 rule Intigration of f(x)=",y)

