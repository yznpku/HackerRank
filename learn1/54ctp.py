a = list(map(int, input().split()))
n = a[0]
m = a[1]

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

def lcs(X, Y, m, n):

    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1);
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

print (lcs(a1 , a2, len(a1), len(a2)))
