
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	instructions = f.readlines()

instructions = [i.strip() for i in instructions]

accumulator = 0
idx = 0
executed_indices = []

while idx < len(instructions):

	command, val = instructions[idx].split()
	val = int(val)

	if idx in executed_indices: break
	else: executed_indices.append(idx)

	if command == "nop":
		idx += 1
	elif command == "jmp":
		idx += val
	elif command == "acc":
		idx += 1
		accumulator += val

print(f"Accumulator value before a statement is repeated: {accumulator}")

def terminates(instructions):

	idx = 0
	accumulator = 0

	executed_indices = []

	while idx < len(instructions):

		command, val = instructions[idx].split()
		val = int(val)

		if idx in executed_indices: 
			accumulator = -1
			break
		 
		executed_indices.append(idx)

		if command == "nop":
			idx += 1
		elif command == "jmp":
			idx += val
		elif command == "acc":
			idx += 1
			accumulator += val

	return accumulator


for idx in range(len(instructions)):

	command, val = instructions[idx].split()
	val = int(val)

	new_instructions = instructions.copy()

	if command == "jmp":
		new_instructions[idx] = f"nop {val}"
	elif command == "nop":
		new_instructions[idx] = f"jmp {val}"

	final_value = terminates(new_instructions)
	if final_value != -1:
		print(f"Accumulator value after program terminates: {final_value}")
