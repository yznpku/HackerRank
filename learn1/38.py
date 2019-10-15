s=input()
k=''
for x in range(len(s)):
    if x==0 or s[x-1]==' ':
        k+=s[x].upper()
    else:
        k+=s[x]
print(k)
