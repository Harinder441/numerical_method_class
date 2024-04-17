'''x=int(input("enter value for x ="))
if(x==0):
    print("sunday")
else:
    if(x==1):
          print("monday")
    else:
        if(x==2):
            print("tuesday")

        else:
          print("not")'''
#elif ladder statement
'''i=1
while(i<3):
    a=int(input("enter value of angle="))
    if(0<a<90):
        print("acute angle")
    elif(a==90):
        print("Right angle")
    elif(90<a<180):
        print("obtuse angle")
    elif(a==180):
        print(("straight line"))
    elif(180<a<360):
        print("reflex ")
    else:
        print("invalid angle")
    i=i+1'''
#list adresses
'''l=[10,20,[30,10]]
print(id(l[0]))
print(id(l[1]))
print(id(l[2][0]))
print(id(l[2][1]))
l[2][0]=l[2][0]-10
print(l)
print(id(l[2][0]))
'''
#Calculate the sum 1/1 + 1/2 + 1/3 + 1/4 + ----------+ 1/ N
'''def ser(n):
    return(1/n)
N=int(input("enter the value for N="))
i=1
sum=0
while(i<=N):
    sum=sum+ser(i)
    i=i+1
print("sum of series for N=",N,"is",sum)'''

#To find the absolute value of an integer.
'''a=int(input("enter any integer="))
print("absolute value of integer is", abs(a))
'''
#Enter 100 integers into an array and sort them in an ascending order.
'''import random as rd
import numpy as np
A=[]

for i  in range (100):
   r=rd.randint(1,1000)
   print(r)
   A.append(r)
print(A)
A.sort()
print(A)'''
import numpy as np
d=5 # decimal point
def f(x):
   y=x*np.log10(x)-1.2
   return y
for i in range(1,5):
   if((f(i)>0 and f(i+1)<0) or (f(i)<0 and f(i+1)>0)):
      a=i
      b=i+1
      break
if(f(a)>0):
   c=a;a=b;b=c
print(a,b)
i=0
while(i<=20):
   t=(a+b)/2
   tr=np.round(t,d)
   ar=np.round(a,d)
   br=np.round(b,d)
   if(f(t)>0):
      b=t
      print("b",b)
      br=np.round(b,d)
   elif(f(t)<0):
      a=t
      print("a",a)
      ar=np.round(a,d)
   if(br==ar):
      print ("answer =",ar)
      break
   i=i+1
# calculating error
E=np.abs(0-f(ar))
print("absolute error=",E)
