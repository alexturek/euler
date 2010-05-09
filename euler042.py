def triangle_number(n):
	return (n * (n + 1)) >> 1

def make_lettermap():
	ret = {}
	val = 1
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		ret[letter] = val
		val += 1
	return ret

def word_value(word, lettermap):
	value = 0
	for letter in word:
		value += lettermap[letter.lower()]
	return value

def find_triangle_words(words):
	lettermap = make_lettermap()
	trianglemax = 0
	triangles = set()
	total = 0
	for word in words:
		val = word_value(word, lettermap)
		while trianglemax < val:
			trianglemax = triangle_number(len(triangles))
			triangles.add(trianglemax)
		if val in triangles:
			total += 1
	return total

with open(r"""C:\Documents and Settings\Tony Turek\Desktop\My Dropbox\d_dev\py\euler""".replace('\\','/') + '/words.txt') as f:
	data = f.read()

words = data.replace('"','').split(',')

ans = find_triangle_words(words)
