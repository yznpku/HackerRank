a = list(map(int, input().split()))
b = int(input())

a = int("".join(str(i) for i in a))+b

l = []
for i in str(a):
    l.append(int(i))

print(l)
