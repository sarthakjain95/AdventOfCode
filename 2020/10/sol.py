
#! /usr/bin/env python

from pprint import pprint

with open("input.txt", 'r') as f:
	adapters = f.readlines()

adapters.append('0')
adapters = [int(a.strip()) for a in adapters]
adapters.append(max(adapters)+3)
adapters = sorted(adapters)
# print(adapters)

differences = {
	1: 0,
	3: 0
}

for i in range(1, len(adapters)):
	differences[adapters[i] - adapters[i-1]] += 1

print("Differences counts:")
pprint(differences)
prod = differences[1] * differences[3]
print(f"Final counts product: {prod} (correct:{prod==2048})")

compatibility_map = {}
cache = {}

for i in range(len(adapters)-1, -1, -1):

	adapter = adapters[i]
	compatibility_map[adapter] = []

	for i in range(1, 3+1):
		if adapter-i in adapters:
			compatibility_map[adapter].append(adapter-i)

def get_combinations(cap):

	if cap in cache:
		return cache[cap]
	else:
		# compute
		if cap == 0:
			cache[cap] = 1
			return 1
		else:
			all_combos = 0
			for c in compatibility_map[cap]:
				combos = get_combinations(c)
				cache[c] = combos
				all_combos += combos
			return all_combos

all_combinations = get_combinations(adapters[-1])
print(f"All combinations: {all_combinations} (correct:{1322306994176==all_combinations})")
