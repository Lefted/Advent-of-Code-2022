import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('input.txt', 'r') as file:
    input = file.read()

# parse input
input = input.splitlines()
input = [re.findall(r'\d+', line) for line in input]
input = [[(int(x), int(y)) for x, y in zip(line[::2], line[1::2])]
         for line in input]

# determine size of grid using max_x, max_y and min_x
max_x = max([max(line, key=lambda x: x[0])[0] for line in input])
max_y = max([max(line, key=lambda x: x[1])[1] for line in input])
min_x = min([min(line, key=lambda x: x[0])[0] for line in input])

grid_width = max_x - min_x + 1
grid_height = max_y + 1

# create grid
grid = [['.' for x in range(grid_width)] for y in range(grid_height)]


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


for line in input:
    for i in range(len(line) - 1):
        x1, y1 = line[i]
        x2, y2 = line[i + 1]
        draw_rock_line(x1, x2, y1, y2)


def print_grid():
    for line in grid:
        # draw source as +
        grid[0][500 - min_x] = '+'
        print(''.join(line))

def summon_sand():
    grid[0][500 - min_x] = '~'
    return (500 - min_x, 0)

def tick_sand(x, y):
    # check if tile under the sand is still in the grid
    if y + 1 >= grid_height:
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
    return False

while True:
    x, y = summon_sand()
    new_sand = None
    while True:
        new_sand = tick_sand(x, y)
        if new_sand == None or new_sand == False:
            break
        x, y = new_sand

    if new_sand == None:
        print_grid()
        break

# count number of sand that has come to rest
count = 0
for line in grid:
    for char in line:
        if char == 'o':
            count += 1

print(count)
