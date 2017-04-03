# Note that only picking the lowest value or the highest
# value for each index is sufficient for this problem.
# Therefore we define two arrays 'low' and 'high', keeping
# track of the max value possible for subarray [0, i).
# 'low' array only picks 1 for i, while 'high' only picks
# B[i] for i.

for case in range(int(input())):
  N, B = int(input()), list(map(int, input().split()))
  low, high = [0] * N, [0] * N
  for i in range(1, N):
    low[i] = max(low[i - 1], high[i - 1] + B[i - 1] - 1)
    high[i] = max(low[i - 1] + B[i] - 1, high[i - 1] + abs(B[i] - B[i - 1]))
  print(max(low[-1], high[-1]))