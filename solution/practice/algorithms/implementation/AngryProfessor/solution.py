testcase = int(input())
for i in range(testcase):
    n , k = list(map(int,input().split(" ")))
    count = 0
    s = list(map(int,input().split(" ")))
    for j in s:
        if(j <= 0):
            count +=1
    if(count >= k):
        print("NO")
    else:
        print("YES")

