#user inputs
X=[1985,1987,1989,1991,1993]
Y=[40,43,48,52,57]
x=1992
print("values of x =",X)
print("Values of y=",Y)
#to construct  n!=n1multi(x-xn)
def nfunc(n,n1):
    if(n==-1):
        return 1
    elif(n==n1):
        return nfunc(n-1,n1)
    else:
        return (x-X[n])*nfunc(n-1,n1)

#to construct n1!=n multi(xn1-xn)
def dfunc(n,n1):
    if(n==-1):
        return 1
    elif(n==n1):
        return dfunc(n-1,n1)
    else:
        return (X[n1]-X[n])*dfunc(n-1,n1)
#to construct (nfunc(n,0)/dfunc(n,0))*y[0]+(nfunc(n,1)/dfunc(n,1))*y[1]#
#--------(nfunc(n,n1)/dfunc(n,n1))*y[n1]

def func(n,n1):
    if(n1==-1):
        return 0
    else:
        return ((nfunc(n,n1)/dfunc(n,n1))*Y[n1])+func(n,n1-1)
n=len(X)-1
n1=len(Y)-1
y=func(n,n1)
print("By applying langrange interpolation at x=",x,"y=",y)
