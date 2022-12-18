# change directory to the directory of this file
import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read input
with open("input.txt") as f:
    data = f.read()

# parse input using regex
sensors = []
beacons = []
for line in data.splitlines():
    m = re.search(r"x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)", line)
    sensors.append((int(m.group(1)), int(m.group(2))))
    beacons.append((int(m.group(3)), int(m.group(4))))

min_x = min(min(sensor[0] for sensor in sensors), min(beacon[0] for beacon in beacons))
max_x = max(max(sensor[0] for sensor in sensors), max(beacon[0] for beacon in beacons))
min_y = min(min(sensor[1] for sensor in sensors), min(beacon[1] for beacon in beacons))
max_y = max(max(sensor[1] for sensor in sensors), max(beacon[1] for beacon in beacons))

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

largest_distance = max(manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1]) for sensor, beacon in zip(sensors, beacons))

def check_position(x, y):
    """check if a position is within a distance from any sensor to its closest beacon"""
    for i, sensor in enumerate(sensors):
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacons[i]

        if manhattan_distance(sensor_x, sensor_y, x, y) <= manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y):
            return True
    return False

def print_row(y):
    """print a row of the grid"""
    for x in range(min_x, max_x + 1):
        if (x, y) in beacons:
            print("B", end="")
        elif (x, y) in sensors:
            print("S", end="")
        elif check_position(x, y):
            print("#", end="")
        else:
            print(".", end="")
    print()

def print_grid():
    for y in range(min_y, max_y + 1):
        print_row(y)

def get_num_positions_within_distance_for_row(y):
    """get the number of positions within a distance from any sensor to its closest beacon for a row"""
    num_positions = 0

    for x in range(min_x - largest_distance, max_x + 1 + largest_distance):
        if (x, y) in beacons:
            continue
        if (x, y) in sensors:
            continue
        if check_position(x, y):
            num_positions += 1
    return num_positions

# print_grid()
print(get_num_positions_within_distance_for_row(2000000))