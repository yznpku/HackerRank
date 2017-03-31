# Apparently, Mark should pick toys in ascending order of price
# until he runs out of money.

N, K = map(int, input().split())
A = sorted(map(int, input().split()))
result = 0
while K >= 0 and result < N:
  K -= A[result]
  result += 1
print(result - 1)
