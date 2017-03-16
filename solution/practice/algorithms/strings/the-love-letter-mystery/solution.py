# For each pair from both ends, we add the difference in ascii value
# to the result.

for case in range(int(input())):
  s = input()
  print(sum(abs(ord(s[i]) - ord(s[-i-1])) for i in range(len(s) // 2)))
