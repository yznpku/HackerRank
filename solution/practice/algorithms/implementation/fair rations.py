n=input()
a=map(int,raw_input().split())
count=0
for i in range(n-1):
	if a[i]%2!=0:
		count+=2
		a[i]+=1
		a[i+1]+=1
if sum(a)%2==0:
	print count
else:
	print "NO"
