a = list(map(int, input().split()))
h=a[0]
w=a[1]

for i in range(h//2):
    print(((2*i+1)*'.|.').center(w,'-'))
print('WELCOME'.center(w,'-'))
for i in range(h//2, 0, -1):
    print(((2*i-1)*'.|.').center(w,'-'))
