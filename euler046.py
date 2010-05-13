import primes

def get_non_goldbachs(maxnum):
    pr = primes.generate_primes_up_to(maxnum)
    nums_sqrd = {2*(x**2) for x in range(1,int((maxnum/2)**0.5))}
    non_goldbachs = []
    for n in range(3,maxnum,2):
        composite = n not in prset
        if composite:
            for p in pr:
                diff = n - p
                if diff < 0:
                    non_goldbachs.append(n)
                    break
                if diff in nums_sqrd:
                    break
    return non_goldbachs
    
ans = non_goldbachs[1000000][0]