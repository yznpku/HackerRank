# According to the linearity of expectation, E(V) = E(sum(v_i)) = sum(E(v_i)).
#
# To calculate E(v_i), see http://cs.stackexchange.com/questions/1076/how-to-approach-vertical-sticks-challenge/1114#1114
# for an excellent explanation.

import collections

for case in range(int(input())):
  N = int(input())
  counter = collections.Counter(map(int, input().split()))
  result, k = 0, N
  for i in sorted(counter.keys()):
    result += counter[i] * (N + 1) / (k + 1)
    k -= counter[i]
  print('%.2f' % result)
