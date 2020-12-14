
#! /usr/bin/env python

from pprint import pprint

with open('input.txt', 'r') as f:
	content = f.readlines()

instructions = [c.strip().split(' = ') for c in content]

mem = {}
mask = ""

for command, val in instructions:

	if command == "mask":
	
		mask = val[::-1]
	
	else:	
	
		val_bin = [*map(int, list(str(bin(int(val)))[2:].zfill(36)))][::-1]
		val_bin_len = len(val_bin)

		addr = int(command[4:-1])
		if addr not in mem:
			mem[addr] = [0]*36

		for idx in range(val_bin_len):
			if val_bin[idx] == 1:
				mem[addr][idx] = 1
			else:
				mem[addr][idx] = 0

		for i in range(36):
			if mask[i] == "0":
				mem[addr][i] = 0
			elif mask[i] == "1":
				mem[addr][i] = 1

total_sum = 0
for addr in mem:
	val = int("".join([*map(str, mem[addr])])[::-1], 2)
	total_sum += val

print(f"Total sum of all values in addresses is {total_sum}")
