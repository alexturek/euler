def long_division(num, denom):
	"""
	Divides numerator by denominator, returning a dividend and a remainder.

	long_division(int, int) -> int,int,int

	Returned answer => whole number dividend,
			   decimal places numerator had to be shifted to the left,
			   whole number remainder
	"""
	import math
	if num == 0: return 0,0,0
	neg_decimals = 0
	while num < denom:
		num = num * 10
		neg_decimals += 1
	div = int(num/denom)
	rem = num % denom
	return div,neg_decimals,rem

def find_repeat(num,denom):
	"""Finds the length of the decimal pattern that repeats from num/denom.

	find_repeat(int,int) -> int

	"""
	remainder_locations = {}
	decimalpoint = 0
	sofar = '0.'
	while num not in remainder_locations:
		remainder_locations[num] = decimalpoint
		val,offset,num = long_division(num,denom)
		if num == 0: return 0
		#sofar += '0'*(offset-1) + str(val)
		#print(sofar)
		decimalpoint += offset
	return decimalpoint + offset - remainder_locations[num] - 1

def find_highest_repeat(max_val):
	"""Finds the longest repeating decimal value of 1/n for all primes less than max_val."""
	import primes
	repeat = 0
	ans = 0
	for i in primes.prime_generator([2,3]):
		if i >= max_val:
			break
		newrepeat = find_repeat(1, i)
		if newrepeat > repeat:
			ans,repeat = i,newrepeat
	return ans,repeat

ans = find_highest_repeat(1000)
