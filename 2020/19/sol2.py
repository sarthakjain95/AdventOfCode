
#! /usr/bin/env python

from pprint import pprint 
from itertools import product

with open("input.txt", 'r') as f:
	content = f.read()

rules, messages = content.split("\n\n")
rules = [r.strip() for r in rules.split('\n')]
messages = [m.strip() for m in messages.split('\n')]

constants = {}
rule_maps = {}

for rule in rules:

	r, mapped_value = rule.split(":")
	r, mapped_value = int(r), mapped_value.strip()

	if mapped_value in ["\"a\"", "\"b\""]:
		constants[r] = mapped_value[1:-1]
	else:
		mapped_value = mapped_value.split("|")
		mapped_rules = tuple([tuple(map(int, m.strip().split(' '))) for m in mapped_value])
		rule_maps[r] = mapped_rules

def resolve_rule(rule_no):

	if rule_no in constants:
		return constants[rule_no]
	
	options = []
	for combo in rule_maps[rule_no]:
		sub_options = []
		for r in combo:
			sub_options.append(resolve_rule(r))
		sub_options = list(product(*sub_options))
		sub_options = ["".join(s) for s in sub_options]
		options = [*options, *sub_options]
	
	return options

rule_possibilities = {}
for rule in rule_maps:
	if rule in [0, 8, 11]:
		continue
	rule_possibilities[rule] = resolve_rule(rule)

valid_messages_count = 0
for m in messages:

	is_valid = False
	original_message = m
	message = m
	r42_length = len(rule_possibilities[42][0])
	r31_length = len(rule_possibilities[31][0])

	while message[:r42_length] in rule_possibilities[42]:

		original_message = original_message[r42_length:]
		message = original_message

		if message[:r42_length] in rule_possibilities[42] and message[-r31_length:] in rule_possibilities[31]:

			while message[:r42_length] in rule_possibilities[42] and message[-r31_length:] in rule_possibilities[31] and len(message) >= (r31_length+r42_length):
				message = message[r42_length:-r31_length]

			if len(message) == 0:
				is_valid = True
				break

	valid_messages_count += is_valid

print(f"Number of valid messages: {valid_messages_count}")
