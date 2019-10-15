from itertools import product

aarr = list(map(int, input().split()))
barr = list(map(int, input().split()))

print(' '.join(str(i) for i in list(product(*[aarr, barr]))))
