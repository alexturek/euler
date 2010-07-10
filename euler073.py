from factors import factorize

def all_fractions(denom, min_frac, max_frac):
    fractions = []
    numerators = [n for n in range(int(denom * min_frac)+1, int(denom * max_frac)+1)]
    for numer in numerators:
        fractions.append(numer/denom)
    if fractions[-1] >= max_frac:
        fractions.pop(-1)
    return fractions
    
# def fractions_between(denominator_range, fraction_range):
    # all_denominators = set(n for n in range(denominator_range[0], denominator_range[1]))
    # min_frac,max_frac = fraction_range
    # fractions = []
    # all_factors = set()
    # while len(all_denominators) > 0:
        # denom = max(all_denominators)
        # factors = set(factorize(denom))
        # fractions.extend(all_fractions(denom, min_frac, max_frac))
        # for f in factors:
            # all_denominators.discard(f)
            # all_factors.add(f)
    # return fractions
    
def max_factor_sieve(toprange):
    # have a 0 so we can do direct indexing
    max_factors = {i:set(factorize(i)[1:]) for i in range(toprange+1)}
    for top in max_factors:
        topfacs = factorize(top)
        for fac in topfacs[1:-1]:
            for mult in range(fac,top,fac):
                max_factors[mult].discard(fac)
    return {i:max_factors[i] for i in max_factors if len(max_factors[i]) > 0}
        
def fractions_between(denominator_range, fraction_range):
    min_denom,max_denom = denominator_range
    min_frac,max_frac = fraction_range
    divisors = max_factor_sieve(max_denom)
    good_fractions = []
    for denom in divisors:
        good_fractions.extend(all_fractions(denom, min_frac, max_frac))
    return good_fractions
        
ans = len(fractions_between((1,12000),(1/3, 1/2)))