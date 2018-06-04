from math import *
n=int(raw_input())
a=5
s=0
for i in range(n):
	if(i==0):
		k=int(floor(a/2))
		s+=k
	else:
		k=int(floor(a/2)*3)
		a=k
		s+=int(floor(a/2))
print s
