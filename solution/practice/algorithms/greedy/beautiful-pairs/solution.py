# If A and B contains the same elements (in any order), we can
# have at most N beautiful pairs. And for every mismatch, the
# number of beautiful pairs will decrease by 1. We here use a 
# collections.Counter to find the number of mismatch.
#
# Since A and B have the same size, changing an element of B
# can always create one beautiful pair, except for when A and
# B are the same and we have to break a pair.

import collections
N = int(input())
A = collections.Counter(map(int, input().split()))
B = collections.Counter(map(int, input().split()))
if A == B:
  print(N - 1)
else:
  print(N - sum((A - B).values()) + 1)
