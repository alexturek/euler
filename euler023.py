import math
def factorize(num):
	factors = []
	for i in range(1, num>>1):
		if i > num / i:
			break
		if num % i == 0:
			factors.append(i)
			if num/i != i:
				factors.append(int(num/i))
	return sorted(factors)

def abundant_num(n):
	if sum(factorize(n)[:-1]) > n:
		return True
	return False

def find_sum_nums(nums1, nums2, max_sum):
	sum_nums = {}
	for n in nums1:
		for m in nums2:
			if m + n < max_sum:
				sum_nums[m+n] = 1
	return set(sum_nums.keys())

abundant_nums = [n for n in range(1,28123) if abundant_num(n)]

sum_abu_nums = find_sum_nums(abundant_nums,abundant_nums,28124)

ans = sum([i for i in range(1,28123) if i not in sum_abu_nums])
