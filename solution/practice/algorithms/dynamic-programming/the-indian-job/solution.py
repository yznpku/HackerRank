# This is a balanced partition problem (which can be solved in O(N*S)
# where S is the sum of the array).
#
# We make an array 'possible' to record all possible sums for any 
# subarray. We then use it to find if there exists a subarray
# whose sum falls in [S / 2, G].

for case in range(int(input())):
  N, G = map(int, input().split())
  A = list(map(int, input().split()))
  total = sum(A)
  possible = [True] + [False] * total
  
  for x in A:
    for i in range(total, -1, -1):
      if possible[i]:
        possible[i + x] = True
        
  for i in range((total + 1) // 2, min(total, G) + 1):
    if possible[i]:
      print('YES')
      break
  else:
    print('NO')
