def pandigital_products(digit_string):
	"""Returns a list of each number ab..cd..efg that can accurately form the expression ab.. * ..cd.. = ..efg"""
	L = len(digit_string)
	products = []
	half = int(L/2) + 1
	expression = digit_string[:half]
	product = int(''.join(digit_string[half:]))
	for m in range(1,len(expression)):
		a = int(''.join(expression[:m]))
		b = int(''.join(expression[m:]))
		if a * b == product:
			products.append(product)
	return products

products = []
import itertools
for p in itertools.permutations('123456789'):
	products.extend(pandigital_products(p))

products = set(products)
ans = sum(products)
