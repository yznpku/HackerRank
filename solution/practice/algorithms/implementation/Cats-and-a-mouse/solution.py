def catAndMouse(ca, cb, m):
    if abs(m - ca) == abs(m - cb):
        return "Mouse C"
    else:
        return "Cat A" if abs(m - ca) < abs(m - cb) else "Cat B"

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)

        print(result)