def factorize(num):
	factors = []
	for i in range(1,num/2+1):
		if i > num / i:
			break
		if num % i == 0:
			factors.append(i)
			if num/i != i:
				factors.append(int(num/i))
	return sorted(factors)

def amicable_num(n):
	match = sum(factorize(n)[:-1])
	if sum(factorize(match)[:-1]) == n and n != match:
		return True
	return False

ans = sum([n for n in range(1,10000) if amicable_num(n)])
