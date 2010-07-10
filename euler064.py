from repeated_fraction import repeated_fraction_sqrt_period
    
ans = sum(1 for i in range(1,10001) if repeated_fraction_sqrt_period(i) % 2 == 1)