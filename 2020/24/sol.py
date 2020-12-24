
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	content = f.readlines()

tiles = [c.strip() for c in content]

black_tiles = set()
direction_map = {
	"e" : [0., 1.],
	"se": [-1., 0.5],
	"sw": [-1., -0.5],
	"w" : [0., -1.],
	"nw": [1., -0.5],
	"ne": [1., 0.5]
}
flipped_ones = 0
flipped_twice = 0

for tile_location in tiles:

	loc = [0, 0]
	tile = tile_location

	while len(tile):

		if tile[:2] in direction_map:
			mov = direction_map[tile[:2]]
			tile = tile[2:]
		elif tile[0] in direction_map:
			mov = direction_map[tile[0]]
			tile = tile[1:]
		else:
			raise NotImplementedError

		loc = [loc[0]+mov[0], loc[1]+mov[1]]

	loc = tuple(loc)

	if loc in black_tiles:
		black_tiles.remove(loc)
		flipped_twice += 1
		flipped_ones -= 1
	else:
		black_tiles.add(loc)
		flipped_ones += 1

# print(black_tiles)
print(len(black_tiles))
print(flipped_ones, flipped_twice)
