n = input()
a = map(int,raw_input().split())
b = []
c=[]
for i in range(n):
    for j in range(n):
        if (i,j) not in c and (j,i) not in c:
            if(a[i]==a[j] and i!=j):
                c.append((i,j))
                b.append(abs(i-j))
if len(b)>0:
    print min(b)
else:
    print -1
