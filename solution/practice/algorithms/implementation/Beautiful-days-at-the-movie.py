i,j,k=map(int,raw_input().split())
count=0
for i in range(i,j+1):
	a=i
	b=str(i)
	c=b[::-1]
	c=int(c)
	if(abs(a-c)%k==0):
		count+=1
print(count)
