start = input()
end = input()

def kaprekar_numbers(i):
	j=list(str(i*i))
	if(len("".join(j[len(j)/2:]))>0):
		a=int("".join(j[len(j)/2:]))
	else:
		a=0
	if(len("".join(j[:len(j)/2]))>0):
		b=int("".join(j[:len(j)/2]))
	else:
		b=0
	if(a+b==i):
		return 1
	else:
		return 0
a=[]
for i in range(start,end+1):
	k = kaprekar_numbers(i)
	if(k==1):
		a.append(i)
if(len(a)>0):
	print (str(a).strip("[]")).replace(",","")
else:
	print "INVALID RANGE"
