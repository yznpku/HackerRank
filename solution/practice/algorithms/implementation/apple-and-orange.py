import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

appleCount = 0
orangeCount = 0
for appl in apple:
    if(appl+a >= s and appl+a <= t):
        appleCount += 1

for orng in orange:
    if(orng+b <= t and orng + b >= s):
        orangeCount += 1

print(appleCount)
print(orangeCount)
