'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

from math import floor, sqrt
from euler import gen_primes

def q3():
    """
	Uses the trial division method in order to find
	the prime factors.
	"""
    num = 600851475143
    pg = gen_primes()
    prime = next(pg)

    # keep track of all the factors
    factors = []

    # no need to go larger than sqrt(num)
    while (prime < floor(sqrt(num))):
        if (num % prime == 0):
            factors.append(prime)
        prime = next(pg)

    return factors

if __name__ == "__main__":
    factors = q3()
    print("Factors:", factors)
    print("Largest:", factors[-1])
