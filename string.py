'''t="harinder"
print(id(t))
s="singh"
n=t+s
print(id(n))
l=[1,2,3]
print("l",id(l))
r=[5,6,7]
print(id(r))

w=l+r
print(id(l+r))
print(n[::2])
sp=" "
m=(n+sp)*5
print(m)'''
#no. of char in each words and total word in string
n="working with python is fun where do you live"
words=1
s=""
for i in n:
    s=s+i
    if (i.isspace()):
        words=words+1
        print("no. of char. in ",s ,"is",len(s)-1)
        s=""
print("no. of char. in ",s ,"is",len(s))
print("Total no. of words is",words,"no. of charctar is",len(n))
'''n="working with python is fun where do you live"
l=n.split()

l1=" * "
print(l1.join(l))
'''

