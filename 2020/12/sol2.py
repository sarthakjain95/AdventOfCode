

#! /usr/bin/env python

with open("input.txt", 'r') as f:
	content = f.readlines()

instructions = [c.strip() for c in content]
instructions = [(c[0], int(c[1:])) for c in instructions]

waypoint = [1, 10]
current_position = [0, 0]


def update_waypoint(wp, d, mag):
	
	if d == "N": wp[0] += mag
	elif d == "S": wp[0] -= mag
	elif d == "W": wp[1] -= mag
	elif d == "E": wp[1] += mag


def update_position(pos, wp, mag):
	
	pos[0] += wp[0] * mag	
	pos[1] += wp[1] * mag


def rotate_waypoint(w, ins, mag): # 0, 90, 180, 270
	
	clockwise_choices = [[-w[1], w[0]], [-w[0], -w[1]], [w[1], -w[0]]] 
	anticlockwise_choices = [[w[1], -w[0]], [-w[0], -w[1]], [-w[1], w[0]]]
	mapped_mag = (mag-90)//90
	
	if ins == "L":
		w[:] = anticlockwise_choices[mapped_mag]
	elif ins == "R":
		w[:] = clockwise_choices[mapped_mag]


for instruction in instructions:

	ins, mag = instruction

	if ins in ["N", "W", "E", "S"]:
		update_waypoint(waypoint, ins, mag)
	elif ins in ["F", "B"]:
		update_position(current_position, waypoint, mag)
	elif ins in ["L", "R"]:
		rotate_waypoint(waypoint, ins, mag)

print(f"Final position: {current_position}")
manhattan_distance = sum([abs(current_position[0]), abs(current_position[1])])
print(f"Manhattan Distance from start point to end point: {manhattan_distance} (correct:{manhattan_distance==89936})")
