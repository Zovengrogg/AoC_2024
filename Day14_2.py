import time
start_time = time.time()

# files/day14_test.txt 12
# length = 11
# height = 7
with open('files/day14.txt', 'r') as file:
    data = []
    for line in file:
        parts = line.strip().split(' ')
        p = list(map(int, parts[0][2:].split(',')))
        v = list(map(int, parts[1][2:].split(',')))
        data.append([p, v])

seconds = 0
length = 101
height = 103
found = False
while found == False:
    positions = []
    for line in data:
        pos = [line[0][0]+line[1][0]*seconds, line[0][1]+line[1][1]*seconds]
        pos = [pos[0]%length, pos[1]%height]
        positions.append(pos)
    positions.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(positions) - 14):
        if all(positions[i+j][0] == positions[i][0] and positions[i+j][1] == positions[i][1] + j for j in range(15)):
            print(f"Found vertical set at {positions[i]} and {seconds} seconds")
            found = True
            time.sleep(2)
            grid = [['.' for _ in range(length)] for _ in range(height)]
            for pos in positions:
                grid[pos[1]][pos[0]] = 'X'

            for row in grid:
                print(''.join(row))
            print("\n\n\n")
        if all(positions[i+j][1] == positions[i][1] and positions[i+j][0] == positions[i][0] + j for j in range(15)):
            print(f"Found horizontal set at {positions[i]} and {seconds} seconds")
            found = True
            time.sleep(2)
            grid = [['.' for _ in range(length)] for _ in range(height)]
            for pos in positions:
                grid[pos[1]][pos[0]] = 'X'

            for row in grid:
                print(''.join(row))
            print("\n\n\n")
        if all(positions[i+j][0] == positions[i][0] + j and positions[i+j][1] == positions[i][1] + j for j in range(15)):
            print(f"Found diagonal set (\\) at {positions[i]} and {seconds} seconds")
            found = True
            time.sleep(2)
            grid = [['.' for _ in range(length)] for _ in range(height)]
            for pos in positions:
                grid[pos[1]][pos[0]] = 'X'

            for row in grid:
                print(''.join(row))
            print("\n\n\n")
        if all(positions[i+j][0] == positions[i][0] + j and positions[i+j][1] == positions[i][1] - j for j in range(15)):
            print(f"Found diagonal set (/) at {positions[i]} and {seconds} seconds")
            found = True
            time.sleep(2)
            grid = [['.' for _ in range(length)] for _ in range(height)]
            for pos in positions:
                grid[pos[1]][pos[0]] = 'X'

            for row in grid:
                print(''.join(row))
            print("\n\n\n")
    seconds += 1

    
print("Execution time: %s seconds" % (time.time() - start_time))

