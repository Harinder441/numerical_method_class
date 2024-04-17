from sympy import *
def trunc(n,d):  #  defining a function for truncation
    s=10**d
    k=int(n*s)
    return k/s
d=int(input("enter no. of decimal places for root=")) # decimal places given by user
x=symbols('x')
#function for given equation
def f(x):
    y= x**2-4
    return y
#function for derivative of given equation
D= Derivative(f(x),x).doit()
#chosing X0
l=[]
for i in range (-10,10):
    l.append(abs(N(f(i))))
for i in range (0,20):
    if(l[i]==min(l)):
        x0=i-10
        if(D.subs({x:x0})==0.0):#check -- is f(x0) =0?
            print("f'(x0) is zero for x0=",x0)
            print("please change range")
        else:
            break
x0=6
# x0 chosen
print("intial approximation x0=",x0)

v=[] # list for approximate values
# Iterations
j=1
print("No.    Approximations      ")
print("___________________________")
while True:
    fdx0= D.subs({x:x0})
    x1=x0-(N(f(x0))/N(fdx0))
    x1r=trunc(x1,d+1)
    print(j,"    ",x1r)
    v.append(x1r)
    if(trunc(x0,d)!=trunc(x1r,d)):
        x0=x1
    else:
        print("___________________________")
        print("answer is " ,trunc(x1r,d),"\n found after",j,"iterations")
        break
    j=j+1
#ploting graph
#defining function for tangent
def t(x,x0):
    Dx0=N(D.subs({x:x0}))
    return (x-x0)*Dx0+f(x0)
p=plot(f(x),t(x,v[0]),t(x,v[1]),t(x,v[2]),t(x,v[j-1]),(x,x1r-1,x1r+1),show=False)
p[0].line_color="r"
p.show()
