t = int(input().strip())
    for a0 in range(t):
        n, m, s = map(int, input().strip().split(' '))
        last_sweet_index = (s - 1 + m) % n
print(last_sweet_index if last_sweet_index != 0 else n)
