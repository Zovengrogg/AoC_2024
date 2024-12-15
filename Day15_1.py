import time
start_time = time.time()

# files/day15_test_1.txt 2028
# files/day15_test_2.txt 10092
with open('files/day15.txt', 'r') as file:
    lines = file.readlines()

block1, block2 = ''.join(lines).split('\n\n')

hash_locations = []
o_locations = []
for y, line in enumerate(block1.split('\n')):
    for x, char in enumerate(line):
        if char == '#':
            hash_locations.append((x, y))
        elif char == 'O':
            o_locations.append((x, y))
        elif char == '@':
            robot = (x, y)

movements = ''.join(block2.split('\n'))

def move(location, direction):
    x, y = location
    if (location[0] + (direction == '>') - (direction == '<'), location[1] + (direction == 'v') - (direction == '^')) in hash_locations:
        return False
    if direction == '^':
        if (x, y - 1) in o_locations:
            if move((x, y - 1), direction):
                o_locations.remove((x, y - 1))
                o_locations.append((x, y - 2))
            else:
                return False
    elif direction == '>':
        if (x + 1, y) in o_locations:
            if move((x + 1, y), direction):
                o_locations.remove((x + 1, y))
                o_locations.append((x + 2, y))
            else:
                return False
    elif direction == 'v':
        if (x, y + 1) in o_locations:
            if move((x, y + 1), direction):
                o_locations.remove((x, y + 1))
                o_locations.append((x, y + 2))
            else:
                return False
    elif direction == '<':
        if (x - 1, y) in o_locations:
            if move((x - 1, y), direction):
                o_locations.remove((x - 1, y))
                o_locations.append((x - 2, y))
            else:
                return False
    return True

for movement in movements:
    if move(robot, movement):
        robot = (robot[0] + (movement == '>') - (movement == '<'), robot[1] + (movement == 'v') - (movement == '^'))
        
        # printing changes
        # grid = [['.' for _ in range(max(x for x, y in hash_locations + o_locations + [robot]) + 1)] for _ in range(max(y for x, y in hash_locations + o_locations + [robot]) + 1)]

        # for x, y in hash_locations:
        #     grid[y][x] = '#'
        # for x, y in o_locations:
        #     grid[y][x] = 'O'
        # grid[robot[1]][robot[0]] = '@'

        # for row in grid:
        #     print(''.join(row))
        # print(movement)

print(sum([abs(x) + abs(y)*100 for x, y in o_locations]))   
print("Execution time: %s seconds" % (time.time() - start_time))


