def square(s):
    pre = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]

    for i in pre:
        
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
