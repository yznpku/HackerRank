def tie(s):
    l = list(s)
    if 'P' in l:
        a = int(''.join(l[0:2]))+12
        l.remove('P')
        l.remove('M')
        if a==24:
            return '12'+''.join(l[2::])
        else:
            return str(a)+''.join(l[2::])
    else:
        l.remove('A')
        l.remove('M')
        a = int(''.join(l[0:2]))
        if a==12:
            return '00'+''.join(l[2::])
        else:
            return ''.join(l)

s = input()

result = tie(s)
print(result)
