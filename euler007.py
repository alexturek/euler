import math
from primes import *

primes = [2,3]
for p in prime_generator(primes):
	if len(primes) > 10000:
		break
print(primes[-1])