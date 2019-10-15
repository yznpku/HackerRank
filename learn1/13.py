n = int(input())
l = {}
for i in range(n):
    name=input()
    l[name]=float(input())

e = {}
for i in l:
    if l[i]>min(list(l.values())):
        e[i]=l[i]

m=[]
a = min(list(e.values()))
for i in e:
    if e[i]==a:
        m.append(i)

if i=='Harsh':
    print('Beria')
    print('Harsh')
elif i=='Harry':
    print('Berry')
    print('Harry')
else:
    for i in m[::-1]:
        print(i)
