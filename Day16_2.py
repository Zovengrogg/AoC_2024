import time
import heapq
from operator import add
start_time = time.time()

# files/day16_test_1.txt 45
# files/day16_test_2.txt 64
with open('files/day16.txt', 'r') as file:
    lines = file.readlines()

    coordinates = []
    start = None
    end = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == '.':
                coordinates.append((x, y))
            elif char == 'S':
                start = (x, y)
                coordinates.append((x, y))
            elif char == 'E':
                end = (x, y)
                coordinates.append((x, y))

class Node:
    nodes = {}
    def __init__(self, location):
        self.location = location
        self.visited = False
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.neighbors = []
        self.count = 0
        Node.nodes[location] = self

    def set_count(self):
        self.count = 0
        self.neighbors = []
        if self.north is not None:
            self.count += 1
            self.neighbors.append(self.north)
        if self.east is not None:
            self.count += 1
            self.neighbors.append(self.east)
        if self.south is not None:
            self.count += 1
            self.neighbors.append(self.south)
        if self.west is not None:
            self.count += 1
            self.neighbors.append(self.west)

    def remove_node(self):
        if self.north is not None:
            self.north.south = None
            other_node = self.north
        if self.east is not None:
            self.east.west = None
            other_node = self.east
        if self.south is not None:
            self.south.north = None
            other_node = self.south
        if self.west is not None:
            self.west.east = None
            other_node = self.west
        coordinates.remove(self.location)
        del Node.nodes[self.location]
        return other_node

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
stack = []
def create_maze(node):
    for direction in directions:
        new_location = tuple(map(add, node.location, direction))
        if new_location in coordinates:
            if new_location not in Node.nodes:
                new_node = Node(new_location)
                stack.append(new_node)
            if direction == directions[0]:
                node.north = Node.nodes[new_location]
            elif direction == directions[1]:
                node.east = Node.nodes[new_location]
            elif direction == directions[2]:
                node.south = Node.nodes[new_location]
            elif direction == directions[3]:
                node.west = Node.nodes[new_location]
            node.set_count()

node_start = Node(start)
stack.append(node_start)
while len(stack) > 0:
    node = stack.pop()
    create_maze(node)

for node in Node.nodes.values():
    if node.count == 1:
        stack.append(node)

while len(stack) > 0:
    node = stack.pop()
    if node.count == 1 and node.location != start and node.location != end:
        other_node = node.remove_node()
        stack.append(other_node)
        other_node.set_count()

def print_maze():
    maze = [[' ' for _ in range(len(lines[0].strip()))] for _ in range(len(lines))]

    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if (x, y) == start:
                maze[y][x] = 'S'
            elif (x, y) == end:
                maze[y][x] = 'E'
            else:
                maze[y][x] = '#'

    for node in Node.nodes.values():
        x, y = node.location
        maze[y][x] = 'X' if node.visited else '.'

    for line in maze:
        print(''.join(line))

solution = set()
def find_min_path(node, path, direction, total, memo):
    global min
    if (node, direction) in memo and memo[(node, direction)] < total:
        return False
    memo[(node, direction)] = total

    if total > min:
        return False

    if node.location == end:
        if total < min:
            min = total
            solution.clear()
        for step in path:
            solution.add(step[:])
        return True

    node.visited = True
    for neighbor in node.neighbors:
        add_on = 1
        if neighbor.south == node or neighbor.north == node:
            new_direction = '|'
            if direction == '-':
                add_on += 1000
        else:
            new_direction = '-'
            if direction == '|':
                add_on += 1000
        if neighbor.visited:
            continue
        path.append(neighbor.location[:])
        find_min_path(neighbor, path, new_direction, total + add_on, memo)
        path.pop()
    node.visited = False
    return False

min = float('inf')
memo = {}
find_min_path(node_start, [start], '-', 0, memo)
print(len(solution))

print("Execution time: %s seconds" % (time.time() - start_time))

