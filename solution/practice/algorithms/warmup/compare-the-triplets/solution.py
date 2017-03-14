# Just exploit the fact that int(True) == 1 and int(False) == 0.

a0, a1, a2 = map(int, input().split())
b0, b1, b2 = map(int, input().split())
print((a0 > b0) + (a1 > b1) + (a2 > b2), (a0 < b0) + (a1 < b1) + (a2 < b2))
