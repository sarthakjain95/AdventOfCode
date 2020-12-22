
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	content = f.read()

p1, p2 = content.split("\n\n")

p1 = p1.split("\n")[1:]
p2 = p2.split("\n")[1:]

p1 = [int(l.strip()) for l in p1][::-1]
p2 = [int(l.strip()) for l in p2][::-1]

def recursive_combat(p1, p2):

	previous_rounds = set()

	while len(p1) and len(p2):

		if (tuple(p1), tuple(p2)) in previous_rounds:
			return 1, p1
		previous_rounds.add((tuple(p1), tuple(p2)))

		a = p1.pop()
		b = p2.pop()

		if len(p1) >= a and len(p2) >= b:
			winner, _ = recursive_combat(p1.copy()[-a:], p2.copy()[-b:])
			if winner == 1: p1 = [b, a, *p1]
			else: p2 = [a, b, *p2]
		else:
			if a>b: p1 = [b, a, *p1]
			else: p2 = [a, b, *p2]

	winner = 1
	if len(p1) == 0: 
		winner = 2

	return winner, p1 if winner == 1 else p2

winner, winner_deck = recursive_combat(p1, p2)
# print(winner)
# print(winner_deck)
result = sum([winner_deck[i]*(i+1) for i in range(len(winner_deck))]) 
print(result)
