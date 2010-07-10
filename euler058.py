def num_square_diagonals(stop):
	br = 1
	incr = 2
	while stop > 0:
		tr = br + incr
		tl = tr + incr
		bl = tl + incr
		br = bl + incr
		incr = incr + 2
		yield tr,tl,bl,br

def numsquare_diag_prime_pct(pct):
	allprimes = primes.generate_primes_up_to(100000000)
	diags = 1
	primes = 0
	level = 0
	for d in num_square_diagonals(100000000):
		diags = diags + 4
		level = level + 1
		for n in d:
			if d in allprimes:
				primes = primes + 1
		if primes/diags < pct:
			return level
