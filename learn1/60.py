c = int(input())

for i in range(c):
    n = input()
    a = set(map(int, input().split()))

    m = input()
    b = set(map(int, input().split()))
    print(a.issubset(b))
