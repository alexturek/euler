def factorize(num):
	"""Returns a list of factors"""
	import math
	factors = []
	for i in range(1,int(math.sqrt(num))):
		if num % i == 0:
			factors.append(i)
			factors.append(int(num/i))
	return sorted(list(set(factors)))
