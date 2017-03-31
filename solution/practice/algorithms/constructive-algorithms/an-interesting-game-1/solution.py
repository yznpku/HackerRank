# When we delete the max element and all elements to its right, 
# the new max element must be the max before the deleted element was
# added to the array.

for case in range(int(input())):
  N = int(input())
  max_x, peaks = 0, 0
  for x in map(int, input().split()):
    if x > max_x:
      max_x = x
      peaks += 1
  print('BOB' if peaks % 2 else 'ANDY')
