a = int(input())
arr = list(map(int, input().split()))

print(sum(set(arr))/len(set(arr)))
