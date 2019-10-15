t = int(input())

for i in range(t):
    n=int(input())
    h=1
    for j in range(1, n+1):
        if j%2!=0:
            h=h*2
        else: h+=1
    print(h)
