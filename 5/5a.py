"""--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ."""

# change to directory of this file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read input
with open('input.txt') as f:
	input = f.read()

# split input into initial state and instructions
initial_state, instructions = input.split('\n\n')

# parse initial state
stacks = []
# for each line but the last one
for line in initial_state.splitlines()[:-1]:
	# iterate over characters and detect current stack using current index of line
	stack = []

	# start index = 1
	i = 1
	# iterate to end of line - 1 from i
	while i < len(line) - 1:
		# get current stack
		current_stack = (i - 1) // 4

		# if current stack is not in stacks
		if current_stack >= len(stacks):
			# add new stack to stacks
			stacks.append([])

		# if character is not a space
		if line[i] != ' ':

			# add character to current stack
			stacks[current_stack].append(line[i])

		i += 4

# print initial state
print('Initial state:')
for stack in stacks:
	print(stack)


# parse instructions (amount, from_number, to_number)
instructions = [(instruction.split()[1::2]) for instruction in instructions.splitlines()]

# print instructions
print('Instructions:')
for instruction in instructions:
	print(instruction)

# execute instructions
for instruction in instructions:
	# get amount, from_number and to_number
	amount, from_number, to_number = instruction

	# convert to int
	amount = int(amount)
	from_number = int(from_number)
	to_number = int(to_number)

	# get crates from the stack at from_number - 1 and remove them from the stack
	crates = stacks[from_number - 1][:amount]

	# remove crates from stack at from_number - 1
	stacks[from_number - 1] = stacks[from_number - 1][amount:]
	print(stacks[from_number - 1])
	
	# add crates to to_number - 1 stack by adding them to the beginning of the stack but reversed
	stacks[to_number - 1] = crates[::-1] + stacks[to_number - 1]

# # print final state
# print('Final state:')
# for stack in stacks:
# 	print(stack)

# print result
print('Result:')
print(''.join([stack[0] for stack in stacks]))