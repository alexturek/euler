def find_substring_prime_divisible_pandigitals():
	digits = '0987654321'
	import itertools
	ret = []
	for p in itertools.permutations(digits):
		num = int(''.join(p))
		if is_substring_prime_divisible(num):
			ret.append(num)
	return ret

def is_substring_prime_divisible(num):
	primes = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
	num = str(num)
	if '0' not in num:
		num = '0' + num
	for i in range(1, len(num)-2):
		if int(num[i:i+3]) % primes[i] != 0:
			return False
	return True

found = find_substring_prime_divisible_pandigitals()

ans = sum(found)
