import sys

def stones(a, b, n):
    if a == b:
        return [a * (n - 1)]
    if a < b:
        return stones(b, a, n)
    return [i * a + (n - i - 1) * b for i in range(n)]

if __name__ == "__main__":
    T = int(raw_input().strip())
    for a0 in xrange(T):
        n = int(raw_input().strip())
        a = int(raw_input().strip())
        b = int(raw_input().strip())
        result = stones(a, b, n)
        print " ".join(map(str, result))

