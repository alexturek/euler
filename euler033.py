from fractions import Fraction
import functools

def curious_fractions():
	"""Returns a list of curious fractions, less than one, of the form ab/bc == a/c"""
	L = []
	for p in itertools.product('0123456789',repeat=4):
		n2,d2 = int(''.join(p[:2])),int(''.join(p[2:]))
		n1,d1 = int(p[0]),int(p[3])
		# no zeroes allowed!
		if min((n1,n2,d1,d1)) == 0:
			continue
		f2,f1 = Fraction(n2,d2),Fraction(n1,d1)
		if f2 == f1 and p[1]==p[2] and n1 < d1:
			L.append(f2)
	return L

cf = list(set(curious_fractions()))
ans = functools.reduce(lambda x,y: x*y, cf).denominator
