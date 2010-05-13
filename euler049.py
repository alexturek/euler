import primes
from collections import defaultdict

pr = primes.generate_primes_up_to(10000)
d = defaultdict(list)

for p in pr:
    k = ''.join(sorted(str(p)))
    d[k].append(p)
    
keys = [k for k in d.keys()]

for k in keys:
    if len(d[k]) < 3:
        tmp = d.pop(k)
del tmp

for k in d:
    v = d[k]
    for x in range(len(v)):
        for y in range(x+1, len(v)):
            if (2 * v[y] - v[x]) in v:
                ans = ''.join((str(v[x]), str(v[y]), str(2 * v[y] - v[x])))
                break

ans