import re

with open('files/day6.txt', 'r') as file:
    content = file.read()
    shift = content.splitlines()

    for i, line in enumerate(shift):
        if '^' in line:
            col = line.index('^')
            start = [i, col]

def run_shift(data):
    location = start
    up = [location]
    right = []
    down = []
    left = []
    direction = 'up'
    isLoop = False
    while True:
        if direction == 'up':
            location = [location[0] - 1, location[1]]
            if location in up:
                isLoop = True
                break
            up.append(location)
            if location[0] - 1 < 0:
                break
            if data[location[0] - 1][location[1]] == '#':
                direction = 'right'
                if data[location[0]][location[1] + 1] == '#':
                    direction = 'down'
                    if data[location[0] + 1][location[1]] == '#':
                        direction = 'left'
        
        if direction == 'right':
            location = [location[0], location[1] + 1]
            if location in right:
                isLoop = True
                break
            right.append(location)
            if location[1] + 1 >= len(data[0]):
                break
            if data[location[0]][location[1] + 1] == '#':
                direction = 'down'
                if data[location[0] + 1][location[1]] == '#':
                    direction = 'left'
                    if data[location[0]][location[1] - 1] == '#':
                        direction = 'up'
        
        if direction == 'down':
            location = [location[0] + 1, location[1]]
            if location in down:
                isLoop = True
                break
            down.append(location)
            if location[0] + 1 >= len(data):
                break
            if data[location[0] + 1][location[1]] == '#':
                direction = 'left'
                if data[location[0]][location[1] - 1] == '#':
                    direction = 'up'
                    if data[location[0] - 1][location[1]] == '#':
                        direction = 'right'
        
        if direction == 'left':
            location = [location[0], location[1] - 1]
            if location in left:
                isLoop = True
                break
            left.append(location)
            if location[1] - 1 < 0:
                break
            if data[location[0]][location[1] - 1] == '#':
                direction = 'up'
                if data[location[0] - 1][location[1]] == '#':
                    direction = 'right'
                    if data[location[0]][location[1] + 1] == '#':
                        direction = 'down'
    return up, right, down, left, isLoop

up, right, down, left, isLoop = run_shift(shift)
positions = set(tuple(pos) for pos in up + right + down + left)


loops = []
for pos in positions:
    data = shift.copy()
    data[pos[0]] = data[pos[0]][:pos[1]] + '#' + data[pos[0]][pos[1] + 1:] 
    if run_shift(data)[4]:
        loops.append(pos)



if start in loops:
    loops.remove(start)

print(len(loops))