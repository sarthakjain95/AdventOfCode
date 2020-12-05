
#! /usr/bin/env python

import re
hexcode_regex = re.compile("""^(#[0-9a-f]{6})$""")
pid_regex = re.compile("""^([0-9]{9})$""")

def height_check(height):
	if height[-2:] not in ["cm", "in"]: return False
	if height[-2:] == "cm": return 150 <= int(height[:-2]) <= 193
	else: return 59 <= int(height[:-2]) <= 76

with open("input.txt", 'r') as f:
	passports = f.read()

passports = passports.strip().split("\n\n")
invalid = 0
valid = 0

for passport in passports:
	
	passport_data = passport.split()
	fields_present = set([data.split(':')[0] for data in passport_data]) - set(["cid"])
	
	if len(fields_present) != 7: 
		invalid += 1
	else:
		checks = []
		check_functions = { # field, function
			"byr": lambda yr: 1920 <= int(yr) <= 2002,
			"iyr": lambda yr: 2010 <= int(yr) <= 2020,
			"eyr": lambda yr: 2020 <= int(yr) <= 2030,
			"hgt": height_check,
			"hcl": lambda clr: bool(hexcode_regex.match(clr)),
			"ecl": lambda clr: clr in "amb,blu,brn,gry,grn,hzl,oth".split(','),
			"pid": lambda idx: bool(pid_regex.match(idx)),
		}
		
		for data in passport_data:
			field, val = data.split(":")
			if field == "cid": continue 
			res = check_functions[field](val)
			# print(field, val, res)
			checks.append(res)

		if all(checks): valid += 1
		else: invalid += 1

print(f"Valid passports: {valid}")
print(f"Invalid passports: {invalid}")
