
#! /usr/bin/env python

from math import ceil

with open("input.txt", 'r') as f:
	content = f.readlines()

content = [c.strip() for c in content]

arrival = int(content[0])
bus_times = content[1].split(',')
bus_times = [int(t) for t in list(filter(lambda x: x!='x', bus_times))] 
print(bus_times)

earliest_bus_id = bus_times[0]
earliest_arrival_delta = ceil(arrival/earliest_bus_id)*earliest_bus_id - arrival

for t in bus_times:
	ax = ceil(arrival/t)*t
	if (ax-arrival) < earliest_arrival_delta:
		earliest_bus_id = t
		earliest_arrival_delta = ax-arrival

# print(earliest_arrival_delta)
ans = earliest_arrival_delta * earliest_bus_id
print(f"Product is {ans} (correct:{ans==2406})")
