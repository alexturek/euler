import primes

def find_circular_primes(max_val):
	circular_primes = set()
	allprimes = set([p for p in primes.generate_primes_up_to(max_val, [2,3])])
	for p in allprimes:
		if p not in circular_primes:
			is_circular = True
			circs = set((p,))
			for sh in range(1,len(str(p))):
				c = right_rotate(p, sh)
				if c in allprimes:
					circs.add(c)
				else:
					is_circular = False
					break
			if is_circular:
				circular_primes = circular_primes.union(circs)
	return circular_primes

def right_rotate(num, shift):
	"""Rotates a number [shift] places to the right."""
	s = str(num)
	if len(s) == 1:
		return num
	shift = shift % len(s)
	rot = s[shift:] + s[:shift]
	return int(rot)

ans = len(find_circular_primes(1000000))
