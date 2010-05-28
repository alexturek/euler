import math
import fractions

def find_closest_smaller_fraction(max_denom, target_fraction):
	target_n,target_d = target_fraction
	frac = target_n/target_d
	ans = 0
	for d in range(2,max_denom+1):
		absolute = d * frac
		min_num = math.floor(absolute)
		max_num = math.ceil(absolute)
		#print(absolute,min_num,max_num,'out of',d)
		for n in range(min_num, max_num):
			if n/d < frac:
				ans = max(fractions.Fraction(n,d),ans)
	return ans
    
ans = find_closest_smaller_fraction(1000000,(3,7)).numerator