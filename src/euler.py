'''
Contains some functions that I've used a few times.
'''
import sys
from functools import reduce

# taken from http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
def gen_primes():
    """ 
    Generate an infinite sequence of prime numbers.
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

def trial_division(n):
    '''
    Simple trial division algorithm.
    Taken from wikipedia.
    '''
    if n == 1: return [1]
    pg = gen_primes()
    p = next(pg)
    prime_factors = []
    while(p < (int(n**0.5) + 1)):
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
        p = next(pg)
    if n > 1: prime_factors.append(n)
    return prime_factors

def count_p_factors(pfacts):
    '''
    Counts the number of factors when given a list of
    prime factors.  
    
    We calculate this by taking all of the
    exponents from the primes, adding one, then multiplying
    them all together.
    '''
    facts = {}
    for p in pfacts:
        if not p in facts:
            facts[p] = 1
        facts[p] += 1

    if len(facts.keys()) > 0:
        return reduce(lambda x,y: x*y, facts.values())
    return 1
    

def triangles():
    '''
    Simple generator for getting triangle numbers.
    
    1 = 1
    3 = 1 + 2
    6 = 1 + 2 + 3
    10 = 1 + 2 + 3 + 4
    etc.
    '''
    n = 1
    total = 1
    while True:
        yield total
        n += 1
        total += n

def pascal(rows):
    '''
    Returns a list of lists, which represent Pascal's triangle.

    pascal(5):
    [
     [1],
     [1, 1],
     [1, 2, 1],
     [1, 3, 3, 1],
     [1, 4, 6, 4, 1]
    ]
    '''
    triangle = []
    for row in range(rows): 
        s = 1
        slist = [s]
        for v in range(row):
            s = s * (row - v) * 1 / (v + 1)
            slist.append(int(s))
        triangle.append(slist)
    return triangle

def max_tri(triangle):
    triangle.reverse()
    for r_i in range(len(triangle) - 1):
        row = triangle[r_i]
        next_row = triangle[r_i + 1]
        for i in range(len(row) - 1):
            next_row[i] += max(row[i], row[i+1])
    return triangle[-1][0]

def parse_triangle(f):
    tri = []
    for l in f:
        tri.append([int(n) for n in l.strip().split(" ") if len(n) > 0])
    return tri
  
def solve_triangle(f):
    return max_tri(parse_triangle(f))   
    