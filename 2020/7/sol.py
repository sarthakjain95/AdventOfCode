
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	rules = f.read().split("\n")

bag_mappings = {}

for rule in rules:
	bag_color, contained_bags = rule.split(" contain ")
	bag_color = bag_color.replace("bags", "").replace("bag", "").strip()
	contained_bags = contained_bags[:-1].split(", ")
	if "no " not in contained_bags[0]: 
		contained_bags_colors = {" ".join(cb.split()[1:]).replace("bags", "").replace("bag", "").strip():int(cb.split()[0]) for cb in contained_bags}
		bag_mappings[bag_color] = contained_bags_colors

def does_include_golden(color):
	if color != "shiny gold" and color not in bag_mappings:
		return False
	elif color == "shiny gold":
		return True
	else:
		return any([does_include_golden(c) for c in bag_mappings[color].keys()])

count = 0
valid_bags = set()
for rule in rules:
	bag_color, _ = rule.split(" contain ")
	bag_color = bag_color.replace("bags", "").replace("bag", "").strip()
	if bag_color == "shiny gold": continue 
	res = does_include_golden(bag_color)
	if res:
		valid_bags.add(bag_color)

print(f"Total valid bags: {len(valid_bags)} (correct:{len(valid_bags)==252})")


def recursive_bag_counting(color):
	if color not in bag_mappings: return 0
	else: return sum(recursive_bag_counting(c)*bag_mappings[color][c]+bag_mappings[color][c] for c in bag_mappings[color])

def count_bags_in_shiny_gold():
	return recursive_bag_counting("shiny gold")

count = count_bags_in_shiny_gold()
print(f"Total bags in shiny golden bag: {count} (correct:{count==35487})")
