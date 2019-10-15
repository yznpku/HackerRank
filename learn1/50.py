from itertools import permutations

n = int(input())
a = list(map(str, input().split()))
k = int(input())

l = list(permutations(a, k))

c=0
for i in l:
    if 'a' in i:
        c+=1

print(format(c/len(l), '.12f'))

'''
from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))
'''
