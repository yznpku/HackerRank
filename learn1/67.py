a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = b[0]
m = b[1]

ways = 0

for i in range(len(a)-m+1):
    if sum(a[i:i+m])==d:
        ways+=1
print(ways)
