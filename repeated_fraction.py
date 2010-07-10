from math import floor, sqrt

def _repeat_frac_sqrt_iter(Asqrt, A, Dn, Rn):
    """Returns an iteration of a repeated fraction I,D,R, in the form:

    sqrt(A) ~= I + (Asqrt + R)/D

    where
    A is the number whose square root we are trying to approximate
    Asqrt is the square root of A
    Dn is the denominator of the last iteration's fraction
    Rn is the rational component of the last iteration's fractional numerator

    This returns I,D,R
    I is the integral part of the next iteration
    D is the denominator of the next iteration's fractional part
    R is the integer remainder of the next iteration's fractional part

    _repeat_frac_sqrt_iter(float, int, int, int) -> int, int, int
    """
    D = floor((A - Rn**2) / Dn)
    I = floor((Asqrt-Rn)/D)
    R = -Rn - D * I
    return I,D,R
    
def repeated_fraction_sqrt(val, precision):
    """Returns a repeating fraction approximation of a square root, out to some number of iterations.

    repeated_fraction_sqrt(int, int) -> list
    """
    A = sqrt(val)
    D = 1
    I = floor(A)
    R = -I
    ans = [I]
    for i in range(precision):
        I,D,R = _repeat_frac_sqrt_iter(A, val, D, R)
        ans.append(I)
    return ans
    
def repeated_fraction_sqrt_period(val):
    A = sqrt(val)
    # Did you give me a square of an integer? return 0
    if int(A) == A:
        return 0
    D = Fraction('1')
    I = floor(A)
    R = -I
    i = 0
    I,D,R = _repeat_frac_sqrt_iter(A,D,R)
    found_before = {}
    while (R,D) not in found_before:
        found_before[(R,D)] = i
        I,D,R = _repeat_frac_sqrt_iter(A,D,R)
        i += 1
    return i - found_before[(R,D)]