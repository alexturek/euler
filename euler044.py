def pent(n):
	return int(n*(3*n - 1)/2)
    
def find_pent_pair(max_n):
	pents = [pent(n) for n in range(1,max_n)]
	pentset = set(pents)
	length = len(pents)
	for j in range(length):
		for k in range(j+1,length):
			J = pents[j]
			K = pents[k]
			d = K - J
			s = J + K
			if d in pentset and s in pentset:
				print(J,'+',K,'=',s,s == J+K)
				print(J,'-',K,'=',d,d == K-J)
				print(s,"in pents", s in pents)
				print(d,"in pents", d in pents)
				return d
            
ans = find_pent_pair(10000)