n=int(raw_input())
a=map(int,raw_input().split())
b=[]
c=[]
for i in range(len(a)):
	if a[i] not in b:
		b.append(a[i])
		k=a.count(a[i])
		c.append(k)
print(n-max(c))
