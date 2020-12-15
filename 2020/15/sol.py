
#! /usr/bin/env python

from pprint import pprint

starting_numbers = [2,0,1,9,5,19]

series = []
seen_map = {}
i = 0

for idx in range(len(starting_numbers)):

	n = starting_numbers[idx]
	series.append(n)
	seen_map[n] = [idx]
	i += 1


LIMIT = 2020

while len(series) < LIMIT:

	last_spoken = series[-1]
	new_num = -1

	if last_spoken in seen_map:
		if len(seen_map[last_spoken]) == 1: new_num = 0
		else: new_num = seen_map[last_spoken][-1] - seen_map[last_spoken][-2]
	else:
		new_num = 0
		seen_map[last_spoken] = [i-1]

	if new_num not in seen_map: seen_map[new_num] = [i]
	else: seen_map[new_num].append(i)

	series.append(new_num)
	i+=1

print(f"Number spoken at {i} is {series[-1]}")
