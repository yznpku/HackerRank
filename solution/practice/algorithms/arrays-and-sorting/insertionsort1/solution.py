# We first shift every element to its right until
# we hit a smaller element that x, or reach the leftmost
# of the array. Then we place x into its correct position.

n = int(input())
a = list(map(int, input().split()))
i, x = n - 2, a[n - 1]
while i >= 0 and a[i] > x:
  a[i + 1] = a[i]
  i -= 1
  print(*a)
a[i + 1] = x
print(*a)
