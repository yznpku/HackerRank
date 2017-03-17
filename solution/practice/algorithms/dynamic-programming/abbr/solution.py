# Denote dp[i][j] as the subproblem of a[:i] and b[:j].
# Situations where j = 0 are tricky to write. dp[i][0] is true if and only if:
# * a[:i+1] contains at least one b[0] in either case
# * a[:i+1] contains at most one uppercase b[0]
# * a[:i+1] doesn't contain any uppercase other than b[0]
# State transition:
# * if a[i] is uppercase, dp[i][j] must come from dp[i-1][j-1] when a[i] == b[j]
# * otherwise dp[i][j] can also come from dp[i-1][j]

for case in range(int(input())):
  a, b = input(), input()
  dp = [[False] * len(b) for i in range(len(a))]
  for i in range(len(a)):
    dp[i][0] = any(x.upper() == b[0] for x in a[:i+1]) \
               and sum(1 for x in a[:i+1] if x == b[0]) <= 1 \
               and not any(x.isupper() and x != b[0] for x in a[:i+1])
  for j in range(1, len(b)):
    for i in range(1, len(a)):
      if not a[i].isupper():
        dp[i][j] = dp[i - 1][j]
      if a[i].upper() == b[j]:
        dp[i][j] = dp[i][j] or dp[i - 1][j - 1]
  print('YES' if dp[-1][-1] else 'NO')
