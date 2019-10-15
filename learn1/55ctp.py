n = int(input())

l = [i for i in range(n+1) if i%2!=0 ]

if n%2==0:
    l = [i for i in l if (l.index(i)+1)%2!=0 ]



while len(l)!=1:
    if n%2==0:
        l = [i for i in l if (l.index(i)+1)%2!=0 ]
    

    if n%2!=0:
        l = [i for i in l if (l.index(i)+1)%2==0 ]
        if len(l)!=1:
            l = [i for i in l if (l.index(i)+1)%2!=0 ]

print(l[0])
