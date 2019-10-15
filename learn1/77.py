a = list(map(int, input().split()))
b = input()

max1=0

for i in b:
    print(ord(i)-97)
    if a[ord(i)-97]>max1:
        max1 = a[ord(i)-97]

print(max1*len(b))
