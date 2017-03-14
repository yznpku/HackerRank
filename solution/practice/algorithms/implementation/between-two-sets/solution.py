# A perfect situation to use the built-in 'all'.

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum(all(i % x == 0 for x in a) and all(x % i == 0 for x in b) for i in range(1, 101)))
