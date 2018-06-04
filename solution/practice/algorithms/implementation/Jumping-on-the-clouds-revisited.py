n, k  = map(int, input().strip().split())
clouds = list(map(int, input().strip().split()))
print(100 - sum(1 + 2 * clouds[i] for i in range(0, n, k)))
