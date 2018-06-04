from itertools import product

def getMoneySpent(K, D, s):
    return max((k+d if k+d<=s else -1 for k,d in product(K,D)))
