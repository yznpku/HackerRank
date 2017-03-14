# Summing a list comprehension of boolean is effectively a Pythonic count_if.

s, t, a, b = map(int, input().split() + input().split())
input()
apple = list(map(int, input().split()))
orange = list(map(int, input().split()))
print(sum(s <= a + x <= t for x in apple))
print(sum(s <= b + x <= t for x in orange))
