
#! /usr/bin/env python

import re 

with open("input.txt", 'r') as f:
	content = f.readlines()

valid_passwords = 0
rule_re = re.compile("""([\d]+)\-([\d]+)\s([a-zA-Z])\:\s([a-z]+)""")

for line in content:
	line = line.strip()
	match = rule_re.match(line)
	if match:
		r1, r2, ch, pwd = match.groups()
		if int(r1) <= pwd.count(ch) <= int(r2):
			valid_passwords += 1

print(f"Total valid passwords: {valid_passwords}")


# PART 2

valid_passwords = 0

for line in content:
	line = line.strip()
	match = rule_re.match(line)
	if match:
		r1, r2, ch, pwd = match.groups()
		indices = [i for i in range(len(pwd)) if pwd[i] == ch]
		r1, r2 = int(r1)-1, int(r2)-1
		val = 0
		if r1 in indices: val+=1
		if r2 in indices: val+=1
		if val == 1:
			valid_passwords += 1

print(f"Total valid passwords (from new rules): {valid_passwords}")
