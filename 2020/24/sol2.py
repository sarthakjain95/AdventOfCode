
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

y_limits = [0, 0] # max, min
x_limits = [0, 0] # max, min

for tile_location in tiles:

	loc = [0, 0]
	tile = tile_location

	while len(tile):

		if loc[0] > y_limits[0]:
			y_limits[0] = loc[0]
		elif loc[0] < y_limits[1]:
			y_limits[1] = loc[0]

		if loc[1] > x_limits[0]:
			x_limits[0] = loc[1]
		elif loc[1] < x_limits[1]:
			x_limits[1] = loc[1]

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


def flip_tiles(grid_size, black_tiles):

	y_lims, x_lims = grid_size
	new_black_tiles = set()

	y = y_lims[1]
	while y < y_lims[0]+1:

		x = x_lims[1]
		while x < x_lims[0]+1:

			adjacent_black_tiles = 0
			loc = [y, x]

			for d in direction_map:
				mov = direction_map[d]
				if (loc[0]+mov[0], loc[1]+mov[1]) in black_tiles:
					adjacent_black_tiles += 1

			if (y, x) in black_tiles:
				if adjacent_black_tiles in [1, 2]:
					new_black_tiles.add((y, x))
			else:
				if adjacent_black_tiles == 2:
					new_black_tiles.add((y, x))

			x += 0.5

		y += 1.0

	return new_black_tiles


iterations = 100
grid_size = [y_limits, x_limits]
grid_size = [
	[grid_size[0][0]+1, grid_size[0][1]-1],
	[grid_size[1][0]+0.5, grid_size[1][1]-0.5]
]

for i in range(iterations):
	black_tiles = flip_tiles(grid_size, black_tiles)
	grid_size = [
		[grid_size[0][0]+1, grid_size[0][1]-1],
		[grid_size[1][0]+0.5, grid_size[1][1]-0.5]
	]

print(f"Total black tiles after day {iterations} : {len(black_tiles)}")
