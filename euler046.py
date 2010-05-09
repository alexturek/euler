import primes

pr = primes.generate_primes_up_to(1000)

def is_sum_prime_and_double_square(n):
    for p in pr[1:]:
        if p > n:
            return False
        root = sqrt(((n - p)/2))
        if int(root) == root:
            return True
    return False

def is_composite_and_odd(n):
    return not(p in pr or p % 2 == 0)

