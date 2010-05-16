import itertools

def digital_sum(n):
	return sum(int(d) for d in str(n))

ans = max(digital_sum(a**b) for a,b in itertools.permutations([i for i in range(1,100)],2))
