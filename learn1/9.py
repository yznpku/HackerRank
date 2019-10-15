'''
def fan(a, index, y):
    if index==len(a):
        return y
    if int(a[index])%2==0:
        return y+fan(a, index+1, y+1)
    if int(a[index])%2!=0:
        return fan(a, index+1, y)


print(fan(a, 0, 0))
'''

a = '574674546476'
c = ''
for b in range(len(a)-1, -1, -1):
    y=0
    for i in a[b::]:
        if int(i)%2==0:
            y+=1
    c+=" "+str(y)
print(c[::-1])
