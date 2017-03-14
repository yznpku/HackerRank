# We notice that each consecutive of 01010...10 can be eliminated
# independently by flipping every other 0 from the second one.
# Therefore we only have to find how many zeros there are in each segment.

import re
n, B = int(input()), input()
count = 0
for match in re.finditer(r'0((10)+)', B):
  count += (len(match.group(1)) + 2) // 4
print(count)
