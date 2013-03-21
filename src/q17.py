#!/usr/bin/env python

nums = { "1": "one", "2": "two", "3": "three", "4": "four",
	"5": "five", "6": "six", "7": "seven", "8": "eight",
	"9": "nine", "10": "ten", "11": "eleven",
	"12": "twelve", "13": "thirteen", "14": "fourteen",
	"15": "fifteen", "16": "sixteen", "17": "seventeen",
	"18": "eighteen", "19": "nineteen", "20": "twenty",
	"30": "thirty", "40": "forty", "50": "fifty",
	"60": "sixty", "70": "seventy", "80": "eighty",
	"90": "ninety"}

endings = ["", "thousand", "million", "billion", "trillion"]

def convert_to_letters(num):
	num = str(num)

	converted = ""
	end_index = 0
	sp = chunks(num[::-1],3)
	
	while(True):
		try:
			converted = parse_triple(sp.next()[::-1]) + " " + endings[end_index] + " " + converted
			end_index += 1
		except StopIteration:
			break

	return converted

def chunks(l,n):
	"""
	Generator function (from StackOverflow) that splits a list into evenly sized chunks.
	"""
	for i in range(0, len(l), n):
		yield l[i:i+n]

def parse_triple(num, needs_and=False):
	"""
	Converts a given max 3 digit number into English.
	"""
	parsed = ""
	num = num.lstrip("0")

	if num == parsed:
		return parsed

	if len(num) == 3:
		parsed = parse_triple(num[0]) + " hundred " + parse_triple(num[1:], True)
	elif len(num) == 2 and int(num) > 20:
		if needs_and:
			parsed = "and "
		parsed = parsed + nums[str(int(num[0]) * 10)] + " " + parse_triple(num[1])
	elif len(num) == 1 or int(num) <= 20:
		if needs_and:
			parsed = "and "
		parsed = parsed + nums[num]

	return parsed

if __name__ == "__main__":
	letters = ""
	for i in range(1,1001):
		letters = letters + convert_to_letters(i)
	
	letters = letters.replace(' ', '')
	print "1 to 1000: %d " % len(letters)
	
	