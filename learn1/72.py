a = list(map(int, input().split()))

pairs=0
for i in set(a):
    pairs+=a.count(i)//2
print(pairs)
