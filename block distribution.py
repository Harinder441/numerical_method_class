#block problem
resd=['s','g','st']
bl=[{'s':'T','g':'F','st':'F'},{'s':'F','g':'T','st':'F'},{'s':'T','g':'T','st':'F'},{'s':'T','g':'F','st':'F'},{'s':'T','g':'F','st':'F'}]

l1=[]
for l in range (0,len(bl)):
    sum=0
    for k,v in bl[l].items():
        sum =sum +ord(bl[l][k])
    l1.append(sum)
for i in range (0,len(l1)):
    if max(l1)==l1[i]:
        print("resident will choose flat no.",i+1,bl[i])
        break
