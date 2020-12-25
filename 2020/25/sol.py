
#! /usr/bin/env python

door_public_key = 8458505
card_public_key = 16050997
# door_public_key = 17807724
# card_public_key = 5764801

def get_loop_size(x):

	start = 1
	loop_size = 0

	while start != x:
		start = start * 7
		start = start % 20201227
		loop_size += 1

	return loop_size

door_loop_size = get_loop_size(door_public_key)
card_loop_size = get_loop_size(card_public_key)
print(door_loop_size, card_loop_size)

def get_encryption_key(subject, loop_size):

	start = 1

	for i in range(loop_size):
		start = start * subject
		start = start % 20201227

	return start

encryption_key = get_encryption_key(door_public_key, card_loop_size)
print(encryption_key)
