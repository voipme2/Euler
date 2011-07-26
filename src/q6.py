'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 ? 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
'''

from functools import reduce

def q6():
	""" Lambdas and reduce are nice. """
	adder = lambda x,y: x+y
	sum_of_square = reduce(adder, [i * i for i in range(1,101)])
	square_of_sum = pow(reduce(adder, range(1,101)), 2)
	print("Difference:", square_of_sum - sum_of_square)

if __name__ == "__main__":
	q6()