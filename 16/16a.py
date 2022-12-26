from collections import deque
import os
from functools import cache

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read the input file
with open('input.txt', 'r') as f:
    lines = f.readlines()


valves = {}
tunnels = {}
# create a dictionary of valves
valves = {}
for line in lines:
    line = line.split()
    valve = line[1]
    flow = line[4][5:-1]
    targets = [tunnel[:-1] if tunnel != line[-1]
               else tunnel for tunnel in line[9:]]
    valves[valve] = int(flow)
    tunnels[valve] = targets

dists = {}
nonempty = []

# credit: https://github.com/hyper-neutrino/advent-of-code

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue

    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}

    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

@cache
def dfs(time, valve, bitmask):
    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue
        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue
        maxval = max(maxval, dfs(remtime, neighbor, bitmask |
                     bit) + valves[neighbor] * remtime)

    return maxval


print(dfs(30, "AA", 0))
