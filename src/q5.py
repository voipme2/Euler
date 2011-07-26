'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def q5():
	"""
	I feel like this function could probably be a bit more efficient.
	For now, we're using short-circuit logic
	"""
	nums = range(1,21)
	smallest = None

	# start at the given number
	current = 2520
	while (smallest == None):
		divisible = True
		for i in nums:
			if divisible:
				divisible = (current % i == 0)
		if divisible:
			smallest = current
		else:
			current += 20

	print("Smallest:", smallest)

if __name__ == "__main__":
	q5()