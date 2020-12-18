
#! /usr/bin/env python

import re
from pprint import pprint 

with open("input.txt", 'r') as f:
	content = f.readlines()

equations = [c.strip().replace(' ', '') for c in content]

parenthesis_re = re.compile("""\(([^\(\)]+)\)""")
add_re = re.compile("""([\d]+)([\+])([\d]+)""")
mul_re = re.compile("""([\d]+)([\*])([\d]+)""")

ops_map = {
	'+': lambda x, y: x+y,
	'*': lambda x, y: x*y
}

def solve_equation(eqn):

	unresolved_paranthesis = parenthesis_re.search(eqn)
	add_op = add_re.search(eqn)
	mul_op = mul_re.search(eqn)

	if unresolved_paranthesis:

		sub_eqn = unresolved_paranthesis
		result = solve_equation( sub_eqn.groups()[0] )
		eqn = eqn[:sub_eqn.start()] + str(result) + eqn[sub_eqn.end():]

	elif add_op:

		sub_eqn = add_op.groups()
		result = ops_map[sub_eqn[1]](int(sub_eqn[0]), int(sub_eqn[-1]))
		eqn = eqn[:add_op.start()] + str(result) + eqn[add_op.end():]

	elif mul_op:

		sub_eqn = mul_op.groups()
		result = ops_map[sub_eqn[1]](int(sub_eqn[0]), int(sub_eqn[-1]))
		eqn = eqn[:mul_op.start()] + str(result) + eqn[mul_op.end():]

	else:
			return int(eqn)

	return solve_equation(eqn)

s = 0 # sum
for eqn in equations:
	s += solve_equation(eqn)

print(f"Sum is {s} (correct:{s==109418509151782})")
