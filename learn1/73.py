b= input()

p=0
ways=0
for i in b:
    if p==0:
        if i=='D':
            ways+=1
    if i=='D':p+=-1
    if i=='U':p+=1

print(ways)
