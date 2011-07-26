'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

from math import floor, sqrt

# taken from http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

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
