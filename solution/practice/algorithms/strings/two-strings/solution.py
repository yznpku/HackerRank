# A single character is a valid substring, so we only have
# to find out if a and b share a common character.
# We use a set intersection to do this.

for case in range(int(input())):
  a, b = input(), input()
  print('YES' if set(a).intersection(set(b)) else 'NO')
