import time
from itertools import combinations
from math import gcd
start_time = time.time()

with open('files/day8.txt', 'r') as file:
    data = file.read().splitlines()

dict_locations = {}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char != '.':
            key = char
            value = dict_locations[key] + [[i, j]] if key in dict_locations else [[i, j]]
            dict_locations[key] = value

def solve():
    width = len(data[0])
    height = len(data)
    points = set()
    for key in dict_locations:
        pairs = list(combinations(dict_locations[key], 2))
        for pair in pairs:
            x0, y0 = pair[0]
            x1, y1 = pair[1]
            dx = x1 - x0
            dy = y1 - y0
            gcden = abs(dx) if dy == 0 else abs(dy) if dx == 0 else abs(gcd(dx, dy))
            dx //= gcden
            dy //= gcden
            x, y = x0 + dx, y0 + dy
            while 0 <= x < height and 0 <= y < width:
                points.add((x, y))
                x += dx
                y += dy
            x, y = x0 + dx, y0 + dy
            while 0 <= x < height and 0 <= y < width:
                points.add((x, y))
                x -= dx
                y -= dy
            points.add((pair[0][0], pair[0][1]))
    print(len(points))

solve()

print("Execution time: %s seconds" % (time.time() - start_time))