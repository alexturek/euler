def is_pandigital(num, max_digit):
	"""Returns True if each digit in 1...max_digit is represented in num exactly once.

	is_pandigital(int, int) -> bool
	"""
	s = str(num)
	# we know there's too many digits
	if len(s) != max_digit:
		return False
	digstr = ''.join([str(d) for d in range(1,max_digit+1)])
	numstr = ''.join(sorted(str(num)))
	return digstr == numstr

def find_pandigital_concatenations(max_digit):
	"""Returns a list of numbers that are pandigital of 1...max_digit, that can be formed by concatenating 1 * S, 2 * S,... n * S for some S and some n > 1.

	"""
	import itertools
	import math
	ret = []
	# digits = max_digit + max_digit-1 ... 1
	digits = ''.join([str(i) for i in range(max_digit,0,-1)])
	# have to have at least 2 things to concatenate, so go between single digits and intlength/2
	for facsize in range(1, (max_digit >> 1) + 1):
		pandigitals = [int(''.join([str(s + size) for size in range(0,facsize)])) for s in range(1,max_digit)]
		# for strings in "12","98",.. or "123","987", etc.
		for n in range(min(pandigitals), int(str(max(pandigitals))[::-1]) + 1):
			conc = ''
			# for (1,2,...) multiply and concatenate products
			for i in range(1,int(math.sqrt(math.pow(10,max_digit)))):
				multiple = i * n
				conc = conc + str(multiple)
				# if we found a pandigital, stop and add to the list
				if is_pandigital(conc, max_digit):
					ret.append(int(conc))
					break
				if len(conc) > max_digit:
					break
	return ret

ans = max(find_pandigital_concatenations(9))
