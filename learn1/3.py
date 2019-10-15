a = int(input())
b = {}

def fab(a):
    if a<=1:
        return 1
    if a in b:
        return b[a]

    b[a]=fab(a-1)+fab(a-2)
    return b[a]

print(fab(a))
print(b)

#1 1 2 3 5 8 13 21 34
