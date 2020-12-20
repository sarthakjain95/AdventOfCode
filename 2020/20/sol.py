
#! /usr/bin/env python

from pprint import pprint 
import numpy as  np

with open("input.txt", 'r') as f:
	content = f.read()

tiles_raw = content.split("\n\n")
tiles = {}

for t in tiles_raw:

	tile = {}
	tile_name, tile_data = t.split("\n")[0], t.split("\n")[1:]

	tile_id = int(t.split("\n")[0].split(" ")[1].strip(":"))
	tile_data = t.replace(".", "0").replace("#", '1').split("\n")[1:]
	tile_data = list(map(lambda td: list(map(int, list(td))), tile_data))

	tiles[tile_id] = {"data":np.array(tile_data), "neighbours":[]}

def generate_orientations(mat):

	orientations = [
		mat, 
		np.rot90(mat, 1), 
		np.rot90(mat, 2), 
		np.rot90(mat, 3),
		mat.T,
		np.rot90(mat.T, 1),
		np.rot90(mat.T, 2),
		np.rot90(mat.T, 3)
	]

	return orientations

def overlap_check(a, b):
	if (a[:, -1] == b[:,  0]).all(): return True
	if (a[:,  0] == b[:, -1]).all(): return True
	if (a[ 0, :] == b[-1, :]).all(): return True
	if (a[-1, :] == b[ 0, :]).all(): return True
	return False

corner_ids = []

for y in tiles:
	a = tiles[y]["data"]
	
	for x in tiles:
		if (y == x): continue
		for b in generate_orientations(tiles[x]["data"]):
			if overlap_check(a, b) == True:
				tiles[y]["neighbours"].append(x)
				break
	
	if len(tiles[y]["neighbours"]) == 2:
		corner_ids.append(y)

result = 1
for i in corner_ids: 
	result *= i

print(f"Product of ids of corner blocks is {result}")
