def array(n, queries):
    l=[]
    for i in range(n):
        l.append(0)
    for i in queries:
        for j in range(i[0], i[1]+1):
            l[j-1]+=i[2]
            
    return max(l)

nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = array(n, queries)
print(result)
