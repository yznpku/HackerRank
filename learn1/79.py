a = list(map(int, input().split()))
a=a[1]
b = list(map(int, input().split()))

n=0
for i in b:
    if i<=0:
        n+=1
if n>=a:
    print("NO")
else:print("YES")
