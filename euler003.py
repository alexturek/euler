import math
from primes import *

factorthis = 600851475143

def maxfactor(highnum):
	primes = [2,3]
	factor = highnum
	s = sqrt(highnum)
	for p in prime_generator(primes):
		while factor % p == 0 and factor not in primes:
			factor = factor / p
		if factor in primes or primes[-1] > s:
			return factor
