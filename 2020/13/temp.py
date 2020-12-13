
#! /usr/bin/env python

from pprint import pprint
from math import ceil

bus_times = [67, 7, 59, 61]

last_digits = []
for i in bus_times:
	digits = []
	for j in range(1, 11):
		digits.append(int(str(j*i)[-1]))
	last_digits.append(digits)

pprint(last_digits)

for i in range(1, 1000000):
	if i%67==0 and (i+1)%7==0 and (i+2)%59==0 and (i+3)%61==0:
		print(i)
		break

print(754018 - (67*7*59)*27)
print(6901 - (67*7)*14)
