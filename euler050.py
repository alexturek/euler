import primes
def longest_sum_subsequence(max_prime):
    max_prime_to_try = int(max_prime / 2)
    pr_trials = primes.generate_primes_up_to(max_prime_to_try)
    pr_sums = list(pr_trials)
    pr_set = set(primes.generate_primes_up_to(max_prime))
    lcs = 1,2
    i = 1
    while len(pr_sums) > 1 and pr_sums[0] < max_prime:
        #print('iterating',i,pr_sums)
        for L in range(len(pr_sums)-1):
            pr_sums[L] = pr_sums[L] + pr_trials[L + i]
        cutoff = -1
        for S in pr_sums[::-1]:
            if S > max_prime:
                cutoff = cutoff - 1
            if S in pr_set:
                lcs = i,S
        pr_sums = pr_sums[:cutoff]
        i = i + 1
    return lcs
 
ans = longest_sum_subsequences(1000000)