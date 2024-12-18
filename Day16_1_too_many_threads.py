import time
start_time = time.time()

# files/day16_test_1.txt 7036
# files/day16_test_2.txt 11048
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
            elif char == 'E':
                end = (x, y)

class Reindeer:
    def __init__(self):
        self.location = None
        self.locations = []

solutions = []
def solve(reindeer, location):
    reindeer.location = location
    if reindeer.location == end:
        reindeer.locations.append(reindeer.location)
        solutions.append(reindeer.locations)
    elif reindeer.location not in reindeer.locations:
        reindeer.locations.append(reindeer.location)
        choices = [(reindeer.location[0] - 1, reindeer.location[1]), (reindeer.location[0], reindeer.location[1] - 1), (reindeer.location[0] + 1, reindeer.location[1]), (reindeer.location[0], reindeer.location[1] + 1)]
        if end in choices:
            solve(reindeer, end)
        steps = []
        for choice in choices:
            if choice in coordinates and choice not in reindeer.locations:
                steps.append(choice)
        if len(steps) > 0:
            copy = Reindeer()
            copy.location = reindeer.location
            copy.locations = reindeer.locations.copy()
            solve(reindeer, steps.pop(0))
            for step in steps:
                solve(copy, step)

def calculate_solution(solution):
    s = solution.copy()
    total = 0
    prev = s.pop(0)[1]
    direciton = '-'
    for step in s:
        total += 1
        if direciton == '-':
            if step[1] == prev:
                prev = step[1]
            else:
                total += 1000
                direciton = '|'
                prev = step[0]
        else:
            if step[0] == prev:
                prev = step[0]
            else:
                total += 1000
                direciton = '-'
                prev = step[1]
    return total

    

reindeer = Reindeer()
solve(reindeer, start)
min = 0
path = []
for solution in solutions:
    points = calculate_solution(solution)
    if points < min or min == 0:
        min = points
        path = solution

print(min)

print("Execution time: %s seconds" % (time.time() - start_time))

