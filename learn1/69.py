a= list(map(int, input().split()))

d = {}
max=0
j=0
for i in set(a):
    if a.count(i)>max:
        max=a.count(i)
        j=i

print(j)
