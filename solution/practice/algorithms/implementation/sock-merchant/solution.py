# Use collections.Counter to count each type of socks. Then divide
# by 2 to find the number of pairs.

import collections
input()
counter = collections.Counter(map(int, input().split()))
print(sum(x // 2 for x in counter.values()))

