# change directory to the directory of this file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read input
with open('input.txt') as f:
    input = f.read()

# parse input by splitting on newlines and spaces
input = [line.split() for line in input.splitlines()]

# convert input to a list of tuples
input = [(line[0], int(line[1])) for line in input]

# create a set of all visited positions
visited = set()

class Knot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# function to print a grid of 26 x 21 where 0,0 is at 16, 12 where 1 is the first character
def print_grid(head, knots, visited):
	# create a grid with the dimensions of the example above
	grid = [['.' for x in range(26)] for y in range(21)]

	# add the knots
	for i, knot in enumerate(knots):
		grid[-knot.y + 15][knot.x + 11] = str(i)

	# add the visited positions
	for position in visited:
		grid[-position[1] + 15][position[0] + 11] = '#'

	# add the head
	grid[-head.y + 15][head.x + 11] = 'H'

	# print the grid
	for row in grid:
		print(''.join(row))

# function to move the head one step
def move_head_one_step(head, direction):
    # move head one step in the given direction
    if direction == 'R':
        head.x += 1
    elif direction == 'L':
        head.x -= 1
    elif direction == 'U':
        head.y += 1
    elif direction == 'D':
        head.y -= 1

def update_knot(prevKnot, knot):
	# if knot and prevKnot are not adjacent (they can still be diagonal)
	if abs(knot.x - prevKnot.x) > 1 or abs(knot.y - prevKnot.y) > 1:
		# if the knot is to the left of the prevKnot
		if knot.x < prevKnot.x:
			knot.x += 1
		# if the knot is to the right of the prevKnot
		elif knot.x > prevKnot.x:
			knot.x -= 1
		# if the knot is above the prevKnot
		if knot.y > prevKnot.y:
			knot.y -= 1
		# if the knot is below the prevKnot
		elif knot.y < prevKnot.y:
			knot.y += 1

def move_head_and_update_knots(head, knots, direction, steps):
	# move the head and update the tail for each step
	# print(direction)
	for i in range(steps):
		move_head_one_step(head, direction)
		for i in range(len(knots) - 1):
			update_knot(knots[i], knots[i + 1])
		# add the position of the last knot to the set of visited positions
		visited.add((knots[-1].x, knots[-1].y))

def main():
	# create knot positions
	knots = [Knot(0, 0) for i in range(10)]

	# add the position of the tail to the set of visited positions
	visited.add((knots[9].x, knots[9].y))

	# move the head and update the tail for each instruction
	for instruction in input:
		# print_grid(knots[0], knots[1:], visited)
		print("\n\n")
		move_head_and_update_knots(knots[0], knots, instruction[0], instruction[1])
	# print_grid(knots[0], knots[1:], visited)

	# print the number of positions the tail visited at least once
	print(len(visited))

main()