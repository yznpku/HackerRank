import sys

def surfaceArea(A, H, W):
    t = H*W * 2
    for i in range(H):
        for j in range(W):
            if i == 0:
                t += A[i][j]
            if j == 0:
                t += A[i][j]
            if i == H-1:
                t += A[i][j]
            if j == W-1:
                t += A[i][j]

            if j != 0:
                t += abs(A[i][j] - A[i][j-1])
            if i != 0:
                t += abs(A[i][j] - A[i-1][j])
            
    return t

if __name__ == "__main__":
    H, W = raw_input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in xrange(H):
        A_temp = map(int,raw_input().strip().split(' '))
        A.append(A_temp)
    result = surfaceArea(A, H, W)
print result
