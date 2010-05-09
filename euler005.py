def LCM(highnum):
	if highnum > 1:
		incr = LCM(highnum - 1)
		x = incr
		allnums = [m for m in range(1,highnum)]
		while len([d for d in allnums if x % d != 0]) > 0:
			x = x + incr
		return x
	else:
		return 1
