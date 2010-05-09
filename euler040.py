import math
import functools

digits = ''.join([str(i) for i in range(1,1000001)])

ans = functools.reduce(lambda a,b: a*b, [int(digits[int(math.pow(10,s))-1]) for s in range(7)])
