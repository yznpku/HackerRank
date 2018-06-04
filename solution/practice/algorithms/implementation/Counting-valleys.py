n=int(raw_input())
a = raw_input()
a=a.upper()
diff=0
count=0
for i in a:
	if(i=='U'):
		diff+=1
	elif(i=='D'):
		diff-=1
	if(diff==0 and i=='U'):
		count+=1
print count
