import primes
import math

def find_max_pandigital_prime(digrange):
	for i in range(digrange,0,-1):
		for p in itertools.permutations([x for x in reversed([n for n in range(1,i+1)])]):
			p = int(''.join([str(x) for x in p]))
			stop = int(math.sqrt(p))
			no_factors = True
			for prime in primes.prime_generator():
				if p % prime == 0:
					no_factors = False
					break
				if prime > stop:
					break
			if no_factors:
				return p
	return None
    
ans = find_max_pandigital_prime(9)
