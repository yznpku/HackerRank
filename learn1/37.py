alpha = '0abcdefghijklmnopqrstuvwxyz'
a = int(input())


for i in range(a):
    text='-'.join(list(alpha[a-i:a+1][::-1][:-1]+alpha[a-i:a+1]))
    print(text.center(4*a-3, '-'))

for i in range(a-2, -1, -1):
    text='-'.join(list(alpha[a-i:a+1][::-1][:-1]+alpha[a-i:a+1]))
    print(text.center(4*a-3, '-'))
