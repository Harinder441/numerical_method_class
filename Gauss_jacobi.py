def trunc(n,d):  #  defining a function for truncuation
    s=10**d
    k=int(n*s)
    return k/s
d=int(input("enter decimal value="))
import numpy as np
#user inputs
A=[[5,-2,3],[-3,9,1],[2,-1,-7]]
D=[[-1],[2],[3]]
#implementing general Form
r1,c1=np.shape(D)
X=np.zeros((r1,c1))
r,c=np.shape(A)
L=np.zeros((r1,c1))
print("Iterations..")
print("----------------")
j=1
while True:
    for i in range(r):
        sum=0
        for k in range(c):
             if k!=i:
                sum=sum+A[i][k]*X[k][0]
        L[i][0]=trunc((D[i][0]-sum)/A[i][i],d)
    print(j,L)
    if((X==L).all()==True):
       print("----------------")
       print("answer=",L)
       break
    else:
         X=np.copy(L)
    j=j+1
