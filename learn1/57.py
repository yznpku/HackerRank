a=list(map(int, input().split()))
n=a[0]
m=a[1]

a1=list(map(int, input().split()))
a2=list(map(int, input().split()))

def facto(a):
    l = []
    for i in range(1, a+1):
        if a%i==0:
            l.append(i)
    return l

c = 0
for i in a2:
    if(set(a1).issubset(set(facto(i)))):
        c+=1

print(c)
