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

quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0
seconds = 100
length = 101
height = 103
mid_v = length // 2
mid_h = height//2
for line in data:
    pos = [line[0][0]+line[1][0]*seconds, line[0][1]+line[1][1]*seconds]
    pos = [pos[0]%length, pos[1]%height]
    if pos[0] < mid_v and pos[1] < mid_h:
        quad1 += 1
    elif pos[0] > mid_v and pos[1] < mid_h:
        quad2 += 1
    elif pos[0] < mid_v and pos[1] > mid_h:
        quad3 += 1
    elif pos[0] > mid_v and pos[1] > mid_h:
        quad4 += 1

print(quad1 * quad2 * quad3 * quad4)

    
print("Execution time: %s seconds" % (time.time() - start_time))

