# Just have to notice that the sum of 4 is sum of 5 minus the left out one.

a = list(map(int, input().split()))
print(sum(a) - max(a), sum(a) - min(a))
