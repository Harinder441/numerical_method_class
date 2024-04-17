from sympy import *
#user inputs
#n=int(input("No. of sub interval="))
n=6
ul=5.2
ll=4
x=symbols("x")
f=log(x)
def simp38(ul,ll,n):
    r=5 # for rounding off
    y=[]
    h1=(ul-ll)/n
    h=round(h1,r)
    i=ll;j=0
    print("No.      X values    Y values")
    print("-----------------------------")
    while(i<=ul+0.01):
        y.append(round(f.subs(x,i),r))
        print(j,"      ",round(i,r),"      ",round(f.subs(x,i),r))
        i=i+h
        j=j+1
    print("------------------------------")
    sum1=y[0]+y[-1]
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    for j in range(1,len(y)-1):
        if(j%6==0):
            sum2=sum2 +y[j]
        elif((j-1)%4==0):
            sum3=sum3+y[j]
        elif((j-3)%3==0):
            sum4=sum4+y[j]
        else:
            sum5=sum5 +y[j]
    #widdles formula
    y=(3*h/10)*(sum1+sum5+5*sum3+6*sum4+2*sum2)
    print("By Weddles rule Intigration of f(x)=",y)
simp38(ul,ll,n)
