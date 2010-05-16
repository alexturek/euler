def numeric_palindrome(n):
	return int(''.join(reversed(str(n))))

def is_lychrel(n, max_iterations):
	palin = numeric_palindrome(n)
	stop = 0
	while True:
		n = n + palin
		palin = numeric_palindrome(n)
		stop += 1
		#print(stop,n, palin, n==palin)
		if palin == n or stop > max_iterations:
			break
	return palin != n

ans = sum(1 for n in range(1,10000) if is_lychrel(n, 50))	
