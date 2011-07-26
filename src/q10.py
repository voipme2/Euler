'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from q3 import gen_primes

def q10():
    '''
    Warning: this takes a long time to run.
    '''
    pg = gen_primes()
    sum = 0
    for i in range(2000000):
        sum += next(pg)
    
    print("First 2,000,000 primes, summed:", sum)
    
if __name__ == "__main__":
    q10()