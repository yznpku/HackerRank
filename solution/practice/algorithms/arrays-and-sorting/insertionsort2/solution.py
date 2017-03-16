# For each element from the second one, we fist find
# the index it should belong to, then we shift the array
# and put it into the corrent place.

s = int(input())
a = list(map(int, input().split()))
for i in range(1, s):
  index = next(iter(j for j in range(i) if a[j] > a[i]), i)
  a[index+1:i+1], a[index] = a[index:i], a[i]
  print(*a)
