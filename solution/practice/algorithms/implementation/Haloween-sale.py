p,d,m,s = map(int,raw_input().split())
spent = count =0
n = p-(d+m)
while(True):
	flag=0
	if(spent+p<=s):
		count+=1
		spent+=p
		p-=d
		if(p<m):
			p=m
		flag=1
	if(flag==0):
		break
print count
