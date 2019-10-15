n = int(input())
arr = list(map(int, input().split()))
l = []
if n==len(arr):
    for i in arr:
        if i<max(arr):
            l.append(i)
print(max(l))
