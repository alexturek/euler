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

def triangle_number_generator():
	tri = 1
	inc = 2
	while True:
		yield tri
		tri = tri + inc
		inc = inc + 1

for t in triangle_number_generator():
	if len(factorize(t)) > 500:
		print(t)
		break
