#from sympy import *
#user inputs
#n=int(input("No. of sub interval="))

n=5
ul=0.6
ll=0
def f(x):
    return 1/(1+x**2)
def simp13(ul,ll,n):
    r=5 # for rounding off
    y=[]
    h1=(ul-ll)/n
    h=round(h1,r)
    i=ll;j=0
    print("No.      X values    Y values")
    print("-----------------------------")
    while(i<=ul):
        y.append(round(f(i),r))
        print(j,"      ",round(i,r),"      ",round(f(i),r))
        i=i+h
        j=j+1
    print("------------------------------")
    sum1=y[0]+y[-1]
    sum2=0
    sum3=0
    for j in range(1,len(y)-1):
        if(j%2==0):
            sum2=sum2 +y[j]
        else:
            sum3=sum3 +y[j]
    #Simpson formula
    y=(h/3)*(sum1+4*sum3+2*sum2)
    print("By Simpson 1/3 rule Intigration of f(x)=",y)
simp13(ul,ll,n)
