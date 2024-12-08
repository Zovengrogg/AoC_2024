import time
from itertools import combinations
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
            slope = [(pair[1][0] - pair[0][0]) , (pair[1][1] - pair[0][1])]
            point = [pair[0][0] - slope[0], pair[0][1] - slope[1]]
            if 0 <= point[0] < height and 0 <= point[1]< width:
                points.add(tuple(point))
            point = [pair[1][0] + slope[0], pair[1][1] + slope[1]]
            if 0 <= point[0] < height and 0 <= point[1] < width:
                points.add(tuple(point))
    print(len(points))

solve()

print("Execution time: %s seconds" % (time.time() - start_time))