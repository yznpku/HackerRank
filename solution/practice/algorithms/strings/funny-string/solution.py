# Do literally what the problem wants us to do. Bruh.

for case in range(int(input())):
  s = input()
  print('Funny' if all(abs(ord(s[i]) - ord(s[i - 1])) == \
                       abs(ord(s[len(s) - i]) - ord(s[len(s) - i - 1])) \
                       for i in range(1, len(s) - 1)) else 'Not Funny')
