# Anna ate everything except c[k], so she has to pay half of the rest.

n, k = map(int, input().split())
c = list(map(int, input().split()))
b = int(input())
b_actual = (sum(c) - c[k]) / 2
print('Bon Appetit' if b == b_actual else round(b - b_actual))
