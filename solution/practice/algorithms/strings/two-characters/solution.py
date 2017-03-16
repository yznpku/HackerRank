# For each pair of lowercase letters, we filter out these
# letters from the original string, and test whether the
# new string is valid in our case.

import re
import itertools
import string
_, s = input(), input()
result = 0
for pair in itertools.combinations(string.ascii_lowercase, 2):
  t = ''.join(c for c in s if c in pair)
  if not re.search(r'(.)\1', t) and len(t) >= 2:
    result = max(result, len(t))
print(result)

