def makefibsequence(highnum):
	fibs = [1,2]
	for i in range(2,highnum):
		fibs.append(sum(fibs[-2:]))
	return fibs

ans = sum([m for m in makefibsequence(40) if m % 2 == 0 and m < 4000000])
