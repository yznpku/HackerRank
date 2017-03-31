# Impossible situations can be found using simple math (#1).
#
# If possible, We start with [b, b-1, b-2, ..., 2, 1]. For each element, we try
# to find if we can replace it to get the desired n (#2). If not, we replace
# it with the maximum value possible (e.g. b -> k, b-1 -> k-1 and so on) (#3).

for case in range(int(input())):
  n, k, b = map(int, input().split())
  if not (1 + b) * b // 2 <= n <= (k * 2 - b + 1) * b // 2:    #1
    print(-1)
  else:
    A = list(range(b, 0, -1))
    diff = n - (1 + b) * b // 2
    for i, x in enumerate(A):
      if diff <= k - i - x:                                    #2
        A[i] += diff
        break
      diff -= k - i - x
      A[i] = k - i                                             #3
    print(*A)
