# There are 3 situations that we should print 'YES':
# * The string is valid by itself (e.g. 'aaabbbccc')
# * The string is a valid string plus a new character (e.g. 'aaabbbcccd')
# * The string is a valid string plus an existing character (e.g. 'aaaabbbccc')
# And we will leave it to collections.Counter to do its magic.

from collections import Counter
c = Counter(Counter(input()).values())
if len(c) == 1:
  print('YES')
elif len(c) == 2 and c[1] == 1:
  print('YES')
elif len(c) == 2 and max(c.keys()) - min(c.keys()) == 1 and c[max(c.keys())] == 1:
  print('YES')
else:
  print('NO')
