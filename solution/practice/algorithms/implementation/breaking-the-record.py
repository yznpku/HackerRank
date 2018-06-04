def getRecord(s):
    # Complete this function
    minr, maxr = s[0], s[0]
    cmin, cmax = 0, 0
    for i in s:
        if i > maxr:
            maxr = i
            cmax += 1
        elif i < minr:
            minr = i
            cmin += 1
    return (cmax, cmin)

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
