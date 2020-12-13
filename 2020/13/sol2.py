
#! /usr/bin/env python

from pprint import pprint

with open("input.txt", 'r') as f:
	content = f.readlines()[1]

content = content.strip().replace("x", "-1").split(",")
bus_times = list(map(int, content))

timings = []
for i in range(len(bus_times)):
	if bus_times[i] == -1:
		continue
	timings.append((bus_times[i], i))

start_value = timings[0][0]
factor = start_value
# print("timings", timings)

for i in range(1, len(timings)):

	t, delta = timings[i]
	dx = start_value

	if (start_value+delta) % t == 0:
		continue
	
	while True:
		dx += factor
		if (dx+delta) % t == 0:
			start_value = dx
			break

	factor *= t

# print(start_value)
print(f"Start time: {start_value} (correct:{start_value==225850756401039})")
