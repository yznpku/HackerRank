# To maximize the number, we want as many '5' as possible.
# By listing some n and their solution, we find out that
# the number of '3' can only be chosen from 0, 5 and 10, and
# is dependent on (N mod 3).

for case in range(int(input())):
  N = int(input())
  n_3 = [0, 10, 5][N % 3]
  if n_3 >= 0 and N - n_3 >= 0:
    print('5' * (N - n_3) + '3' * n_3)
  else:
    print(-1)
