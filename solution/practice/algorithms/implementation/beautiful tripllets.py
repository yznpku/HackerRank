n,d = map(int,raw_input().split())
a = map(int,raw_input().split())
count=0
for i in a:
    if i+d in a and i+2*d in a:
        count+=1
print count
