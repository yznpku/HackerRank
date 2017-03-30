# This is a rather primitive solution: for each required
# (a, b) we perform a BFS to find the minimum steps.
#
# I wonder if there's a better solution. Any help will be
# appreciated.

import collections
n = int(input())
result = [[-1] * (n - 1) for i in range(n - 1)]
for a in range(1, n + 1):
  for b in range(1, n + 1):
    moves = [(-a, -b), (-a, b), (a, -b), (a, b),
             (-b, -a), (-b, a), (b, -a), (b, a)]
    visited = [[False] * n for i in range(n)]
    q = collections.deque([((0, 0), 0)])
    visited[0][0] = True
    while q:
      x, steps = q.popleft()
      visited[x[0]][x[1]] = True
      if x == (n - 1, n - 1):
        result[a - 1][b - 1] = steps
        break
      for move in moves:
        target = (x[0] + move[0], x[1] + move[1])
        if 0 <= target[0] < n and 0 <= target[1] < n and \
           not visited[target[0]][target[1]]:
          q.append((target, steps + 1))
          visited[target[0]][target[1]] = True
for row in result:
  print(*row)
