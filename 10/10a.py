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

# run clock
x = 1
signal_strengths = []
running_addition = None
instruction_index = 0
for cycle in range(1, 221):
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(cycle * x)

    if running_addition is not None:
        x += running_addition
        running_addition = None

    elif instruction_index < len(instructions):
        instruction = instructions[instruction_index]
        if instruction[0] == 'addx':
            running_addition = int(instruction[1])
        instruction_index += 1

# print answer
print(sum(signal_strengths))
