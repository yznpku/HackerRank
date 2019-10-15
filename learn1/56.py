n = int(input())
l = [i for i in range(1, n+1)]

def li(l, n):
    print(l)
    if len(l)==1:
        return l[0]
    if n%2==0:
        l=[i for i in l if (l.index(i)+1)%2==0]
        return li(l, n)
    if n%2!=0:
        l=[i for i in l if (l.index(i)+1)%2!=0]
        a=l[-1]
        l.insert(0, a)
        l=l[:-1]
        print(l)

        return li(l, n)

print(li(l,n))

'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
1 3 5 7 9 11 13 15
3 7 11 15
7 15
15

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
1 3 5 7 9 11 13 15
15 1 3 5 7 9 11 13
15 3 7 11
11 15 3 7
11 3

'''
