
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	content = f.readlines()

instructions = [c.strip() for c in content]
instructions = [(c[0], int(c[1:])) for c in instructions]

direction_change_map = {
	"L": {
		"N": {90: "W", 180: "S", 270: "E"},
		"E": {90: "N", 180: "W", 270: "S"},
		"W": {90: "S", 180: "E", 270: "N"},
		"S": {90: "E", 180: "N", 270: "W"}
	},
	"R": {
		"N": {90: "E", 180: "S", 270: "W"},
		"E": {90: "S", 180: "W", 270: "N"},
		"W": {90: "N", 180: "E", 270: "S"},
		"S": {90: "W", 180: "N", 270: "E"}
	},
}

opposites = {
	"N": "S",
	"S": "N",
	"W": "E",
	"E": "W"
}

current_position = [0, 0]
direction = "E"

def update_direction(pos, d, mag):

	if d == "N": pos[0] += mag
	elif d == "S": pos[0] -= mag
	elif d == "W": pos[1] -= mag
	elif d == "E": pos[1] += mag

for instruction in instructions:

	ins, mag = instruction

	if ins in ["L", "R"]:
		direction = direction_change_map[ins][direction][mag]
	else:
		if ins in ["F", "B"]:
			d = direction if ins == "F" else opposites[direction]
			update_direction(current_position, d, mag)
		else:
			update_direction(current_position, ins, mag)

manhattan_distance = sum([abs(current_position[0]), abs(current_position[1])])
print(f"Manhattan distance from start point to final location: {manhattan_distance} (correct:{manhattan_distance==1838})")
