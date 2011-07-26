'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from q3 import gen_primes

def q7():
	pg = gen_primes()
	for _ in range(10000):
		next(pg)
	print("10,001th prime:", next(pg))

if __name__ == "__main__":
	q7()