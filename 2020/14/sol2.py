
#! /usr/bin/env python

from pprint import pprint
from itertools import product

with open('input.txt', 'r') as f:
	content = f.readlines()

instructions = [c.strip().split(' = ') for c in content]

mem = {}
mask = ""


def write_to_address(addr, val_bin):

	if addr not in mem:
		mem[addr] = ['0']*36

	val_len = len(val_bin)
	mem[addr][0:val_len] = val_bin[::-1]


def resolve_address(addr, value, m="0"*36):

	if addr not in mem:
		mem[addr] = ['0']*36

	addr_bin = list(str(bin(int(addr)))[2:].zfill(36))[::-1]
	addr_bin_len = len(addr_bin)

	x_indices = []
	for idx in range(len(m)):
		if m[idx] == '1':
			addr_bin[idx] = '1'
		elif m[idx] == 'X':
			addr_bin[idx] = 'X'
			x_indices.append(idx)

	all_products = product(['1', '0'], repeat=m.count('X'))
	possible_address = []

	for permute in all_products:

		na = [*permute]
		for idx in x_indices:
			addr_bin[idx] = na.pop()

		possible_address.append(addr_bin.copy())

	for a in possible_address:
		possibility = int("".join(a)[::-1], 2)
		write_to_address(possibility, list(str(bin(value))[2:].zfill(36)))


for command, val in instructions:
	if command == "mask":
		mask = val[::-1]
	else:
		addr = int(command[4:-1])
		resolve_address(addr, int(val), mask)

total_sum = 0

for addr in mem:
	val = int("".join(mem[addr])[::-1], 2)
	total_sum+=val

print(f"Total sum for version 2.0 is {total_sum}")
