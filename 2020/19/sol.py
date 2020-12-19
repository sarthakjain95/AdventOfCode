
#! /usr/bin/env python

from pprint import pprint 
from itertools import product

with open("input.txt", 'r') as f:
	content = f.read()

rules, messages = content.split("\n\n")
rules = [r.strip() for r in rules.split('\n')]
messages = set([m.strip() for m in messages.split('\n')])

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

valid_messages = set(resolve_rule(0))
n_valid_messages = len(valid_messages.intersection(messages))

print(f"Number of valid messages: {n_valid_messages}")
