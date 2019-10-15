a = list(map(int, input().split()))
a = a[0]
k = list(map(int, input().split()))
u = list(map(int, input().split()))

max=0
for i in k:
    for j in u:
        if i+j>=max and i+j<=a:
            max=i+j

if a<min(k)+min(u):
    max=-1

print(max)
