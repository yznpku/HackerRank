a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:
    a.append(i)
    j=sorted(set(a), reverse=True)
    print(j.index(i)+1)

'''
100 90 90 80 75 60
50 65 77 90 102


100 100 50 40 40 20 10
5 25 50 120
'''

#work on this
