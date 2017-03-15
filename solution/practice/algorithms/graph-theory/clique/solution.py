# See https://en.wikipedia.org/wiki/Tur%C3%A1n_graph for the formulae we used here.
# We first use the approximation (as given in the challege hint) to get started,
# then we increment the result until the exact condition is met.

import math
def exact(n, k):
  return (n * n - (n % k) * math.ceil(n / k) ** 2 - (k - n % k) * math.floor(n / k) ** 2) / 2
for case in range(int(input())):
  N, M = map(int, input().split())
  k = math.ceil(N * N / (N * N - 2 * M))
  while M > exact(N, k):
    k += 1
  print(k) 
