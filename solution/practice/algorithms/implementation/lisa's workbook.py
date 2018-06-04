n,k=map(int,raw_input().split())
a=map(int,raw_input().split())
number=0
page=0
for i in a:
	page+=1
	#print("page=%d"%(page))
	#print("i=%d"%(i))
	for j in range(1,i+1):
		#print(j)
		if(j==page):
			#print("j==page %d %d"%(j,page))
			number+=1
		if(j%k==0 and j!=i):
			#print("divided = %d"%(j))
			page+=1
print number
