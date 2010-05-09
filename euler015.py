def path_count_grid(grid_size):
	row = [0] + [1 for i in range(grid_size)]
	for i in range(grid_size-1):
		prev_row = row
		row = [2 * prev_row[1]]
		for j in range(len(prev_row)-2):
			row.append(row[-1] + prev_row[j+2])
	return 2*row[1]
