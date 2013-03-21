#!/usr/bin/env python

import sys

def max_path(triangle):

	index = 0
	total = 0
	for row in triangle:
		print row
		if len(row) == 1:
			amt = row[0]
		else:
			l,r = index, (index + 1)
			if index < 0:
				l = index - 1
			if r > len(row):
				r = len(row)
			amt = max(int(row[l]), int(row[r]))
			index = row.index(amt)
		total += amt
	return total

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Need a file"
	else:
		triangle = []
		for l in open(sys.argv[1]):
			triangle.append(map(lambda x: int(x), l.split(" ")))
		print "Maximal path value %d" % max_path(triangle)