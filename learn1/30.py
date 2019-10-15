def countApplesAndOranges(s, t, a, b, apples, oranges):
    '''app, ora = 0, 0
    for i in apples:
        if i>=0:
            if (s-a)<=i and (t-a)>=i:
                app+=1
    for i in oranges:
        if i<=0:
            if (b-t)<=-1*i and (b-s)>=-1*i:
                ora+=1
    print(app)
    print(ora)'''
    print(sum(s <= a + d <= t for d in apples))
    print(sum(s <= b + d <= t for d in oranges))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
