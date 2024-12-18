import time
start_time = time.time()

# files/day15_test_2.txt 9021
with open('files/day15.txt', 'r') as file:
    lines = file.readlines()

block1, block2 = ''.join(lines).split('\n\n')

hash_locations = []
left_locations = []
right_locations = []
for y, line in enumerate(block1.split('\n')):
    for x, char in enumerate(line):
        if char == '#':
            hash_locations.append((2*x, y))
            hash_locations.append((2*x + 1, y))
        elif char == 'O':
            left_locations.append((2*x, y))
            right_locations.append((2*x + 1, y))
        elif char == '@':
            robot = (2*x, y)

movements = ''.join(block2.split('\n'))

def move(location, direction):
    x, y = location
    if (location[0] + (direction == '>') - (direction == '<'), location[1] + (direction == 'v') - (direction == '^')) in hash_locations:
        return False
    if direction == '^':
        if (x, y - 1) in left_locations:
            if move((x, y - 1), direction) and move((x + 1, y - 1), direction):
                left_locations.remove((x, y - 1))
                left_locations.append((x, y - 2))
                right_locations.remove((x + 1, y - 1))
                right_locations.append((x + 1, y - 2))
            else:
                return False
        if (x, y - 1) in right_locations:
            if move((x, y - 1), direction) and move((x - 1, y - 1), direction):
                right_locations.remove((x, y - 1))
                right_locations.append((x, y - 2))
                left_locations.remove((x - 1, y - 1))
                left_locations.append((x - 1, y - 2))
            else:
                return False
    elif direction == '>':
        if (x + 1, y) in left_locations:
            if move((x + 2, y), direction):
                left_locations.remove((x + 1, y))
                left_locations.append((x + 2, y))
                right_locations.remove((x + 2, y))
                right_locations.append((x + 3, y))
            else:
                return False
    elif direction == 'v':
        if (x, y + 1) in left_locations:
            if move((x, y + 1), direction) and move((x + 1, y + 1), direction):
                left_locations.remove((x, y + 1))
                left_locations.append((x, y + 2))
                right_locations.remove((x + 1, y + 1))
                right_locations.append((x + 1, y + 2))
            else:
                return False
        if (x, y + 1) in right_locations:
            if move((x, y + 1), direction) and move((x - 1, y + 1), direction):
                right_locations.remove((x, y + 1))
                right_locations.append((x, y + 2))
                left_locations.remove((x - 1, y + 1))
                left_locations.append((x - 1, y + 2))
            else:
                return False
    elif direction == '<':
        if (x - 1, y) in right_locations:
            if move((x - 2, y), direction):
                right_locations.remove((x - 1, y))
                right_locations.append((x - 2, y))
                left_locations.remove((x - 2, y))
                left_locations.append((x - 3, y))
            else:
                return False
    return True

for movement in movements:
    # printing changes
    # grid = [['.' for _ in range(max(x for x, y in hash_locations + left_locations + right_locations + [robot]) + 1)] for _ in range(max(y for x, y in hash_locations + left_locations + right_locations + [robot]) + 1)]

    # for x, y in hash_locations:
    #     grid[y][x] = '#'
    # for x, y in left_locations:
    #     grid[y][x] = '['
    # for x, y in right_locations:
    #     grid[y][x] = ']'
    # grid[robot[1]][robot[0]] = '@'

    # for row in grid:
    #     print(''.join(row))
    # print(movement)
    if move(robot, movement):
        robot = (robot[0] + (movement == '>') - (movement == '<'), robot[1] + (movement == 'v') - (movement == '^'))

print(sum([abs(x) + abs(y)*100 for x, y in left_locations]))   
print("Execution time: %s seconds" % (time.time() - start_time))


