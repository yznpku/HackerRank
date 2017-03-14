# Functions from itertools can save you from writing nested for-loops.

from itertools import combinations
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(sum(sum(pair) % k == 0 for pair in combinations(a, 2)))
