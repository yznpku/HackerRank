# It's almost identical to how we calculate the original
# Fibonacci series.

t = [0] * 20
t[0], t[1], n = map(int, input().split())
for i in range(2, n):
  t[i] = t[i - 2] + t[i - 1] * t[i - 1]
print(t[n - 1])


