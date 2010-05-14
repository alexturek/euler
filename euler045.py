def tri(n):
	return int(n*(n+1)/2)
    
def pent(n):
	return int(n*(3*n - 1)/2)
    
def hexag(n):
	return int(n*(2*n - 1))
    
maxrange = int(1e6)

isections = {tri(n) for n in range(maxrange)}.intersection({pent(n) for n in range(maxrange)}).intersection({hexag(n) for n in range(maxrange)})

ans = sorted(isections)[-1]