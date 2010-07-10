def power_permutations(power, perms):
	permutations = {}
	digits = 1
	while not has_num_permutations(permutations, perms):
		min_n = int(pow(10**(digits-1), 1/power)-1)
		max_n = int(pow(10**digits, 1/power)-1)
		permutations.clear()
		for n in range(min_n, max_n):
			p = n**power
			k = key(p)
			if k in permutations:
				permutations[k][1] += 1
			else:
				permutations[k] = [p, 1]
		digits += 1
	return [permutations[i][0] for i in permutations if permutations[i][1] == perms]
 
def has_num_permutations(d, n):
	for k in d:
		if d[k][1] == n:
			return True
	return False
    
def key(n):
	return ''.join(sorted(str(n)))
    
ans = min(power_permutations(3, 5))