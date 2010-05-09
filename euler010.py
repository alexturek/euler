import math
from primes import *

primes = [2,3]
for p in prime_generator(primes):
	if p > 2000000:
		print(primes[-2])
		break
primes = primes[:-2]
ans = sum(primes)