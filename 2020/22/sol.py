
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	content = f.read()

p1, p2 = content.split("\n\n")

p1 = p1.split("\n")[1:]
p2 = p2.split("\n")[1:]

p1 = [int(l.strip()) for l in p1][::-1]
p2 = [int(l.strip()) for l in p2][::-1]

while len(p1) and len(p2):

	a = p1.pop()
	b = p2.pop()

	if a > b: p1 = [b, a, *p1]
	else: p2 = [a, b, *p2]

winner = p2
if len(p1):
	winner = p1

result = sum([winner[i]*(i+1) for i in range(len(winner))])
print(result)
