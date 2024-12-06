import re

with open('files/day6.txt', 'r') as file:
    content = file.read()
    shift = content.splitlines()

    for i, line in enumerate(shift):
        if '^' in line:
            col = line.index('^')
            start = [i, col]

location = start
positions = [location]
direction = 'up'
while True:
    if direction == 'up':
        location = [location[0] - 1, location[1]]
        if location not in positions:
            positions.append(location)
        if location[0] - 1 < 0:
            break
        if shift[location[0] - 1][location[1]] == '#':
            direction = 'right'
    
    if direction == 'right':
        location = [location[0], location[1] + 1]
        if location not in positions:
            positions.append(location)
        if location[1] + 1 >= len(shift[0]):
            break
        if shift[location[0]][location[1] + 1] == '#':
            direction = 'down'
    
    if direction == 'down':
        location = [location[0] + 1, location[1]]
        if location not in positions:
            positions.append(location)
        if location[0] + 1 >= len(shift):
            break
        if shift[location[0] + 1][location[1]] == '#':
            direction = 'left'
    
    if direction == 'left':
        location = [location[0], location[1] - 1]
        if location not in positions:
            positions.append(location)
        if location[1] - 1 < 0:
            break
        if shift[location[0]][location[1] - 1] == '#':
            direction = 'up'

print(len(positions))