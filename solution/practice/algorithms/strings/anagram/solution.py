# The rearrangement is only possible when both strings have
# equal lengths. We will then use collections.Counter to tell
# the actual difference between the two strings.

from collections import Counter
for case in range(int(input())):
  s = input()
  if len(s) % 2:
    print(-1)
  else:
    c = Counter(s[:len(s)//2]) - Counter(s[len(s)//2:])
    print(sum(x for x in c.values() if x > 0))

