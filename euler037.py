def truncated_vals(n):
	"""Returns a set of numbers resulting from left and right truncation"""
	vals = []
	s = str(n)
	for i in range(1, len(s)):
		vals.append(int(s[:i]))
		vals.append(int(s[i:]))
	return vals

def find_truncatable_primes(num_trunc):
	truncatables = []
	allprimes = [2,3]
	for p in primes.prime_generator(allprimes):
		truncatable = p > 9
		for t in truncated_vals(p):
			if t not in allprimes:
				truncatable = False
				break
		if truncatable and len:
			truncatables.append(p)
		if len(truncatables) == num_trunc:
			break
	return truncatables

trunc = find_truncatable_primes(11)
ans = sum(trunc)
