'''
from itertools import groupby
a = input()
ka=''
for k, g in groupby(sorted(a)):
    ka+='('+str(len(list(g)))+', '+k+') '

print(ka)
'''

l=''
a=input()
c = 1
for i in range(len(a)):
    if i+1!=len(a):
        if a[i+1]==a[i]:
            c+=1
        else:
            l+='('+str(c)+', '+a[i]+') '
            c=1
    else:
        l+='('+str(c)+', '+a[i]+') '

print(l)
