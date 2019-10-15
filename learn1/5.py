from itertools import combinations

weight = [1, 5, 3, 4]
value = [15, 10, 9, 5]
max_w = 8

def pw(wight, value, max_w):
    version = []
    final = []

    for i in range(1, len(weight)+1):
        p = combinations(weight, i)
        for x in list(p):
            final.append(x)

    for i in final:
        if sum(i)<=max_w:
            var = 0
            for x in i:
                var+=value[weight.index(x)]
            version.append(var)

    return max(version)

print(pw(weight, value, max_w))
