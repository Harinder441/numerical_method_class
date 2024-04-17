#LU decomposition,Harinder singh ,uid -192606051
from numpy import shape,zeros
#user inputs
A=[[2,3,1,5],[6,13,5,19],[2,19,10,23],[4,10,11,31]]
#function to Solve LU=A
def LUdeco(A):
    r,c=shape(A)
    L=zeros((r,c))
    U=zeros((r,c))
    for i in range(r):
        L[i][i]=1
        for j in range(c):
            if i==0:
                U[i][j]=A[i][j]
            suml=0
            for kl in range(j):
                suml=suml+L[i][kl]*U[kl][j]
            if i>j:
                L[i][j]=(A[i][j]-suml)/U[j][j]
            sumu=0
            for ku in range(i):
                sumu=sumu+L[i][ku]*U[ku][j]
            if j>=i:
                U[i][j]=A[i][j]-sumu
    return L,U
L,U=LUdeco(A)
print("upper triangular matrix  U=\n",U)
print("Lower triangular matrix  L=\n",L)
