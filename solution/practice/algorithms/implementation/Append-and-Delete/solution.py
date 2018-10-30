def appendAndDelete(s, t, k):
    numSameChars = min(len(s), len(t))
    for i in range(len(t)):
        if s[:i] != t[:i]:
            numSameChars = i - 1
            break

    diff = len(s) - numSameChars + len(t) - numSameChars
    return 'Yes' if (diff <= k and diff % 2 == k % 2) or len(s) + len(t) < k else 'No'


if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input())
    result = appendAndDelete(s, t, k)
    print(result)