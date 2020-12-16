
#! /usr/bin/env python

import re

with open("input.txt", 'r') as f:
	content = f.read()

rules, your_ticket, nearby_tickets = content.split("\n\n")

rules = rules.split('\n')
your_ticket = your_ticket.split('\n')[1]
nearby_tickets = nearby_tickets.split('\n')[1:]

string_to_numbers = lambda values: list(map(int, values.split(",")))

your_ticket = string_to_numbers(your_ticket)
nearby_tickets = list(map(string_to_numbers, nearby_tickets))

rule_re = re.compile("([\d]+)\-([\d]+)")
rule_ranges = []

for line in rules:

	rule = line.split(":")[1].strip()
	extracted_rules = rule_re.findall(rule)
	extracted_rules = [list(map(int, r)) for r in extracted_rules]
	rule_ranges = rule_ranges + extracted_rules

# print(rule_ranges)
wrong_values_sum = 0

for nums in nearby_tickets:
	
	for n in nums:
		satisfies = False

		for rule in rule_ranges:
			if rule[0] <= n <= rule[1]:
				satisfies = True
				break

		if not satisfies:
			wrong_values_sum += n

print(f"Sum of all the invalid values: {wrong_values_sum}")
