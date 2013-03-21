#!/usr/bin/env python

def is_amicable(a,b):
	return dsum(a) == b and dsum(b) == a and a != b

def dsum(n):
	return reduce(lambda x,y: x + y, divisors(n), 0)

def divisors(n):
	return [ i for i in range(1,n) if n % i == 0 ]

if __name__ == "__main__":
	amicable = [ for i in range(2,10000) if is_amicable(i, dsum(i))]
	print "Sum of amicable under 10000: %d" % reduce(lambda x,y: x + y, amicable)