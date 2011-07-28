'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all 
starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def get_sequence(num):
	seq = [num]
	if num == 1: return seq
	if num % 2 == 0:
		seq.extend(get_sequence(num / 2))
	else:
		seq.extend(get_sequence((3 * num) + 1))
	return seq

if __name__ == "__main__":
	start = 999999
	longest = 1
	terms = []
	for i in range(start, 1, -1):
		seq = get_sequence(i)
		if len(seq) > len(terms):
			terms = seq
			longest = i
	print("Longest:", i, "(", len(terms),"terms )")
