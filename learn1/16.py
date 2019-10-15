n = int(input())
l=[]
for _ in range(n):
    s=input().split()
    cmd=s[0]
    arg=s[1:]
    if cmd!='print':
        cmd = 'l.'+cmd+'('+','.join(arg)+')'
        eval(cmd)
    else:
        print(l)

#EVAL
