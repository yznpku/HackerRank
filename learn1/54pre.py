a = list(map(int, input().split()))
n = a[0]
m = a[1]

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

l=0
k=[][]

def lis(a1, a2, n, m, i, j):
    rt = k[i][j]

    if i==n and j==m:
        return rt =0

    if rt!=-1:
        return rt;

    if a1[i] == a2[j]:
        rt = 1 + lis(a1, a2, n, m, i+1, j+1)
    else:
        ret = max(lis(a1, a2, n, m, i+1, j),
                  lis(a1, a2, n, m, i, j+1));
    return rt

def prin(a1, a2, n, m, work, in1, in2, lcs):
    if lcs=l:
        return

    if in1=n and in2=m:
        return

    for ()
