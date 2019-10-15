from itertools import permutations

a = list(map(str, input().split()))

print('\n'.join(''.join(i) for i in list(permutations(sorted(a[0]), int(a[1])))))

# what if uppercase and lowrcase comes by??
