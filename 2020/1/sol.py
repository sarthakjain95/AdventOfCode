
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	content = f.readlines()

content = [int(n.strip()) for n in content]

for i in content:
	for j in content:
		if i!=j and i+j == 2020:
			print(i*j, i, j)

print("done.")

for i in content:
	for j in content:
		for k in content:
			if i!=j and i!=k and i+j+k == 2020:
				print(i*j*k, i, j, k)

print("done.")
