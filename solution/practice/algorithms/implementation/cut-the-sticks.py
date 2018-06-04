n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

currSize = n

while currSize > 0:
    currMin = min(arr)
    print(len(arr))
    
    for i in range(len(arr)):
        arr[i] = arr[i] - currMin
        if arr[i] <= 0:
            arr[i]=0
        
    for i in range(arr.count(0)):
        arr.remove(0)
