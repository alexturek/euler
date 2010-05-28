from collections import defaultdict
powers = defaultdict(list)

for i in range(1,10):
	for j in range(1,1000):
		powers[i**j].append(j)
        
ans = sum([1 for k in powers if len(str(k)) in powers[k]])