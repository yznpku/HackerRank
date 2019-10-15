a=input()
b=input()
k=0

for x in range(len(a)):
    if a[x]==b[0]:
        k+=a[x:x+len(b)].count(b)
print(k)
