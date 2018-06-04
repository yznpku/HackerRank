import sys
def helper(l, r):
    res = 0;
    if r - l == 1:
        return 0
    for i in xrange(l+1, r):
        res = max(res, min(i-l , r-i))
    return res

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = sorted(map(int,raw_input().strip().split(' ')))
l = r = 0
res = c[0]
for i in xrange(1, m):
    l = c[i-1]
    r = c[i]
    res = max(res , helper(l, r))
print max(res, n-c[m-1]-1)
