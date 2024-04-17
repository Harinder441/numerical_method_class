#xlogx=1.2
'''import numpy as np
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
#calculating error
E=np.abs(0-f(ar))
print("absolute error=",E)'''

#y=x**4-x-10
'''import numpy as np
d=5 # decimal point
def f(x):
   y=x**4-x-10
   return y
for i in range(1,10):
   if((f(i)>0 and f(i+1)<0) or (f(i)<0 and f(i+1)>0)):
      a=i
      b=i+1
      break
if(f(a)>0):
   c=a;a=b;b=c
print(a,b)
i=1
while(i<=20):
   t=(a+b)/2
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
print("found after",i,"iteration")
#calculating error
E=np.abs(0-f(ar))
print("absolute error=",E)'''



import numpy as np
d=3 # decimal point
def f(x):
   y=x*3-np.cos(x)-1
   return y
for i in range(0,10):
   if((f(i)>0 and f(i+1)<0) or (f(i)<0 and f(i+1)>0)):
      a=i
      b=i+1
      break
if(f(a)>0):
   c=a;a=b;b=c
print(a,b)
i=1
while(i<=20):
   t=(a+b)/2
   ar=np.round(a,d)
   br=np.round(b,d)
   if(f(t)>0):
      b=t
      print("x",i,"=",b)
      br=np.round(b,d)
   elif(f(t)<0):
      a=t
      print("x",i,"=",a)
      ar=np.round(a,d)
   if(br==ar):
      print ("answer =",ar)
      break
   i=i+1
print("found after",i,"iteration")
#calculating error
E=np.abs(0-f(ar))
print("absolute error=",E)
