import numpy as np
def matrix():
    r=int(input("enter number of rows="))
    c=int(input("enter number of column="))
    M=[]
    for i in range(r):
        a=[]
        print("enter entry of row ",i+1)
        for j in range(c):
            e=float(input())
            a.append(e)
        M.append(a)
    return(M)
def LUdeco(A):
    r,c=np.shape(A)
    L=np.zeros((r,c))
    U=np.zeros((r,c))
    for i in range(r):
        L[i][i]=1
        for j in range(c):
            sum=0
            for k in range(j):
                sum=sum+L[i][k]*U[k][j]

            if i==0:
                U[i][j]=A[i][j]
            if j<i:
               L[i][j]=(A[i][j]-sum)/U[j][j]
            sum1=0
            for k1 in range(i):
                sum1=sum1+L[i][k1]*U[k1][j]
            if j>=i:
                U[i][j]=A[i][j]-sum1
    return L,U

def Zdeco(B):
    r,c=np.shape(B)
    Z=np.zeros((r,c))
    for i in range(r):
        for j in range(c):
            sum=0.0
            for k in range(i):
                sum=sum+L[i][k]*Z[k][j]
            Z[i][j]=(B[i][j]-sum)/L[i][i]
    return(Z)
def Xdeco(Z):
    r,c=np.shape(Z)
    X=np.zeros((r,c))
    for i in range(r-1,-1,-1):
        for j in range(c):
            sum=0.0
            for k in range(i+1,r):
                sum=sum+U[i][k]*X[k][j]
            X[i][j]=(Z[i][j]-sum)/U[i][i]
    return(X)
A=[[2,1,-3],[0,2,3],[1,4,9]]
B=[[10],[18],[16]]
print("Solution A=LU")
L,U=LUdeco(A)
print("upper triangular matrix  U=\n",U)
print("Lower triangular matrix  L=\n",L)
Z=Zdeco(B)
print("By solving equation LZ=B we get Z= \n",Z)
X=Xdeco(Z)
print("By solving equation UX=Z we get X= \n",X)
