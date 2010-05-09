alphabet = 'abcdefghijklmnopqrstuvwxyz'
values = {}
for i in range(len(alphabet)):
	values[alphabet[i]] = i + 1

with open('c:/dev/py/euler/names.txt') as f:
	allnames = f.read()

names = [eval(x) for x in allnames.split(',')]
names = sorted(names)

def get_alpha_value(name, valuedict):
	return sum([valuedict[letter] for letter in name.lower()])

ans = sum([(i+1) * get_alpha_value(names[i],values) for i in range(len(names))])
