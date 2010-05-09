def is_palindrome(num):
	s = str(num)
	if s == s[::-1]:
		return True
	else:
		return False

for s in range(1000, 0, -1):
	found = False
	for t in range(s, s-300, -1):
		if is_palindrome(s * t):
			print(s*t)
			found = True
			break
	if found:
		break