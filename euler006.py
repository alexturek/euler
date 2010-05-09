import math

highnum = 101

sum_of_squares = sum(m * m for m in range(highnum))
square_of_sums = math.pow(sum([m for m in range(highnum)]),2)

ans = square_of_sums - sum_of_squares
