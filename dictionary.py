d={1:'A',2:'B',3:'C'}
print(d.pop(2))
print(d)
d.popitem()
print(d)

print(d.get(4,'not thier'))
s={1,2,3,3,'s','t',1.5,(3,2)}
print(s)
t={}
print(type(t))
print(s)
S=set()
print(S)
S=set("hellomyname")
print(S)
S=set([1,2,3,45,5])
print(S)
sq={n**2 for n in range(10)}
print(sq)
R={1,2,3,4,56,7}
print(R)
R.add(5)
print(R)
R.update({1,2,3,45,6})
print(R)
R.remove(5)
print(R)
#R.remove(78) # gve error
R.discard(78)
print(R)
print(567 in  R)
print(567 not in  R)
R={1,2,3,4,56,7}
Z={3,56}
print("subset or not")
print(Z==R)
print(Z<R)
print(Z.issubset(R))
print(Z>R)
print(Z<=R)
print(Z>=R)
print("diff",R.difference(Z),R-Z)
print("diff",R.intersection(Z),R&Z)
print("diff",R.union(Z),R|Z)
