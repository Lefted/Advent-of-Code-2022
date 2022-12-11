# change directory to the directory of this file
import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read input
with open('input.txt', 'r') as file:
    input = file.read()

# parse input
instructions = []
for line in input.splitlines():
    instructions.append(re.findall(r'(\w+) ?(-?\d+)?', line)[0])

instruction_index = 0
sprite_middle = 1
sprite_width = 3
running_addition = None

rows = ['' for row in range(6)]

# run cycles
for cycle in range(1, 241):
	# get current row
	row = rows[int((cycle - 1)/ 40) ]
	pixel_in_row = (cycle-1) % 40

	if running_addition is None:
		instruction = instructions[instruction_index]
		if instruction[0] == 'addx':
			running_addition = (int(instruction[1]), 1)
		instruction_index += 1

	# check if sprite is visible
	if pixel_in_row == sprite_middle - 1 or pixel_in_row == sprite_middle or pixel_in_row == sprite_middle + 1:
		row += '#'
	else:
		row += '.'

	if running_addition is not None:
		value, lifetime = running_addition
		# if lifetime is 0 execute addition and reset
		if lifetime == 0:
			sprite_middle += value
			running_addition = None
		else:
			running_addition = (value, lifetime - 1)

	# update row
	rows[int((cycle - 1)/ 40)] = row

# print result
for row in rows:
	print(row)