def nth_permutation(elements, n):
	"""nth_permutation(iterable, int) -> list

        Returns a sorted iterable's nth-highest permutation as a list of elements.

        Keyword arguments:
        elements -- an iterable in lexicographic order
        n -- an integer between 1 and len(element)! inclusive

        """
	import math
	n = n - 1
	copy = list(elements)
	possible = math.factorial(len(elements))
	if n > possible:
		raise ValueError(str(n) + " > " + str(possible) + " (possible highest value)")
	elif n == possible:
		return [e for e in reversed(elements)]

	L = len(elements)
	ans = []
	for elementindex in range(L):
		if n ==0: # we hit the right permutation, end
			break
		min_permutation = math.factorial(L - elementindex - 1)
		if min_permutation > n:
			ans.append(copy.pop(0))
			continue
		elif min_permutation <= n:
			repeats = int(n / min_permutation)
			n = n % (repeats * min_permutation)
			ans.append(copy.pop(repeats))
	ans = ans + copy
	return ans

def check(numset):
	last = 0
	for i in range(1,math.factorial(len(numset))+1):
		val = int(''.join([str(n) for n in nth_permutation(numset,i)]))
		if val <= last:
			print(i,'value out of order:',val,'<=',last)
		else:
			print(i,':',val)
		last = val

ans = ''.join([str(n) for n in nth_permutation([i for i in range(10)],1000000)])
