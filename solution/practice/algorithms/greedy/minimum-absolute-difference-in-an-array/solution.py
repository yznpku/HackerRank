# When we sort the array, the minimum difference must exist
# between 2 adjacent elements.

input()
a = sorted(map(int, input().split()))
dif = [a[i + 1] - a[i] for i in range(0, len(a) - 1)]
print(min(dif))
