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

min_x = min(min(sensor[0] for sensor in sensors),
            min(beacon[0] for beacon in beacons))
max_x = max(max(sensor[0] for sensor in sensors),
            max(beacon[0] for beacon in beacons))
min_y = min(min(sensor[1] for sensor in sensors),
            min(beacon[1] for beacon in beacons))
max_y = max(max(sensor[1] for sensor in sensors),
            max(beacon[1] for beacon in beacons))


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_remaining_distance(x, y):
    """check if a position is within a distance from any sensor to its closest beacon and return the remaining distance until it is no longer"""
    for i, sensor in enumerate(sensors):
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacons[i]

        delta = manhattan_distance(
            sensor_x, sensor_y, beacon_x, beacon_y) - manhattan_distance(sensor_x, sensor_y, x, y)
        if delta >= 0:
            return delta
    return -1


def find_tuning_frequency():
    # Initialize variables
    x = 0
    y = 0

    # Set search limits
    x_max = 4000000
    y_max = 4000000
    while y < y_max:

        if y % 1000 == 0:
            # print percentage of y and round to 2 decimals
            print(round(y / y_max * 100, 2), "%")

        while x < x_max:
            distance_to_go = get_remaining_distance(x, y)
            if distance_to_go == -1:
                print(x * 4000000 + y)
                return
            if distance_to_go == 0:
                distance_to_go = 1
            x += distance_to_go
        x = 0
        y += 1


find_tuning_frequency()
