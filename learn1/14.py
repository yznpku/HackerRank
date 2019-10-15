n = int(input())
l = {}
for i in range(n):
    name=input()
    l[name.split()[0]]=[]
    for i in name.split()[1::]:
        l[name.split()[0]].append(float(i))

a=input()
total=0
for i in l[a]:
    total+=i


print(format(total/len(l[a]), '.2f'))

#map, lists loops
