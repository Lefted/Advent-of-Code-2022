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

# function to print the grid where 0, 0 is in the bottom left corner and the grid has a size of 6x5
def print_grid(head, tail):
    # print the grid row by row from top to bottom
    for y in range(4, -1, -1):
        # print the grid column by column from left to right
        for x in range(6):
            # if the position is the head
            if x == head.x and y == head.y:
                print('H', end='')
            # if the position is the tail and not the same as the head
            elif x == tail.x and y == tail.y and (x, y) != (head.x, head.y):
                print('T', end='')
            # if the position is the starting position and not the same as the head or tail
            elif x == 0 and y == 0 and (x, y) not in [(head.x, head.y), (tail.x, tail.y)]:
                print('s', end='')
            # if the position is visited and not the same as the head or tail
            elif (x, y) in visited and (x, y) not in [(head.x, head.y), (tail.x, tail.y)]:
                print('#', end='')
            # if the position is empty
            else:
                print('.', end='')
        print()

# function to update the tail position


def update_tail(head, tail):
    # if head and tail are not adjacent (they can still be diagonal)
    if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
        # if the tail is to the left of the head
        if tail.x < head.x:
            tail.x += 1
        # if the tail is to the right of the head
        elif tail.x > head.x:
            tail.x -= 1
        # if the tail is above the head
        if tail.y > head.y:
            tail.y -= 1
        # if the tail is below the head
        elif tail.y < head.y:
            tail.y += 1

# function to move the head one step
def move_head_one_step(head, direction):
    # move head one step in the given direction
    print(direction)
    if direction == 'R':
        head.x += 1
    elif direction == 'L':
        head.x -= 1
    elif direction == 'U':
        head.y += 1
    elif direction == 'D':
        head.y -= 1

# function to move the head and update the tail
def move_head_and_update_tail(head, tail, direction, steps):
    # move the head and update the tail for each step
    for i in range(steps):
        # print_grid(head, tail)
        # print("\n\n")
        move_head_one_step(head, direction)
        update_tail(head, tail)
        # add the position of the tail to the set of visited positions
        visited.add((tail.x, tail.y))

# class to represent a position


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# create a head and a tail
head = Position(0, 0)
tail = Position(0, 0)

# add the position of the tail to the set of visited positions
visited.add((tail.x, tail.y))

# move the head and update the tail for each instruction
for instruction in input:
    move_head_and_update_tail(head, tail, instruction[0], instruction[1])

# print_grid(head, tail)

# print the number of positions the tail visited at least once
print(len(visited))
