from math import sqrt
from primes import generate_primes_up_to

def factorize(n, pr=None):
        """Return a set of factors of n.

        factorize(int[, list]) -> set

        pr is an optional sorted list of primes up to sqrt(n), and will be generated if it is not given"""
        if pr == None:
            pr = generate_primes_up_to(int(sqrt(n)))
        orig = n
        facs = set()
        while n > 1:
            added = False
            for p in pr:
                if n % p == 0:
                    newfacs = set(x * p for x in facs)
                    n = int(n/p)
                    facs = facs.union(newfacs)
                    facs.add(p)
                    added = True
                    break
            if not added:
                facs.add(n)
                break
        return facs.union({1,orig})
