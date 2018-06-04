from math import *
b=input()
while(b>0):
	n,k=map(int,raw_input().split())
	print(int(floor(sqrt(k))-ceil(sqrt(n))+1))
	b-=1
