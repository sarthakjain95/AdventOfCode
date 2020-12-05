
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	passes = f.readlines()

passes = [p.strip() for p in passes]

seat_ids = []

for pass_id in passes:
	
	l, h = 0, 127

	rows = pass_id[:7]
	cols = pass_id[-3:]

	delta = 128//2
	for r in rows:
		if r == "F": h -= delta
		elif r == "B": l += delta
		delta //= 2

	row = l

	l, h = 0, 7
	delta = 8//2
	for c in cols:
		if c == "R": l += delta
		elif c == "L": h -= delta
		delta//=2

	col = l

	seat_id = row * 8 + col
	seat_ids.append(seat_id)

print(f"Highest Seat Id is: {max(seat_ids)}")

missing_seats = []
for i in range(0, 128*8):
	if (i+1 in seat_ids) and (i-1 in seat_ids) and (i not in seat_ids):
		missing_seats.append(i)

missing_ids_str = ", ".join([*map(str, missing_seats)])
print(f"Missing Seat Id(s): {missing_ids_str}")
