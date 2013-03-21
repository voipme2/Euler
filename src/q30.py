#!/usr/bin/env python

def is_fifth_sum(num):
	return num == reduce(lambda x,y: int(x) + int(y) ** 5, str(num), 0)

if __name__ == "__main__":
	nums = []
	# testing shows that the max is less than 200000
	for i in range(2,200000):
		if is_fifth_sum(i):
			print "%d - %s" % (i, ' + '.join([ s + "^5" for s in str(i)]))
			nums.append(i)

	print "Sum of all of them: %d" % reduce(lambda x,y: x+y, nums)