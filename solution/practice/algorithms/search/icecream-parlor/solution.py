# In this problem, we want to check if (m - x) exists for each x in the list.
# Since duplicates only matter if they are exactly half of m, we can use a set
# to speed up the lookup process.
#
# Time complexity: O(n log n)

for case in range(int(input())):
  m, n = int(input()), int(input())
  c = list(map(int, input().split()))
  half_price = sorted([i + 1 for i, x in enumerate(c) if x * 2 == m])
  if len(half_price) >= 2:
    print(half_price[0], half_price[1])
  else:
    s = set(c)
    for x in s:
      if m - x in s:
        print(*sorted((c.index(x) + 1, c.index(m - x) + 1)))
        break 
