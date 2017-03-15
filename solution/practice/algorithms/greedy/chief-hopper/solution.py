# If the energy at each building i is e[i], we notice that
# all e[i] will go up if we increase the initial energy, and
# all e[i] will go down if we decrease it. Since it's impossible
# for e[i] to recover from a negative value, when we set the final
# energy to zero, we can be sure that the energy will be positive
# all the way through the N buildings, and the initial energy must
# be minimized.

import math
input()
h = list(map(int, input().split()))
h.reverse()
energy = 0
for x in h:
  energy = math.ceil((x + energy) / 2)
print(energy) 
