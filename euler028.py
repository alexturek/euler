def sum_spiral_diags(spiral_width):
	total = 1
	last = 1
	for ring in range(int(spiral_width/2)):
		incr = (ring + 1) * 2
		total += sum([corner * incr + last for corner in range(1,5)])
		last = 4 * incr + last
	return total

ans = sum_spiral_diags(1001)
