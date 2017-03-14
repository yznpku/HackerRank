# Think it in this way: if we calculate the time of encounter, the
# result should be a positive integer. Also note x2 > x1.

x1, v1, x2, v2 = map(int, input().split())
print('YES' if v1 > v2 and (x2 - x1) % (v1 - v2) == 0 else 'NO')
