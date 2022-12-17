"""Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0."""

# change directory to the directory of this file
import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# import modules

# read input
with open('input.txt', 'r') as file:
    input = file.read()

# parse input
input = input.splitlines()
input = [re.findall(r'\d+', line) for line in input]
# input = [[int(x) for x in line] for line in input]
# same as above but putting every x,y in a tuple
input = [[(int(x), int(y)) for x, y in zip(line[::2], line[1::2])]
         for line in input]

# determine size of grid using max_x, max_y and min_x
up_to_inf = 200

max_x = max([max(line, key=lambda x: x[0])[0] for line in input]) + up_to_inf
max_y = max([max(line, key=lambda x: x[1])[1] for line in input])
min_x = min([min(line, key=lambda x: x[0])[0] for line in input]) - up_to_inf


grid_width = max_x - min_x + 1
grid_height = max_y + 3

# create grid
grid = [['.' for x in range(grid_width)] for y in range(grid_height)]

"""Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########."""

# draw rock


def draw_rock_line(x1, x2, y1, y2):
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            grid[y][x1 - min_x] = '#'
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            grid[y1][x - min_x] = '#'


# add bottom line
input.append([(min_x, max_y + 2), (max_x, max_y + 2)])

for line in input:
    for i in range(len(line) - 1):
        x1, y1 = line[i]
        x2, y2 = line[i + 1]
        draw_rock_line(x1, x2, y1, y2)


def print_grid():
    for line in grid:
        # draw source as +
        print(''.join(line))


def summon_sand():
    grid[0][500 - min_x] = '~'
    return (500 - min_x, 0)


"""Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source."""

"""So, drawing sand that has come to rest as o, the falling sand tile as ~"""

# tick falling sand


def tick_sand(x, y):
    # if sand is at the bottom
    if y == max_y + 2:
        grid[y][x] = 'o'
        return None

    # check if sand can fall down
    if grid[y + 1][x] == '.':
        grid[y][x] = '.'
        grid[y + 1][x] = '~'
        return (x, y + 1)

    # check if sand can fall down-left
    if grid[y + 1][x - 1] == '.':
        grid[y][x] = '.'
        grid[y + 1][x - 1] = '~'
        return (x - 1, y + 1)

    # check if sand can fall down-right
    if grid[y + 1][x + 1] == '.':
        grid[y][x] = '.'
        grid[y + 1][x + 1] = '~'
        return (x + 1, y + 1)

    # if sand can't fall down, down-left or down-right
    grid[y][x] = 'o'
    return None


while True:
    x, y = summon_sand()
    while True:
        new_sand = tick_sand(x, y)
        if new_sand == None:
            break
        x, y = new_sand

    if grid[0][500-min_x] == 'o':
        print_grid()
        break

"""Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?"""

# count number of sand that has come to rest
count = 0
for line in grid:
    for char in line:
        if char == 'o':
            count += 1

print(count)
