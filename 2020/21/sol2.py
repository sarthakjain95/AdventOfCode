
#! /usr/bin/env python

import re
from pprint import pprint

with open("input.txt", 'r') as f:
	content = f.readlines()

food_items = [c.strip() for c in content]
ingredients_allergens_re = re.compile(r'''([\ a-z]+)\ \(contains\ ([\ a-z\,]+)\)''')

allergens_map = {}
ingredients_list = []

for line in food_items:

	ingredients, allergens = ingredients_allergens_re.match(line).groups()
	ingredients = set(ingredients.split(" "))
	allergens = set(allergens.split(", "))

	for allergen in allergens:
		if allergen not in allergens_map:
			allergens_map[allergen] = []
		allergens_map[allergen].append(ingredients)

	ingredients_list.append(ingredients)

for allergen in allergens_map:
	common_ingredients = allergens_map[allergen][0]
	for l in allergens_map[allergen][1:]:
		common_ingredients = common_ingredients.intersection(l)
	allergens_map[allergen] = common_ingredients

all_allergens_list = list(allergens_map.keys())

for a1 in all_allergens_list:
	if len(allergens_map[a1]) > 1: 
		continue
	for a2 in all_allergens_list:
		if a1 == a2: continue
		else: allergens_map[a2] = allergens_map[a2] - allergens_map[a1]

dangerous_ingredients_list = [(a, list(allergens_map[a])[0]) for a in allergens_map]
dangerous_ingredients_list = sorted(dangerous_ingredients_list, key=lambda x: x[0])
dangerous_ingredients_list = [d[1] for d in dangerous_ingredients_list]

print(",".join(dangerous_ingredients_list))
