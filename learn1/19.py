def diff(arr):
    l1,l2=0,0
    for i in range(len(arr)):
        l1+=arr[i][i]
        l2+=arr[i][len(arr)-1-i]
    return abs(l1-l2)

arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

r = diff(arr)
print(r)
