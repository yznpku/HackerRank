# First we should notice that sum(|a_i - a_j|) >= max(a) - min(a).
# Left and right are equal if and only if a is sorted (in either order).
#
# When we sort an array, we are essentially doing a permutation (See
# https://en.wikipedia.org/wiki/Permutation#Permutations_in_group_theory).
# The permutation can be broken down into n-cycles and further into swaps.
# We need (n - 1) swaps for each n-cycle in the permutation. Therefore, 
# in our code we will find each of the n-cycle and sum up all of them.

def count_swaps(A):
  visited = [False] * len(A)
  def ring_gen(x):
    visited[x] = True
    i = x
    while A[i] != x:
      visited[A[i]] = True
      yield A[i]
      i = A[i]
  return sum(sum(1 for x in ring_gen(i)) for i in range(len(A)) if not visited[i])

n = int(input())
a = list(map(int, input().split()))
forward = sorted(range(n), key=lambda x: a[x])
backward = sorted(range(n), key=lambda x: a[x], reverse=True)
print(min(count_swaps(forward), count_swaps(backward)))
