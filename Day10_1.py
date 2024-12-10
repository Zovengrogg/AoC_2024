import time
start_time = time.time()

with open('files/day10_test.txt', 'r') as file:
    data = file.read().splitlines()

class Hiker:
    def __init__(self, coordinate, level):
        self.coordinate = coordinate
        
        self.level = level
    
    @classmethod
    def walk_right(coordinate, level):
        if(data[coordinate[0]][coordinate[1]+1] == level + 1):
            return True
        return False

    def walk_left(coordinate, level):
        if(data[coordinate[0]][coordinate[1]-1] == level + 1):
            return True
        return False

    def walk_up(coordinate, level):
        if(data[coordinate[0]-1][coordinate[1]] == level + 1):
            return True
        return False

    def walk_down(coordinate, level):
        if(data[coordinate[0]+1][coordinate[1]] == level + 1):
            return True
        return False

for x, line in enumerate(data):
    for y, level in enumerate(line):
        if level == 0:
            hiker = Hiker([x, y], level)




print("Execution time: %s seconds" % (time.time() - start_time))
