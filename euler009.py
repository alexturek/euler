import math

def find_triangle_sides(side1, perimeter):
	rem = perimeter - side1
	side2 = (rem * rem - side1 * side1) / rem / 2
	return float(side1), side2, perimeter - side1 - side2
    
def good_triple(a,b,c):
	if int(a) == a and int(b) == b and int(c) == c and a * a + b * b == c * c:
		return True
	else:
		return False

def find_py_triples(perimeter):
	ret = []
	for i in range(1,int(perimeter/2)):
		a,b,c = find_triangle_sides(i,perimeter)
		if good_triple(a,b,c):
			ret.append(tuple(sorted([n for n in (a,b,c)])))
	return list(set(ret))
