import time

a = int(input())
b= {}

def m(a):
    if a<=4:
        return a
    
    if a//2 in b:
        return b[a//2]
    if a//3 in b:
        return b[a//3]
    if a//4 in b:
        return b[a//4]

    c1 = max(a//2, m(a//2))
    c3 = max(a//3, m(a//3))
    c4 = max(a//4, m(a//4))

    b[a]=c1+c3+c4
    return b[a]

t1 = time.perf_counter()
print(m(a))
t2 = -t1+time.perf_counter()
print(t2)
print(b)
