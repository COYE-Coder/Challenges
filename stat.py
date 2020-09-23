"""
You are the "computer expert" of a local Athletic Association (C.A.A.). 
Many teams of runners come to compete. 
Each time you get a string of all race results of every team who has run. 
For example here is a string showing the individual results of a team of 5 runners:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

Each part of the string is of the form: 
	h|m|s 

To compare the results of the teams you are asked for giving three statistics:
 - Range
 - Median
 - Mean
 
Your task is to return a string giving these 3 values. 
	For the example given above, the string result will be

	"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

	of the form:

	"Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"

	where hh, mm, ss are integers (represented by strings) with each 2 digits.

"""
import time


def get_sec(hh, mm, ss):
	return int(hh) * 3600 + int(mm) * 60 + int(ss)


def get_hhmmss(sec):
	return time.strftime('%H|%M|%S', time.gmtime(sec))


def stat(strng):
	if not strng:
		return ''
	# Create a nested list such that every 3rd element corresponds to HH, MM, or SS:
	times = list(map(lambda x: x.split('|'), strng.split(', ')))

	times_sec = []

	for t in times:
		times_sec.append(get_sec(t[0], t[1], t[2]))

	times_sec.sort()

	# Find range and max
	rng = times_sec[-1] - times_sec[0]
	mn = sum(times_sec) / len(times_sec)

	# Find median is more complex
	_num = len(times_sec)

	# If there are an even number of runners
	if _num % 2 == 0:
		med = (times_sec[_num // 2] + times_sec[(_num - 1) // 2]) / 2

	# If there an odd number of runners
	else:
		med = times_sec[_num // 2]

	# Throw all into list
	rng_mean_med = [rng, mn, med]

	result = []
	for val in rng_mean_med:
		result.append(get_hhmmss(val))

	return "Range: " + result[0] + 
			" Average: " + result[1] + 
			" Median: " + result[2]




strng = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"
print(stat(strng))













