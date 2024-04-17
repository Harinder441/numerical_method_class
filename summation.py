#Calculate the sum 1/1 + 1/2 + 1/3 + 1/4 + ----------+ 1/ N
def ser(n):
    return(1/n)
N=int(input("enter the value for N="))
i=1
sum=0
while(i<=N):
    sum=sum+ser(i)
    i=i+1
print("sum of series for N=",N,"is",sum)
