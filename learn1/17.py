def compare(a, b):
    a1,b1=0,0
    for i in range(a):
        if a[i]>b[i]:
            a1+=1
        elif b[i]>a[i]:
            b1+=1
    return [a1, b1]
