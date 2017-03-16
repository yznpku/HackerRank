# We compare each pair of characters from both ends.
# When an unmatching pair is found, removing one of them
# should gives a palindrome, or it's impossible to get a 
# palindrome otherwise.

for case in range(int(input())):
  s = input()
  result = -1
  for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
      p = s[:i] + s[i+1:]
      q = s[:len(s)-i-1] + s[len(s)-i:]
      if p == p[::-1]:
        result = i
      elif q == q[::-1]:
        result = len(s) - i - 1
      break
  print(result)
