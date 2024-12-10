import time
start_time = time.time()

with open('files/day10.txt', 'r') as file:
    data = [list(map(int, line)) for line in file.read().splitlines()]

class Hiker:
    def __init__(self, coordinates, new_coordinates, level):
        self.coordinates = coordinates
        self.new_coordinates = new_coordinates
        self.level = level
    
    def walk_right(self, coordinate, level):
        right = coordinate[1] + 1
        if(right >= len(data[0])):
            return False
        if(data[coordinate[0]][right] == level + 1):
            self.new_coordinates.append([coordinate[0], right])
            return True
        return False


    def walk_left(self, coordinate, level):
        left = coordinate[1] - 1
        if(left < 0):
            return False
        if(data[coordinate[0]][left] == level + 1):
            self.new_coordinates.append([coordinate[0], left])
            return True
        return False

    def walk_up(self, coordinate, level):
        up = coordinate[0] - 1
        if(up < 0):
            return False
        if(data[up][coordinate[1]] == level + 1):
            self.new_coordinates.append([up, coordinate[1]])
            return True
        return False

    def walk_down(self, coordinate, level):
        down = coordinate[0] + 1
        if(down >= len(data)):
            return False
        if(data[down][coordinate[1]] == level + 1):
            self.new_coordinates.append([down, coordinate[1]])
            return True
        return False

    def take_the_step(self):
        for coordinate in self.coordinates:
            self.walk_right(coordinate, self.level)
            self.walk_left(coordinate, self.level)
            self.walk_up(coordinate, self.level)
            self.walk_down(coordinate, self.level)
        self.coordinates = self.new_coordinates
        self.new_coordinates = []


count = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        level = data[x][y]
        if level == 0:
            hiker = Hiker([[x, y]], [], level)
            while hiker.level < 9:
                hiker.take_the_step()
                hiker.level += 1
            count += len(hiker.coordinates)

print(count)

print("Execution time: %s seconds" % (time.time() - start_time))
