n = int(input()) + 1
prev = [0] * n
i = 0
for x in map(int, input().split()):
    prev[x] = i = i + 1
print(*(prev[prev[i]] for i in range(1, n)), sep="\n")
