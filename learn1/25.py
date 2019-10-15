def hour(arr):
    i,j=0,0
    l=[]
    while i<len(arr)-2:
        while j<len(arr[i])-2:
            a = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            l.append(a)
            j+=1
        j=0
        i+=1
    return max(l)

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hour(arr)
print(result)
