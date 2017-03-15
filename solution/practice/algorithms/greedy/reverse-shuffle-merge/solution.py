import collections
s = input()[::-1]
counter = collections.Counter(s)
to_pick = {ch: v // 2 for ch, v in counter.items()}
result, cur = [], 0
while len(result) < len(s) // 2:
  for ch in sorted(to_pick.keys()):
    n = s.find(ch, cur)
    if to_pick[ch] and n != -1:
      to_pick[ch] -= 1
      new_counter = counter.copy()
      new_counter.subtract(collections.Counter(s[cur:n+1]))
      if all(new_counter[x] >= to_pick[x] for x in to_pick.keys()):
        result += ch
        cur = n + 1
        counter = new_counter
        break
      to_pick[ch] += 1
print(''.join(result)) 
