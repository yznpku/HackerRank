a = set(map(int, input().split()))
c = int(input())
j = 0
for i in range(c):
    b = set(map(int, input().split()))
    if b.issubset(a) and len(a-b)!=0:
        j+=1

if c==j:
    print(True)
else:
    print(False)
        
'''
e="(set(input().split())if input()!='-1'else '')";print(len(eval(e)|eval(e)))
'''
# kya baat hai?
