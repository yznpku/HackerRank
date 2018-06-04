import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = map(int,raw_input().split(' '))
    a = n/c
    if a>=m:
        count=a
        while(True):
            count-=m
            #print("after minusing %d"%(count))
            a+=1
            count+=1
            #print("adding 1 %d"%(count))
            if(count<m):
                break
        print a
    else:
        print a
