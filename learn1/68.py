k = list(map(int, input().split()))
k = k[1]
a = list(map(int, input().split()))

ways=0
for i in range(len(a)):
    for j in range(len(a)):
        if i<j and (a[i]+a[j])%k==0:
            ways+=1

print(ways)
