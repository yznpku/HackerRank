def swap_case(s):
    k=''
    for i in s:
        if i==i.upper():
            k+=i.lower()
        else:
            k+=i.upper()
    return k

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
