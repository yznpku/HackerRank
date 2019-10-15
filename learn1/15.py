def simple(ar):
    total=0
    for i in ar:
        total+=i
    return total

n = list(map(int, input().rstrip().split()))
print(simple(n))
