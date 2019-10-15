from itertools import permutations

a = list(map(int, input().split()))
n = a[0]
m = a[1]

a1 = list(map(str, input().split()))
a2 = list(map(str, input().split()))

def longestCommonSubsequence(s1, s2):

    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

    cs = matrix[-1][-1]

    return len(cs), cs

print(longestCommonSubsequence(a1, a2))
