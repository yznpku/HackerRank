# This problem is solved with greedy method.
# We start from the left of the line. Put the first transmitter as right as possible,
# while still covering the leftmost house. Then we remove the houses it covers, and repeat the process
# until all houses are covered.
#
# Time complexity: O(n)

n, k = map(int, input().split())
x = sorted(list(set(list(map(int, input().split())))))
n = len(x)

count, first_uncovered = 0, 0
while first_uncovered < n:
  i = first_uncovered
  while i < n and x[i] - x[first_uncovered] <= k:
    i += 1
  while first_uncovered < n and x[first_uncovered] - x[i - 1] <= k:
    first_uncovered += 1
  count += 1
print(count) 
