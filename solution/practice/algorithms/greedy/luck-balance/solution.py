# For maximum luck, Lena should win the most valuable K important
# matches, and lose all else.
#
# The final luck = sum(all matches) - 2 * sum(matches lost)

N, K = map(int, input().split())
A = [[], []]
for i in range(N):
  L, T = map(int, input().split())
  A[T].append(L)
print(sum(A[0] + A[1]) - 2 * sum(sorted(A[1])[:-K] if K else A[1]))
