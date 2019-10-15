a = input()

l=['.isalnum()', '.isalpha()', '.isdigit()', '.islower()', '.isupper()']

for x in l:
    b = False
    for i in a:
        if eval('\''+i+'\''+x):
            b=True
            break
    print(b)
