a = list(map(int, input().split()))

a = sorted(a)
max1=0
for i in set(a):
    if a.count(i)+a.count(i+1)>max1:
        max1=a.count(i)+a.count(i+1)
print(max1)


#best

'''
m=[]
for i in a:
    l=[]
    for j in a:
        if abs(i-j)<=1:
            l.append(j)
    m.append(l)

print(m)
k=[]
for i in m:
    con = True
    for x in i:
        for y in i:
            if abs(x-y)>1:
                con = False
    if con:
        k.append(i)

max=0
for i in k:
    if len(i)>max:
        max=len(i)

print(k)
print(max)
'''
