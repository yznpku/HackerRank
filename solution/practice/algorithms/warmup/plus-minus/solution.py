# Straightforward.

n = int(input())
arr = list(map(int, input().split()))
print(sum(x > 0 for x in arr) / n)
print(sum(x < 0 for x in arr) / n)
print(sum(x == 0 for x in arr) / n)
