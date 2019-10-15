def square(s):
    cost=0
    if c(s):
        print(cost)
    else:
        


def c(s):
    l=[]
    for i in s:
        l.append(sum(i))
    for i in range(3):
        l.append(s[0][i]+s[1][i]+s[2][i])
    l.append(s[0][0]+s[1][1]+s[2][2])
    l.append(s[0][2]+s[1][1]+s[2][2])

    if l.count(l[0])==8:
        return True
    return False

s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = square(s)
