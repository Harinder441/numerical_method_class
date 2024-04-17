def trunc(n,d):  #  defining a function for truncuation
    s=10**d
    k=int(n*s)
    return k/s
d=3
import numpy as np
A=np.array([[5,-2,3],[-3,9,1],[2,-1,-7]])
print("A=",A)
b=np.array([-1,2,3])
print("b=",b)
x=np.array([0,0,0])
print("Let initial guess is:",x)
D=np.diag(A)
R=A-np.diagflat(D)
i=1
while(i>=1):
    x1=(b-np.dot(R,x))/D
    x1[0]=trunc(x1[0],d+1)
    x1[1]=trunc(x1[1],d+1)
    x1[2]=trunc(x1[2],d+1)
    print("After Iteration",i,",x1=",x1)

    if(trunc(x[0],d)==trunc(x1[0],d) and trunc(x[1],d)==trunc(x1[1],d) and trunc(x[2],d)==trunc(x[2],d)):
        break
    else:
        x=x1
        i=i+1

print("Solution:",x1)
