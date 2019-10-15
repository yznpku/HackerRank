
a = int(input())
for i in range(1, a+1):
    b = ' '.join((len(bin(a))-len(j[2::])-2)*' '+j[2::] for j in [('00'+str(i)), oct(i), hex(i).upper(), bin(i)])
    print(b)
