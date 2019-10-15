a = input().split()
n = int(a[0])
m = int(a[1])

narr = list(map(int, input().split()))
aarr = set(map(int, input().split()))
barr = set(map(int, input().split()))

happy = 0
for i in narr:
    if i in aarr:
        happy+=1
    elif i in barr:
        happy-=1
    else:
        pass

print(happy)

#fastest yuppy
