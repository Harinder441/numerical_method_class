from sympy import symbols
x=symbols("x")
class NI:
    def __init__(self,f,ul,ll,n):
        self.f=f
        self.ul=ul
        self.ll=ll
        self.n=n
        self.h1,self.y1=self.table()

    def table(self):
        r=5 # for rounding off
        y=[]
        h1=(self.ul-self.ll)/self.n
        h=round(h1,r)
        i=self.ll;j=0
        print("No.      X values    Y values")
        print("-----------------------------")
        while(i<=self.ul+0.01):
            y.append(round(self.f.subs(x,i),r))
            print(j,"      ",round(i,r),"      ",round(self.f.subs(x,i),r))
            i=i+h
            j=j+1
        print("------------------------------")
        return h,y
    def simp38(self):
        y=self.y1
        h=self.h1
        sum1=y[0]+y[-1]
        sum2=0
        sum3=0
        for j in range(1,len(y)-1):
            if(j%3==0):
                sum2=sum2 +y[j]
            else:
                sum3=sum3 +y[j]
        #Simpson formula
        y=(3*h/8)*(sum1+3*sum3+2*sum2)
        print("By Simpson 3/8 rule Intigration of f(x)=",y)
        return y
    def simp13(self):
        y=self.y1
        h=self.h1
        sum1=y[0]+y[-1]
        sum2=0
        sum3=0
        for j in range(1,len(y)-1):
            if(j%2==0):
                sum2=sum2 +y[j]
            else:
                sum3=sum3 +y[j]
        #Simpson formula
        y=(h/3)*(sum1+4*sum3+2*sum2)
        print("By Simpson 1/3 rule Intigration of f(x)=",y)
        return y
    def Trap(self):
        y=self.y1
        h=self.h1
        sum1=y[0]+y[-1]
        sum2=0
        for j in range(1,len(y)-1):
                sum2=sum2 +y[j]
        #trap formula
        y=(h/2)*(sum1+2*sum2)
        print("By Trapzoidal rule rule Intigration of f(x)=",y)
        return y
    def widdles(self):
        y=self.y1
        h=self.h1
        sum1=y[0]+y[-1]
        sum2=0
        sum3=0
        sum4=0
        sum5=0
        for j in range(1,len(y)-1):
            if(j%6==0):
                sum2=sum2 +y[j]
            elif((j-1)%4==0):
                sum3=sum3+y[j]
            elif((j-3)%3==0):
                sum4=sum4+y[j]
            else:
                sum5=sum5 +y[j]
        #widdles formula
        y=(3*h/10)*(sum1+sum5+5*sum3+6*sum4+2*sum2)
        print("By Weddles rule Intigration of f(x)=",y)
        return y


