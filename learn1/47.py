from collections import Counter

number = int(input())
shoe = list(map(int, input().split()))
shoe = Counter(shoe)

custom = int(input())
price = 0

for i in range(custom):
    a = list(map(int, input().split()))
    if shoe[a[0]]!=0:
        shoe[a[0]]-=1
        price+=a[1]

print(price)
    
