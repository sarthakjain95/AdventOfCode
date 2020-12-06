
#! /usr/bin/env python

with open("input.txt", 'r') as f:
	content = f.read()

answers = content.split("\n\n")


total_yes_answers = 0
for ans in answers:
	total_yes_answers += len(set(list(ans.replace("\n", '').strip())))

print(f"Total 'yes' answers: {total_yes_answers}")


all_answers_yes = 0
for per_person_answers in answers:
	per_person_answers = per_person_answers.split('\n')
	common_answers = set(list(per_person_answers[0]))
	for line in per_person_answers[1:]:
		common_answers = common_answers.intersection(set(list(line.strip())))
	all_answers_yes += len(common_answers)

print(f"Total times all members answered 'yes': {all_answers_yes}")
