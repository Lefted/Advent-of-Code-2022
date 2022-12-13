# change directory to the directory of this file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read input
with open('input.txt', 'r') as file:
    input = file.read()

# create heightmap
heightmap = [list(line) for line in input.splitlines()]

# search for start
for y, line in enumerate(heightmap):
    if 'S' in line:
        start = (line.index('S'), y)
        break
# search for end
for y, line in enumerate(heightmap):
    if 'E' in line:
        end = (line.index('E'), y)
        break


# convert a-z to 0-25
heightmap = [[ord(c) - 97 for c in line] for line in heightmap]

# set start height
heightmap[start[1]][start[0]] = 0
# set end height
heightmap[end[1]][end[0]] = 25


# find shortest path using dijkstra's algorithm
# create a unidirectional graph with nodes and edges
graph = {}
for y, line in enumerate(heightmap):
    for x, height in enumerate(line):
        # create a list of neighbours
        neighbours = {}
        # check if the neighbour is above
        if y > 0:
            neighbour = (x, y - 1)
            # check if the neighbour is reachable
            if heightmap[neighbour[1]][neighbour[0]] <= height + 1:
                # add the neighbour to the list
                neighbours[neighbour] = 1
        # check if the neighbour is below
        if y < len(heightmap) - 1:
            neighbour = (x, y + 1)
            # check if the neighbour is reachable
            if heightmap[neighbour[1]][neighbour[0]] <= height + 1:
                # add the neighbour to the list
                neighbours[neighbour] = 1
        # check if the neighbour is left
        if x > 0:
            neighbour = (x - 1, y)
            # check if the neighbour is reachable
            if heightmap[neighbour[1]][neighbour[0]] <= height + 1:
                # add the neighbour to the list
                neighbours[neighbour] = 1
        # check if the neighbour is right
        if x < len(line) - 1:
            neighbour = (x + 1, y)
            # check if the neighbour is reachable
            if heightmap[neighbour[1]][neighbour[0]] <= height + 1:
                # add the neighbour to the list
                neighbours[neighbour] = 1
        # add the node to the graph
        graph[(x, y)] = neighbours

# dijkstra's algorithm for multiple start nodes


def dijkstra_multiple(graph, starts, end):
    # create a list of distances
    distances = {node: float('inf') for node in graph}
    for start in starts:
        distances[start] = 0
    # create a list of previous nodes
    previous = {node: None for node in graph}
    # create a list of unvisited nodes
    unvisited = set(graph)
    # loop until all nodes are visited
    while unvisited:
        # find the node with the smallest distance
        current = min(unvisited, key=lambda node: distances[node])
        # check if the node is the end node
        if current == end:
            # return the shortest path
            path = []
            while previous[current] is not None:
                path.append(current)
                current = previous[current]
            path.append(start)
            return path[::-1]
        # mark the node as visited
        unvisited.remove(current)
        # update distances
        for neighbour in graph[current]:
            # calculate new distance
            new_distance = distances[current] + graph[current][neighbour]
            # check if the distance is shorter
            if new_distance < distances[neighbour]:
                # update the distance
                distances[neighbour] = new_distance
                # update the previous node
                previous[neighbour] = current
    # return None if no path was found
    return None


# get all fields where hegiht is 0
starts = [(x, y) for y, line in enumerate(heightmap)
          for x, height in enumerate(line) if height == 0]
# find shortest path using dijkstra's algorithm
path = dijkstra_multiple(graph, starts, end)
# print the path
print(len(path) - 1)
