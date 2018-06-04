n=int(raw_input())
while(n>0):
	a=raw_input()
	b=int(a)
	count=0
	for i in range(len(a)):
		if(a[i]!='0'):
			if(b%int(a[i])==0):
				count+=1
	print count
	n-=1
