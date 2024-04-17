from sympy import *
#user inputs
#n=int(input("No. of sub interval="))
n=6
ul=6
ll=0
def f(x):
    return 1/(sqrt(1+x**2+x**4))
def simp13(ul,ll,n):
    r=5 # for rounding off
    y=[]
    h1=(ul-ll)/n
    h=round(h1,r)
    i=ll;j=0
    print("No.      X values    Y values")
    print("-----------------------------")
    while(i<=ul+0.01):
        y.append(round(f(i),r))
        print(j,"      ",round(i,r),"      ",round(f(i),r))
        i=i+h
        j=j+1
    print("------------------------------")
    sum1=y[0]+y[-1]
    sum2=0
    for j in range(1,len(y)-1):
            sum2=sum2 +y[j]
    #Simpson formula
    y=(h/2)*(sum1+2*sum2)
    print("By Trapzoidal rule rule Intigration of f(x)=",y)
simp13(ul,ll,n)
