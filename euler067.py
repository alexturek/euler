import euler018

def make_pyramid(data):
	return [[int(node) for node in line.split(' ')] for line in data.split('\n')]
    
with open('/dev/py/euler/triangle.txt') as f:
	ans = euler018.max_path(make_pyramid(f.read().strip()))