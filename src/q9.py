'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt

def q9():
	possibles = []
	# go to 500, since a and b have to be less than c
	for x in range(1, int(sqrt(501))):
		for y in range(1, int(sqrt(501))):
			possibles.append((x,y))
	a, b, c = 0, 0, 0
	solved = False
	for m,n in possibles:
		ta = m*m - n*n
		tb = 2 * m * n
		tc = m * m + n * n
		if (ta + tb + tc == 1000) and (ta*ta + tb*tb == tc*tc):
			solved = True
			a, b, c = ta, tb, tc
	if solved:
		print("Answer:", a * b * c)

if __name__ == "__main__":
	q9()