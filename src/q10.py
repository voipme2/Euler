'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from q3 import gen_primes

def q10():
    pg = gen_primes()
    sum = 0
    prime = next(pg)
    while(prime < 2000000):
        sum += prime
        prime = next(pg)
    
    print("Primes < 2M, summed:", sum)
    
if __name__ == "__main__":
    q10()