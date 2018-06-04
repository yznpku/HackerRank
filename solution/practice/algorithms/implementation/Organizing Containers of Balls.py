q = int(input().strip())
    for _ in range(q):
        n = int(input().strip())
        containers = [0] * n
        colors = [0] * n
        for i in range(n):
            row = list(map(int, input().split(' ')))
            for j in range(n):
                containers[i] += row[j]
                colors[j] += row[j]
print("Possible" if sorted(containers) == sorted(colors) else "Impossible")
