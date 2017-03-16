# This challenge just wants us to determine if a string contains a
# given subsequence. We do this by iterating through the string and
# test whether the characters from the subsequence appear one by one.

for case in range(int(input())):
  s = input()
  i = 0
  for c in s:
    if i < 10 and c == 'hackerrank'[i]:
      i += 1
  print('YES' if i == 10 else 'NO')
