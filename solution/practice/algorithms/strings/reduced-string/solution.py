# We will sacrifice some performance for the pure awesomeness. Haha.

import re
s = input()
for i in range(50):
  s = re.sub(r'(.)\1', '', s)
print(s if s else 'Empty String')
