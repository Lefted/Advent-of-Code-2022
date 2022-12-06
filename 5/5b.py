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
	
	# add crates to to_number - 1 stack by adding them to the beginning of the stack in same order
	stacks[to_number - 1] = crates + stacks[to_number - 1]

# # print final state
# print('Final state:')
# for stack in stacks:
# 	print(stack)

# print result
print('Result:')
print(''.join([stack[0] for stack in stacks]))
