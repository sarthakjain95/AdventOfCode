
#! /usr/bin/env python

import re
from pprint import pprint

with open("input.txt", 'r') as f:
	content = f.read()

rule_re = re.compile("([\d]+)\-([\d]+)")
string_to_numbers = lambda values: list(map(int, values.split(",")))

rules, your_ticket, nearby_tickets = content.split("\n\n")

rules = rules.split('\n')
your_ticket = your_ticket.split('\n')[1]
nearby_tickets = nearby_tickets.split('\n')[1:]

your_ticket = string_to_numbers(your_ticket)
nearby_tickets = list(map(string_to_numbers, nearby_tickets))

rules_map = {}

for line in rules:

	rule_name, rule = line.split(":")
	extracted_rules = [list(map(int, r)) for r in rule_re.findall(rule)]
	rules_map[rule_name] = extracted_rules

valid_tickets = []

for nums in nearby_tickets:
	is_valid = True

	for n in nums:
		satisfies = False

		for rule in [r for ru in rules_map.values() for r in ru]:
			if rule[0] <= n <= rule[1]:
				satisfies = True
				break

		if not satisfies:
			is_valid = False
			break

	if is_valid:
		valid_tickets.append(nums)

# pprint(rules_map)
remaining_rules = list(rules_map.keys())
remaining_indices = list(range(len(valid_tickets[0])))
N_FIELDS = len(valid_tickets[0])

rule_index_map = {}

while len(remaining_rules):

	rule_name = remaining_rules[0]
	rule = rules_map[rule_name]

	satisfied_indices = []

	for x in remaining_indices:
		ticket_results = []

		for y in valid_tickets:
			satisfies = False

			for ru in rule:
				if ru[0] <= y[x] <= ru[1]:
					satisfies = True

			ticket_results.append(satisfies)

		if all(ticket_results):
			satisfied_indices.append(x)

	if len(satisfied_indices) == 1:
		rule_index_map[rule_name] = satisfied_indices[0]
		del remaining_rules[0]
		del remaining_indices[remaining_indices.index(satisfied_indices[0])]
	else:
		remaining_rules.append(rule_name)
		del remaining_rules[0]

final_result = 1
for key in rule_index_map:
	if key[:9] == "departure":
		final_result *= your_ticket[rule_index_map[key]]

print(f"Product of indices with 'departure' in your ticket is {final_result}")
