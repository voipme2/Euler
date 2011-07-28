'''
You are given the following information, but you may prefer to do some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a century unless 
	it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

normal_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
		"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def is_leap(year):
	if (repr(year)[2:] == "00"):
		return year % 400 == 0
	return year % 4 == 0

def day_of_week():
	# 0 = sunday
	d = 1
	while True:
		yield d
		if d == 6:
			d = 0
		else:
			d += 1

if __name__ == "__main__":
	dg = day_of_week()
	day = next(dg)
	year = 1900
	sundays = 0
	
	while year < 2001:
		leap = is_leap(year)
		days = normal_days
		if leap: days = leap_days
		
		for m in range(len(days)):
			for d in range(1, days[m] + 1):
				if (day == 0 and d == 1 and year >= 1901):
					sundays += 1
					print(d, months[m], year, weekdays[day])
				day = next(dg)
		year += 1

	print("Total sundays:", sundays)
