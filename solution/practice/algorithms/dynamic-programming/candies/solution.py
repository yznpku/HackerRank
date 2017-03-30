# The constraint on candy[i] exists when EITHER rating[i - 1] < rating[i]
# OR rating[i] > rating[i + 1]. We can calculate candy[i] for the subproblem
# with only rating[i - 1] < rating[i] in one pass (and save it to 'forward').
# Similarly we can solve the other subproblem (rating[i] > rating[i + 1]).
# The final candy[i] is the larger one of these subproblems value.

N = int(input())
rating = list(int(input()) for i in range(N))
forward, backward = [1] * N, [1] * N
for i in range(1, N):
  if rating[i] > rating[i - 1]:
    forward[i] = forward[i - 1] + 1
  if rating[N - i - 1] > rating[N - i]:
    backward[N - i - 1] = backward[N - i] + 1
print(sum(max(forward[i], backward[i]) for i in range(N)))
