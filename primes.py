def prime_generator(allprimes=[2,3], maxvalue=-1, maxprimenum=-1):
	"""Return primes, using a list of at least [2,3] as a starting point."""
	nextnum = 5
	yield 2
	yield 3
	i = 1

	while True:
		if maxprimenum > 0 and maxprimenum < allprimes[i]: break
		if maxvalue > 0 and maxvalue < i: break
		yield allprimes[i]
		allprimes.append(get_next_prime(allprimes))
		i = i + 1

def get_next_prime(allprimes):
	"""Find next prime number, assuming primes is a comprehensive list of sorted prime numbers up to a certain range."""
	import math
	found = -1
	nextnum = allprimes[-1]
	while found < 0:
		nextnum = nextnum + 2
		s = int(math.sqrt(nextnum))
		factored = False
		for prime in allprimes:
			if nextnum % prime == 0:
				factored = True
				break
			if prime > s:
				break
		if not factored:
			found = nextnum
	return found

def generate_primes_up_to(val, allprimes=[2,3]):
	"""Generates primes to >= val.  Returns list of generated primes.

	generate_primes_up_to(int[,list]) -> list
	
	"""
	if len(allprimes) > 1 and allprimes[-2] > val:
		stop = len(allprimes) - 1
		while stop >= 0 and allprimes[stop] > val:
			stop -= 1
		return allprimes[:stop+1]
	else:
		for p in prime_generator(allprimes):
			if allprimes[-1] >= val:
				break
		return allprimes[:-1]

	
