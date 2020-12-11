
#! /usr/bin/env python

from pprint import pprint

with open("input.txt", 'r') as f:
	seats = f.readlines()

grid = [list(s.strip()) for s in seats]

def is_valid_coord(y, x, limy, limx):
	if y < 0 or y >= limy:
		return False
	if x < 0 or x >= limx:
		return False 
	return True

def occupied_seats_around(y, x, grid):

	limy, limx = len(grid), len(grid[0])
	visible_filled_seats = 0

	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:

			if i == 0 and j == 0:
				continue

			cy, cx = y+i, x+j
			is_filled = False
			while is_valid_coord(cy, cx, limy, limx):
				if grid[cy][cx] == "L":
					break
				elif grid[cy][cx] == "#":
					is_filled = True
					break
				cy, cx = cy+i, cx+j

			visible_filled_seats += is_filled

	return visible_filled_seats

def update_grid(grid):

	updated_grid = [[grid[j][i] for i in range(len(grid[0]))] for j in range(len(grid))]

	for y in range(len(grid)):
		for x in range(len(grid[0])):

			if grid[y][x] == '.':
				continue
			elif grid[y][x] == 'L' and occupied_seats_around(y, x, grid) == 0:
				updated_grid[y][x] = '#'
			elif grid[y][x] == '#' and occupied_seats_around(y, x, grid) >= 5:
				updated_grid[y][x] = 'L'
			else:
				updated_grid[y][x] = grid[y][x]

	return updated_grid

flatten = lambda grd: ''.join([''.join(g) for g in grd]) 

updated_grid = update_grid(grid)
updated_grid_hash = flatten(updated_grid)
grid_hash = flatten(grid)

while updated_grid_hash != grid_hash:
	grid = updated_grid
	updated_grid = update_grid(grid)
	updated_grid_hash = flatten(updated_grid)
	grid_hash = flatten(grid)
	# pprint([''.join(g) for g in grid])

occupied_seats = 0
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == '#':
			occupied_seats += 1

print(f"Total occupied seats: {occupied_seats}")
