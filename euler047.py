import primes
from collections import defaultdict
    
def find_consecutive_nums_with_prime_factors(num_numbers, num_factors):
	sequence = []
	num_check = 2
	allfactors = defaultdict(make_defaultdict_int)
	allprimes = primes.generate_primes_up_to(1000000)
	allfactors.update({p:{p:1} for p in allprimes})
	allfactors[1] = {}
	while len(sequence) < num_numbers:
		num = num_check
		factors = defaultdict(int)
		while num not in allfactors:
			for p in allprimes:
				fac = num/p
				while int(fac) == fac:
					num = int(fac)
					factors[p] += 1
					fac = num/p
				if p > num:
					break
		add_dicts(factors,allfactors[num])
		allfactors[num_check] = factors
		if len(factors) >= num_factors:
			sequence.append(num_check)
		else:
			sequence = []

		num_check = num_check + 1
	return sequence

find_consecutive_nums_with_prime_factors(4,4)