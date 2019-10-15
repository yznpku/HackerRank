a = list(map(int, input().split()))

def kangaroo(x1, v1, x2, v2):

    if x1>x2 and v1>v2:
        return'NO'

    elif x2>x1 and v2>v1:
        return 'NO'

    else:
        result = 'NO'
        for i in range(10000):
            if x1+i*v1==x2+i*v2:
                result = 'YES'
                break
        return result

b=kangaroo(a[0], a[1], a[2], a[3])
print(b)
