def max_solutions_for_triangle_perimeter_range(max_perimeter):
	"""Returns the perimeter p that has the most integral side solutions for right triangles, for p <= max_perimeter"""
	import euler009
	import functools
	perimeter_solutions = []
	for p in range(1, max_perimeter+1):
		perimeter_solutions.append((p,len(euler009.find_py_triples(p))))
	def max_solutions_perimeter(a,b):
		if a[1] > b[1]:
			return a
		return b
	return functools.reduce(max_solutions_perimeter, perimeter_solutions)[0]

ans = max_solutions_for_triangle_perimeter_range(1000)
