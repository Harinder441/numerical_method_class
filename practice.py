from sympy import *
x,y,m=symbols("x y m")
def N(x,y):
    return x-y**2
def d(x,y):
    return x**2+y**2
def f(x,y):
    return N(x,y)/d(x,y)
a=float(input("x tends to"))
b=float(input("y tends to"))
if(d(a,b)!=0):
    print("limit=",f(a,b))
else:
    s1=f(x,m*(x-a)+b)
    s2=simplify(s1)
    print(s2)
    l=[]
    for i in range (-4,5):
        s3=s2.subs({m:i})
        lhl=limit(s3,x,i)
        rhl=limit(s3,x,i,"-")
        if(lhl==rhl):
            l.append(lhl)
            if(i==4):
                d=0
        else:
            print("not exist")
            d=1
            break

    if(d==0):
        print(l)
        for i in range (1,9):
            if(l[i-1]==l[i]):
                if(i==8):
                   print("need")
            else:
                print("not exist..")
                break

