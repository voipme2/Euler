'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

from functools import reduce

if __name__ == "__main__":
    huge = repr(2 ** 1000)
    print("Summed digits:", reduce(lambda x,y: int(x)+int(y),huge))