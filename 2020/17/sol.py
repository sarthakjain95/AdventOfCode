
#! /usr/bin/env python

import numpy as np
from pprint import pprint

with open("input.txt", 'r') as f:
	content = f.read()

content = content.replace('.', '0').replace('#', '1').split('\n')
INIT_SIZE = len(content[0])
grid = list(map(lambda x: list(map(int, list(x))), content))
grid = np.array(grid).astype(np.bool).reshape((1, INIT_SIZE, INIT_SIZE))

iters = 6

x = INIT_SIZE + 2 * iters
y = INIT_SIZE + 2 * iters
z = 1 + 2 * iters

final_grid = np.zeros((z, x, y)).astype(np.bool)
i = iters
final_grid[i:i+1, i:i+INIT_SIZE, i:i+INIT_SIZE] = grid

is_valid_crd = lambda c, l: all([c[o]>=0 and c[o]<l[o] for o in range(len(l))])

for i in range(iters):

	new_grid = np.zeros(final_grid.shape)

	for z in range(final_grid.shape[0]):
		for x in range(final_grid.shape[1]):
			for y in range(final_grid.shape[2]):

				active_blocks_count = 0

				for dz in range(-1, 2, 1):
					for dx in range(-1, 2, 1):
						for dy in range(-1, 2, 1):

							if (dz == 0) and (dx == 0) and (dy == 0):
								continue

							if is_valid_crd((z+dz, x+dx, y+dy), final_grid.shape):
								if final_grid[z+dz, x+dx, y+dy] == True:
									active_blocks_count += 1

				if final_grid[z, x, y] == True:

					if active_blocks_count in [2, 3]:
						new_grid[z, x, y] = True
				
				elif active_blocks_count == 3:
					new_grid[z, x, y] = True

	final_grid[:] = new_grid
	# print(f"Iteration {i} complete.")

print(f"Final Active Cubes after {iters} iters : {final_grid.sum()}")
