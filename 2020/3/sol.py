
#! /usr/bin/env python

with open("input.txt",'r') as f:
	m = f.readlines()

forest_map = [x.strip() for x in m]

block_height = len(forest_map)
block_width = len(forest_map[0])

print("*---- TEST 1 ---------------*")
print(f"Block size: {block_height}h x {block_width}w")
print(forest_map[0])

level = 0
pos = [0, 0]
trees_encountered = 0


while level < block_height:

	new_pos = [pos[0] + 1, pos[1]+3]
	level += 1
	pos = new_pos

	if forest_map[new_pos[0]%block_height][new_pos[1]%block_width] == "#":
		trees_encountered += 1

print(f"Total trees encountered: {trees_encountered}")


def check_slope(block, slope):

	h, w = len(block), len(block[0])
	
	level = 0
	pos = [0, 0]
	trees_encountered = 0
	slope = slope[::-1] # x,y to y,x

	while level < h:

		new_pos = [pos[0]+slope[0], pos[1]+slope[1]]
		level += 1
		pos = new_pos

		if pos[0] < h: 
			if block[new_pos[0]%block_height][new_pos[1]%block_width] == "#":
				trees_encountered += 1

	return trees_encountered

slopes = [
	[1, 1],
	[3, 1],
	[5, 1],
	[7, 1],
	[1, 2]
]

encounters = []

for slope in slopes:
	encounters.append(check_slope(forest_map, slope))

print("*---- TEST 2 ---------------*")
print(encounters)
reduced_result = 1
for e in encounters:
	reduced_result *= e

print(f"Reduced result for all slopes: {reduced_result}")
