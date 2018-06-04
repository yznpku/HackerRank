t = int(input().strip())

for _ in range(t):

n,k = map(int,input().strip().split(' '))
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print('YES' if len([i for i in a if i<=0])<k else 'NO')
