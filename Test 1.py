#Roots finding with Secant Method ,uid-192606051,Harinder singh
#user inputs
def f(x):
    return x**3+x-1
x0=0
x1=1
d=3 #decimal value given
#Iterations
if(f(x0)>0):#seting f(x0)<0 and f(x1)>0
    x0,x1=x1,x0
L=[x0,x1] #this list will contain all approximations
print("Interval given",L)
print("No.    Approximation")
print("______________________")
i=1
while True:
    m=(f(x1)-f(x0))/(x1-x0)
    x2= x0-f(x0)/m #applying secant formula
    x2r=round(x2,d)
    L.append(x2r)
    print(i,"   ",x2r)
    # checking sign of f(x2) and replacing with same sign ordinate
    if(f(x2)>0):
        x0=x2
    else:
        x1=x2
    #checking weather two consecutive approximation are equal or not
    if(L[i]==L[i+1]):
        print("______________________")
        print("Answer is =",L[i+1])
        print("Found after "+str(i-1)+" iterations.")
        break
    i=i+1
