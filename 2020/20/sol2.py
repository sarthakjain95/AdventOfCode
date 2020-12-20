
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

top_left_corner_options = []

for y in tiles:
	a = tiles[y]["data"]
	for x in tiles:
		if y == x or x in tiles[y]["neighbours"]: continue
		for b in generate_orientations(tiles[x]["data"]):
			if overlap_check(a, b):
				tiles[y]["neighbours"].append(x)
				tiles[x]["neighbours"].append(y)
				break

	if len(tiles[y]["neighbours"]) == 2:
		top_left_corner_options.append(y)

grid_size = int(len(tiles_raw)**0.5)
bs = len(tiles_raw[0].split("\n")[-1])
cropped_bs = bs - 2
bordered_image_size = grid_size * bs
borderless_bordered_image_size = grid_size * cropped_bs

tile_code_grid = np.zeros((grid_size, grid_size)).astype(np.int64)

def valid_coordinate(y, x):
	if y<0 or x<0: return False
	if y>=grid_size or x>=grid_size: return False
	return True

def recursive_image_construction(y, x):
	
	a = image[y*bs:(y+1)*bs, x*bs:(x+1)*bs]
	choices = tiles[tile_code_grid[y, x]]["neighbours"]

	# Build Down
	if valid_coordinate(y, x+1) and tile_code_grid[y, x+1] == -1:
		found = False
		for choice in choices:
			if found: break
			for b in generate_orientations(tiles[choice]["data"]):
				if (a[:, -1] == b[:, 0]).all():
					image[(y)*bs:(y+1)*bs, (x+1)*bs:(x+2)*bs] = b
					found = True
					tile_code_grid[y, x+1] = choice
					break
		if not found: return False
		recursive_image_construction(y, x+1)

	# Build Right
	if valid_coordinate(y+1, x) and tile_code_grid[y+1, x] == -1:
		found = False
		for choice in choices:
			if found: break
			for b in generate_orientations(tiles[choice]["data"]):
				if (a[-1, :] == b[0, :]).all():
					image[(y+1)*bs:(y+2)*bs, (x)*bs:(x+1)*bs] = b
					found = True
					tile_code_grid[y+1, x] = choice
					break
		if not found: return False
		recursive_image_construction(y+1, x)

	return True

for option in top_left_corner_options:
	
	tile_code_grid.fill(-1)
	tile_code_grid[0][0] = option
	image = np.zeros((bordered_image_size, bordered_image_size)).astype(np.int64)
	image[0:bs, 0:bs] = tiles[option]["data"]
	
	if recursive_image_construction(0, 0): break

cropped_image = np.zeros((borderless_bordered_image_size, borderless_bordered_image_size))

for y in range(grid_size):
	for x in range(grid_size):

		cropped_image[y*cropped_bs:(y+1)*cropped_bs, x*cropped_bs:(x+1)*cropped_bs] = image[y*bs+1:(y+1)*bs-1, x*bs+1:(x+1)*bs-1] 

monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

monster = monster[1:-1].replace("#", '1').replace(" ", "0").split("\n")
monster = list(map(lambda x: list(map(int, list(x))), monster))
monster = np.array(monster)

cropped_image = np.rot90(cropped_image, 3)

for img_copy in generate_orientations(cropped_image):

	img = img_copy.copy()
	for y in range(borderless_bordered_image_size-monster.shape[0]):
		for x in range(borderless_bordered_image_size-monster.shape[1]):

			res = img[y:y+monster.shape[0], x:x+monster.shape[1]] * monster
			if res.astype(np.bool).sum() == monster.sum():
				img[y:y+monster.shape[0], x:x+monster.shape[1]] += monster

	img = np.where(img==1, 0, img)
	for im in generate_orientations(img):
		if img.astype(np.bool).sum() == (cropped_image * im).astype(np.bool).sum():
			cropped_image += im
			break 

water_roughness = (cropped_image == 1).sum()
print(f"Water roughness is : {water_roughness}")
