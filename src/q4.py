'''
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 � 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(num):
	one = list(repr(num))
	two = list(repr(num))
	two.reverse()
	if (one == two):
		return True
	return False

def q4():
	largest = 0
	for x in range(100,1000):
		for y in range(100, 1000):
			prod = x * y
			if (is_palindrome(prod) and prod > largest):
				largest = prod
	print("Largest:", largest)

if __name__ == "__main__":
	q4()