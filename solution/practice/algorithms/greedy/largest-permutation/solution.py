# We take the greedy approach: for each element, we swap it
# to the largest element possible (e.g. swap N to the 0th place,
# N - 1 to the 1st place, N - 2 to the 2nd place and so on).
#
# We should take good care of the situation where the desired element
# is already in place. (#1)

N, K = map(int, input().split())
A = list(map(int, input().split()))
index = [0] * (N + 1)
for i, x in enumerate(A):
  index[x] = i
i = 0
while i < K and i < N:
  if A[i] == N - i:                                        #1
    K += 1
  else:
    A[index[N - i]], index[A[i]] = A[i], index[N - i]
    A[i], index[N - i] = N - i, i
  i += 1
print(*A)
