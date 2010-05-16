def fac(n):
    for i in range(1,n):
        n = n * i
    return n

def max_combinations(select, _from):
    if select == 0 or select >= _from:
        return 1
    return max(1,int(fac(_from) / fac(select) / fac(_from - select)))

def num_combos_over(base,min_combos):
    return sum(1 for i in range(1,base+1) if max_combinations(i,base) > min_combos)

ans = sum(num_combos_over(base, 1000000) for base in range(1,101))
