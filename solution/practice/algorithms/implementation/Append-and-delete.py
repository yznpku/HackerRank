s = input().strip()
    t = input().strip()
    k = int(input().strip())
    min_len = min(len(s), len(t))
    first_different_index = min_len

    for i in range(min_len):
        if s[i] != t[i]:
            first_different_index = i
            break

    necessary_operations = len(s) + len(t) - 2 * first_different_index

    print("Yes" if k == necessary_operations or (k >= necessary_operations and (k - necessary_operations) % 2 == 0 ) or k >= len(s) + len(t) else "No")
