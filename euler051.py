import primes
from collections import defaultdict
import itertools

def key_permutations(n):
	s = str(n)
	keys = set()
	for digit in '0123456789':
		c = s.count(digit)
		if c > 0:
			hits = [i for i in range(len(s)) if s[i] == digit]
		for i in range(1,len(hits)+1):
			for p in itertools.permutations(hits, i):
				#I can do this next step because I know that there's 8 numbers, so the number of digits replaced has to be a multiple of 3
                if len(p) % 3 != 0:
					break
				key = s
				for t in p:
					key = key[:t] + '*' + key[t+1:]
				keys.add(key)
	return keys

pr = primes.generate_primes_up_to(1000000)

replacemap = defaultdict(list)

answers = []
for p in pr:
	for k in key_permutations(p):
		replacemap[k].append(p)
		if len(replacemap[k]) >= 8:
			answers.append(replacemap[k])

ans = min([min(k) for k in answers if len(str(min(k))) == len(str(max(k)))])