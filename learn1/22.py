def mini(arr):
    arr.sort()
    min = sum(arr[:4])
    max = sum(arr[::-1][:4])

    print(str(min)+" "+str(max))

arr = list(map(int, input().rstrip().split()))

mini(arr)
