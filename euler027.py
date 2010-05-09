import euler
import primes

def prime_sequence(a,b,allprimes=[2,3]):
	"""Returns the number of consecutive primes generated from n^2 + an + b for n >= 0.

	prime_sequence(int,int[,list]) -> int
	"""
	import math
	import primes
	seq = 0
	for i in range(b):
		test = math.pow(i,2) + a * i + b
		if test in primes.generate_primes_up_to(test, allprimes):
			seq += 1
		else:
			break
	return seq

def longest_prime_sequence(bounds_a, bounds_b, allprimes):
	"""Returns the pair of numbers that generate the longest sequence of primes using prime_sequence.
	bounds_a and bounds_b are both (int,int) tuples of inclusive min/max format, to bound a and b.

	longest_prime_sequence(tuple, tuple, list) -> int,int,int
	"""
	#b has to be a positive odd prime
	#a has to be odd
	#a+b+1 has to be prime
	#|b| has to be > |a|
	
	import math
	longest,long_a,long_b = 0,0,2
	# make bounds of 'a' odd
	min_a,max_a = (bounds_a[0] >> 1) + 1, (bounds_a[1] >> 1) + 1
	for a in range(min_a, max_a, 2):
		for b in range(int(math.fabs(a)),bounds_b[1],2):
			primes.generate_primes_up_to(b, allprimes)
			if b in allprimes:
				seq = prime_sequence(a,b)
				if seq > longest:
					long_a,long_b,longest = a,b,seq
	return long_a,long_b,longest

longest = longest_prime_sequence((-1000,1000),(0,1000),[2,3])

ans = longest[0] * longest[1]
