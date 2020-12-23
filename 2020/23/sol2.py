
#! /usr/bin/env python

from pprint import pprint

def cups_game(start, cups_map, moves):

	current_cup = cups_map[start]

	for m in range(moves):

		if m%1_000_000 == 0:
			print(m)

		dest = current_cup.value - 1
		if dest == 0: dest = 1_000_000
		picked_up_cups = []

		temp = current_cup
		for i in range(1, 4):
			temp = temp.next
			picked_up_cups.append(temp.value)

		while dest in picked_up_cups:
			dest = dest - 1
			if dest == 0: dest = 1_000_000

		pickedupcups_head = cups_map[current_cup.value].next
		pickedupcups_next = temp.next
		destination_next = cups_map[dest].next
		
		cups_map[dest].next = pickedupcups_head
		temp.next = destination_next
		current_cup.next = pickedupcups_next

		current_cup = current_cup.next

	x, y = cups_map[1].next.value, cups_map[1].next.next.value
	print()
	print(f"Values after 1: {x} and {y}")

	return x*y


cups = "459672813"
cups = list(map(int, list(cups)))

class Cup:

	def __init__(self, value):
		self.value = value
		self.next = None

first_cup = Cup(cups[0])
cups_map = { cups[0]: first_cup }

for i in range(1, len(cups)):
	new_cup = Cup(cups[i])
	cups_map[cups[i-1]].next = new_cup
	cups_map[cups[i]] = new_cup

new_cup = Cup(max(cups)+1)
cups_map[cups[-1]].next = new_cup
cups_map[max(cups)+1] = new_cup

for i in range(max(cups)+2, 1_000_000+1): 
	new_cup = Cup(i)
	cups_map[i-1].next = new_cup
	cups_map[i] = new_cup

cups_map[1_000_000].next = cups_map[cups[0]]

result = cups_game(cups[0], cups_map, 10_000_000)
print("Result:", result)
