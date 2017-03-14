# Some simple calculation of the number of spaces and hashes.

n = int(input())
for i in range(n):
  print(' ' * (n - i - 1) + '#' * (i + 1)))
