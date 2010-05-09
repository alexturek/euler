def rule(n):
	iterations = 0
	while n != 1:
		iterations = iterations + 1
		if n%2 == 0:
			n = int(n / 2)
		else:
			n = 3 * n + 1
	return iterations

def find_max_collatz(maxnum):
	import time
	then = time.clock()
	m = 1
	for i in range(1000000,1,-1):
		n = rule(i)
		if n > m:
			print(i,':',n)
			m = n
	now = time.clock()
	print('finished in',str(now-then),'seconds.')
