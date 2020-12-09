
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	nums = f.readlines()

nums = [int(n.strip()) for n in nums]

def is_valid_number(x, group):

	for i in range(len(group)):
		for j in range(len(group)):
			if i == j: continue

			if group[i] + group[j] == x:
				return True

	return False

d = 25
first_fault = -1
for i in range(d, len(nums)):

	if not is_valid_number(nums[i], nums[(i-d):i]):
		first_fault = nums[i]
		break

print(f"First number to break this property is {first_fault} (correct:{first_fault==144381670})")


first_fault_idx = nums.index(first_fault)

for i in range(len(nums)):

	if nums[i] == first_fault:
		continue

	cont_sum = nums[i]

	for j in range(i+1, len(nums)):

		if j == first_fault_idx:
			break

		cont_sum += nums[j]

		if cont_sum == first_fault:
			mx = max(nums[i:j])
			mn = min(nums[i:j])
			print(f"Found range: {i}-{j} (idx)")
			print(f"Range Max: {mx}")
			print(f"Range Min: {mn}")
			sm = mx + mn
			print(f"Sum of Min and Max: {sm} (correct:{sm==20532569})")
			break 
