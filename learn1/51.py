from itertools import product

km = list(map(int, input().split()))
k= km[0]
m= km[1]

n=[]
for i in range(k):
    ni = list(map(int, input().split()))
    n.append(ni[1::])

m1=0
for i in list(product(*n)):
    l=0
    for j in i:
        l+=j**2
    if l%m>m1:
        m1=l%m

print(m1)
