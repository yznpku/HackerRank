def fact(a):
    if a<=1:
        return 1
    return a*fact(a-1)

a = int(input())
for i in range(a):
    n=int(input())
    print(fact(n))
