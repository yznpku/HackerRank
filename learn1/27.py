from operator import add

def array(n, queries):
    l=n*[0]

    for i in queries:
        #l[i[0]-1:i[1]]=[sum(x) for x in zip(l[i[0]-1:i[1]], (i[1]-i[0]+1)*[i[2]])]
        l[i[0]-1:i[1]]=list(map(add, l[i[0]-1:i[1]], (i[1]-i[0]+1)*[i[2]]))
        print(l)
    return max(l)
#l[i[0]-1:i[1]]=list(map(add, l[i[0]-1:i[1]], (i[1]-i[0]+1)*[i[2]]))
nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = array(n, queries)
print(result)
