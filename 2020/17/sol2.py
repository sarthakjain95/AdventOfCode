
#! /usr/bin/env python

import numpy as np
from pprint import pprint

with open("input.txt", 'r') as f:
	content = f.read()

content = content.replace('.', '0').replace('#', '1').split('\n')
init_grid_size = len(content[0])
grid = list(map(lambda x: list(map(int, list(x))), content))
grid = np.array(grid).astype(np.bool).reshape((1, 1, init_grid_size, init_grid_size))

iters = 6

x = init_grid_size + 2 * iters
y = init_grid_size + 2 * iters
z = 1 + 2 * iters
w = 1 + 2 * iters

final_grid = np.zeros((w, z, x, y)).astype(np.bool)
i = iters
final_grid[i:i+1, i:i+1, i:i+init_grid_size, i:i+init_grid_size] = grid

is_valid_crd = lambda c, l: all([c[o]>=0 and c[o]<l[o] for o in range(len(l))])

for i in range(iters):

	new_grid = np.zeros(final_grid.shape)

	for w in range(final_grid.shape[0]):
		for z in range(final_grid.shape[1]):
			for x in range(final_grid.shape[2]):
				for y in range(final_grid.shape[3]):

					active_blocks_count = 0

					for dw in range(-1, 2, 1):
						for dz in range(-1, 2, 1):
							for dx in range(-1, 2, 1):
								for dy in range(-1, 2, 1):

									if (dz == 0) and (dx == 0) and (dy == 0) and (dw == 0):
										continue

									if is_valid_crd((w+dw, z+dz, x+dx, y+dy), final_grid.shape):
										if final_grid[w+dw, z+dz, x+dx, y+dy] == True:
											active_blocks_count += 1

					if final_grid[w, z, x, y] == True:

						if active_blocks_count in [2, 3]:
							new_grid[w, z, x, y] = True
					
					elif active_blocks_count == 3:
						new_grid[w, z, x, y] = True

	final_grid[:] = new_grid
	print(f"Iteration {i} complete.")

print(f"Number of active cudes after {iters} iterations : {final_grid.sum()}")
