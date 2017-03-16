# We will use collections.Counter to tell the difference
# between two strings.

from collections import Counter
s1, s2 = input(), input()
c1, c2 = Counter(s1), Counter(s2)
print(sum((c1 - c2).values()) + sum((c2 - c1).values()))
