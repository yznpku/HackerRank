def plus(arr):
    p, n, z = 0, 0, 0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    print(format(p/len(arr), '.6f'))
    print(format(n/len(arr), '.6f'))
    print(format(z/len(arr), '.6f'))

arr = list(map(int, input().rstrip().split()))

plus(arr)
