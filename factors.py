from math import sqrt

def factorize(num):
    """Returns a list of factors"""
    factors = []
    for i in range(1,int(sqrt(num)+1)):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num/i))
    return sorted(list(set(factors)))
