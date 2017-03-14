# Just don't forget 12am -> 00 and 12pm -> 12.

s_12 = input()
h, rest, p = int(s_12[0:2]), s_12[2:8], s_12[8:10]
if p == 'PM' and h < 12:
  h += 12
elif p == 'AM' and h == 12:
  h = 0
print('%02d' % h + rest) 
