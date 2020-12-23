
#! /usr/bin/env python

cups = "459672813"
cups = list(map(int, list(cups)))

def cups_game(cups, moves):

	current_cup = cups[0]
	max_cup = max(cups)

	for move in range(moves):

		dest = current_cup - 1
		if dest == 0: dest = max_cup

		picked_up_cups = []
		for i in range(1, 4):
			picked_up_cups.append(cups[(cups.index(current_cup)+i)%len(cups)])

		for cup in picked_up_cups:
			del cups[cups.index(cup)]

		while dest not in cups:
			dest -= 1
			if dest == 0: dest = max_cup

		for i in range(3):
			cups.insert(cups.index(dest)+i+1, picked_up_cups[i])

		current_cup = cups[(cups.index(current_cup)+1)%len(cups)]

	result_cups = []
	for i in range(1, 9):
		result_cups.append(cups[(cups.index(1)+i)%len(cups)])

	return result_cups

result = cups_game(cups, 100)
result = list(map(str, result))
result = "".join(result)
print(result)
