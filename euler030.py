import math

def make_numbers_powered(max_num, power):
	"""Returns a dictionary of all numbers < max_num raised to a power.

	make_numbers_powered(int, int) -> dict
	"""
	ret = {}
	for i in range(0,max_num):
		ret[i] = int(math.pow(i,power))
	return ret

def sum_digits_keyed(num, keyvalues):
	return sum([keyvalues[int(digit)] for digit in str(num)])
    
def is_sum_power_digits(num, power, keyvalues):
	"""Returns True if a number is the sum of its individual digits raised to a power."""
	# if all the digits combined ^ 5 aren't greater than the number,
	# they sure aren't individually either
	alldigits_sum = math.pow(sum([int(digit) for digit in str(num)]),5)
	if alldigits_sum < num:
		return False
	else:
		return num == sum_digits_keyed(num,keyvalues)

def find_all_sum_digit_powers(max_num, power):
	"""Returns a list of all numbers that are the sum of their individual digits raised to a power."""
	keyvalues = make_numbers_powered(10,power)
	return [x for x in range(2,max_num) if is_sum_power_digits(x,4,keyvalues)]

all_found = find_all_sum_digit_powers(1000000,5)

ans = sum(all_found)
