import numpy as np
# user entries
X=[1,2,3,4,5,6,7,8]
Y=[1,8,27,64,125,216,343,512]
x=7.5
print("                   Difference Table")
print("__________________________________________________________")
print("X  | ",X)
print("Y  | ",Y)
#calculating difference
def difference(Y):
    L=[]
    for i in range(len(Y)-1):
        L.append(np.round(Y[i+1]-Y[i],4))
    return L
# making difference table and storing 1St value of every colon  in D0
D0=[Y[len(Y)-1]]
K=Y
i=0
while len(K)!=1:
    K=difference(K)
    print("D"+str(i+1)+"Y|",K)
    D0.append(K[len(K)-1])
    i=i+1
print("__________________________________________________________")
# calculating value of h and u
h=X[1]-X[0]
print("h=",h)
u=(x-X[-1])/h
print("u=",u)
#to construct u(u+1)...(u+(n-1))(u+n)
def ufunc(u,n):
    if n==0:
        return u
    else:
        return (u+n)*ufunc(u,(n-1))
# to construct n!
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
#To construct D0[0]+uD0[1]/1! +.....+u(u-1)...(u-(n-1))D0[n]/n!
def f2(n):
    if (n==0):
        return D0[0]
    else:
        return (ufunc(u,n-1)*D0[n])/fact(n) + f2(n-1)
print("By applying newton Backward Introploation..... ")
n1=len(D0)-1
y=f2(n1)
print("At x=",x,"y=",y)
#difference from newton forward
''' 1 u=(x-xn)/h
    2 D0 is now Dn which will contain last elements
    3 ufunc is now for u(u+1)....(u+(n-1))(u+n)
'''
