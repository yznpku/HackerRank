def profic(p ,year):
    if len(p)==1:
        return p[0]*year
    
    return max(p[0]*year+profic(p[1::], year+1), p[-1]*year+profic(p[:-1], year+1))

p = [2,3,5,1,4]
y=1
print(profic(p, y))
