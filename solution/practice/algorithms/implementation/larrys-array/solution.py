# A cycle of 3 element is an even permutation. (See https://en.wikipedia.org/wiki/Parity_of_a_permutation)
# Therefore, the parity of inversions is kept unchanged through any sequence of cycles.
# A sorted array has 0 inversions, so the initial array must have an even number of
# inversions to be able to sort in this way.
#
# In this challenge we use itertools.combinations to count the number of inversions. This is
# not an optimized approach but can keep the code clean.

from itertools import combinations
for case in range(int(input())):
  input()
  inversions = sum(x[0] > x[1] for x in combinations(map(int, input().split()), 2))
  print('YES' if inversions % 2 == 0 else 'NO')
