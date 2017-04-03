# * n is a winning situation if and only if any of
#   [n - 2, n - 3, n - 5] is a losing situation.
# * 0 is a losing situation.
#
# Note that functools.lru_cache can be used to write
# plain recursion instead of DP without losing performance.

import functools

@functools.lru_cache(maxsize=None)
def iswinning(n):
  if n <= 1:
    return False
  return any(not iswinning(n - i) for i in [2, 3, 5] if n - i >= 0)

for case in range(int(input())):
  print('First' if iswinning(int(input())) else 'Second')