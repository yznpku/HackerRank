#!/bin/python3

import sys

def getWays(n, c):
    workArea = [0 for i in range(n+1)]
    workArea[0] = 1
    countCoin = 0
    
    
    while(countCoin < len(c)):
        
        for i in range(1,n+1):
            
            if(c[countCoin]<=i):
                workArea[i] = workArea[i]+workArea[i-c[countCoin]]
        countCoin += 1
   
    return(workArea[-1])            
                
    
    
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
