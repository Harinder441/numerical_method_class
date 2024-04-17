def trunc(n,d):  #  defining a function for truncuation
    s=10**d
    k=int(n*s)
    return k/s
d=int(input("enter no. of decimal places for root=")) # decimal places given by user
# coffcients from user
a1=float(input("enter a1="));b1=float(input("enter b1="));c1=float(input("enter c1="));d1=float(input("enter d1="))
a2=float(input("enter a2="));b2=float(input("enter b2="));c2=float(input("enter c2="));d2=float(input("enter d2="))
a3=float(input("enter a3="));b3=float(input("enter b3="));c3=float(input("enter c3="));d3=float(input("enter d3="))
#intial approximation
x0=y0=z0=0
#iterations
i=1
while True:
    x1=(d1-y0*b1-z0*c1)/a1
    y1=(d2-x0*a2-z0*c2)/b2
    z1=(d3-x0*a3-y0*b3)/c3
    x1r=trunc(x1,d); y1r=trunc(y1,d);z1r=trunc(z1,d)
    print(i,x1r,y1r,z1r)
    x0r=trunc(x0,d); y0r=trunc(y0,d);z0r=trunc(z0,d)
    if((x1r!=x0r) or (y1r!=y0r)  or  (z1r!=z0r) ):
        x0=x1;y0=y1;z0=z1
    else:
        print("answer is x=",x1r,"y=",y1r,"z=",z1r,"\n found after",i,"iterations")
        break
    i=i+1
