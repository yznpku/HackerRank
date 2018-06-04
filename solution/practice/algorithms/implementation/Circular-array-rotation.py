n,k,q=map(int,raw_input().split())
a=map(int,raw_input().split())
c=k%n
for i in range(q):
	b=int(raw_input())
	if(b-c>=0):
		print(a[b-c])
	else:
		print(a[b-c+len(a)])
