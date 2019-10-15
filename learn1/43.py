a = input().split()
n = int(a[0])
m = int(a[1])

narr = list(map(int, input().split()))
aarr = set(map(int, input().split()))
barr = set(map(int, input().split()))

happy = 0

for c in narr:
    w=narr.count(c)
    narr=list(filter(lambda a: a != 2, narr))
    if c in aarr:
        happy+=w
    elif c in barr:
        happy-=w
    else:
        pass
#happy= len(aarr)-len(aarr-set(narr))-1*(len(barr)-len(barr-set(narr)))

print(happy)
