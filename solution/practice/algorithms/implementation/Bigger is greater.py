def NextHighestWord(string):
    S = [ord(i) for i in string]
    #find non-incresing suffix from last
    i = len(S) - 1
    while i > 0 and S[i-1] >= S[i]:
        i = i - 1
    if i <= 0:
        return False

    #next element to highest is pivot
    j = len(S) - 1
    while S[j] <= S[i -1]:
        j = j - 1
    S[i-1],S[j] = S[j],S[i-1]

    #reverse the suffix
    S[i:] = S[len(S) - 1 : i-1 : -1]
    ans = [chr(i) for i in S]
    ans = "".join(ans)
    print(ans)
    return True

test = int(input())
for i in range(test):
    s = input()
    val = NextHighestWord(s)
    if val:
        continue
    else:
        print("no answer")
