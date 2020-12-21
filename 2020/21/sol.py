
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

	ingredients_list.append(list(ingredients))

for allergen in allergens_map:
	common_ingredients = allergens_map[allergen][0]
	for l in allergens_map[allergen][1:]:
		common_ingredients = common_ingredients.intersection(l)
	allergens_map[allergen] = common_ingredients

all_allergen_items = set([v for f in list(allergens_map.values()) for v in f])
non_allergen_count = 0

for line in ingredients_list:
	for ing in line:
		if ing not in all_allergen_items:
			non_allergen_count += 1

print(non_allergen_count)
