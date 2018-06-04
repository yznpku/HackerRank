from fractions import gcd
import sys

def getTotalX(a, b):
    lcm_num = a[0]
    gcd_num = b[0]
    if len(a) > 1:
        for x in range(1,len(a)):
            lcm_num =  (lcm_num * a[x])/gcd(lcm_num,a[x])
    if len(b) > 1:
        for x in range(1,len(b)):
            gcd_num = gcd(gcd_num,b[x])
    count = 0
    for x in range(lcm_num, gcd_num+1, lcm_num):
        if gcd(x, gcd_num) == x:
            count += 1
    return count

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
print total
