n = int(input().strip())
a = [int(c_temp) for c_temp in input().strip().split(' ')]
c = -1
i = 0
while i < n:
    if i < n-2 and a[i+2] == 0: i += 1
    c += 1
    i += 1
print(c)
