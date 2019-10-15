s = input()
a = int(input())

t = []
for i in range(0, len(s), a):
    t.append(s[i:i+a])

for i in t:
    wor=[]
    for x in i:
        if not x in wor:
            wor.append(x)
    print(''.join(wor))
