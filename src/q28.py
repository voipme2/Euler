#!/usr/bin/env python
# 


if __name__ == "__main__":
	nums = [1]
	for s in range(1,1002,2):
		if s > 1:
			nums.append(s**2)
			nums.append((s**2) - (s - 1))
			nums.append((s**2) - (s - 1)*2)
			nums.append((s**2) - (s - 1)*3)
	
	print "Sum of diagonals: %d" % sum(nums)	