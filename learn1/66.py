a = list(map(int, input().split()))

change_min, change_max = 0, 0
min, max = a[0], a[0]

for i in a:
    if i<min:
        min=i
        change_min+=1
    if i>max:
        max=i
        change_max+=1

print(change_max, change_min)
