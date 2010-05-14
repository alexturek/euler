def key(n):
	return ''.join(sorted(str(n)))
    
def minmax(digitsize, divisor):
	min_n = int(eval('1e' + str(digitsize-1)))
	max_n = int(eval('1e' + str(digitsize))/divisor)
	return min_n, max_n
    
def digit_keeper(maxdigits, *mults):
	digits = 2
	while True:
		min_n,max_n = minmax(digits, max(mults))
		print(min_n, max_n, "for digits",digits)
		for i in range(min_n, max_n+1):
			k = key(i)
			found = True
			for m in mults:
				if key(m * i) != k:
					found = False
					break
			if found:
				return i
		digits = digits + 1
		if digits > maxdigits:
			print('no numbers found')
			break
            
ans = digit_keeper(6,2,3,4,5,6)