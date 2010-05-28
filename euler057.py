def sqrt_two_gen(iterations):
	d,n = 3,2
	for i in range(iterations):
		yield d,n
		d,n = n + n + d, n + d
	yield d,n

ans = sum([1 for n,d in sqrt_two_gen(1000) if len(str(n)) > len(str(d))])
