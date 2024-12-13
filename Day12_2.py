import time
start_time = time.time()

# files/day12_test1.txt 80
# files/day12_test3.txt 436
# files/day12_test4.txt 368
with open('files/day12.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]
    
farm = [row.copy() for row in data]

class Region:
    instances = []
    def __init__(self, plants):
        self.plants = plants
        self.perimeter = 0
        self.area = len(plants)
        self.letter = plants[0].letter
        Region.instances.append(self)
        self.create_corners()
        self.set_perimeter()

    def create_corners(self):
        corner_dict = {}
        for plant in self.plants:
            # LEFT
            if plant.perimeter[0] == 1:
                if plant.location in corner_dict:
                    corner_dict[plant.location] += ['bottom']
                else:
                    corner_dict[plant.location] = ['bottom']
                if (plant.location[0] + 1, plant.location[1]) in corner_dict:
                    corner_dict[(plant.location[0] + 1, plant.location[1])] += ['top']
                else:
                    corner_dict[(plant.location[0] + 1, plant.location[1])] = ['top']
            # TOP
            if plant.perimeter[1] == 1:
                if plant.location in corner_dict:
                    corner_dict[plant.location] += ['right']
                else:
                    corner_dict[plant.location] = ['right']
                if (plant.location[0], plant.location[1] + 1) in corner_dict:
                    corner_dict[(plant.location[0], plant.location[1] + 1)] += ['left']
                else:
                    corner_dict[(plant.location[0], plant.location[1] + 1)] = ['left']
            # BOTTOM
            if plant.perimeter[2] == 1:
                if (plant.location[0] + 1, plant.location[1]) in corner_dict:
                    corner_dict[(plant.location[0] + 1, plant.location[1])] += ['right']
                else:
                    corner_dict[(plant.location[0] + 1, plant.location[1])] = ['right']
                if (plant.location[0] + 1, plant.location[1] + 1) in corner_dict:
                    corner_dict[(plant.location[0] + 1, plant.location[1] + 1)] += ['left']
                else:
                    corner_dict[(plant.location[0] + 1, plant.location[1] + 1)] = ['left']
            # RIGHT
            if plant.perimeter[3] == 1:
                if (plant.location[0], plant.location[1] + 1) in corner_dict:
                    corner_dict[(plant.location[0], plant.location[1] + 1)] += ['bottom']
                else:
                    corner_dict[(plant.location[0], plant.location[1] + 1)] = ['bottom']
                if (plant.location[0] + 1, plant.location[1] + 1) in corner_dict:
                    corner_dict[(plant.location[0] + 1, plant.location[1] + 1)] += ['top']
                else:
                    corner_dict[(plant.location[0] + 1, plant.location[1] + 1)] = ['top']
        for corner in corner_dict:
            c = Corner(corner)
            for direction in corner_dict[corner]:
                c.attach(direction)

    def set_perimeter(self):
            for corner in Corner.instances:
                self.perimeter += corner.corner
            Corner.instances = []

    def price(self):
        return self.perimeter * self.area

# Perimeter is a tuple (left, top, right, bottom)
class Plant:
    instances = []
    def __init__(self, letter, location, perimeter):
        self.letter = letter
        self.location = location
        self.perimeter = perimeter
        Plant.instances.append(self)

class Corner:
    instances = []
    def __init__(self, location):
        self.location = location
        self.left = False
        self.top = False
        self.right = False
        self.bottom = False
        self.corner = 0
        Corner.instances.append(self)
    
    def attach(self, direciton):
        if direciton == 'left':
            self.left = True
        elif direciton == 'top':
            self.top = True
        elif direciton == 'right':
            self.right = True
        elif direciton == 'bottom':
            self.bottom = True
        self.corner = 2 if sum([self.left and self.top, self.right and self.bottom, self.left and self.bottom, self.right and self.top]) == 4 else sum([self.left and self.top, self.right and self.bottom, self.left and self.bottom, self.right and self.top])

def create_plant(letter, location):
    top = 0
    left = 0
    bottom = 0
    right = 0
    if location[1] == 0 or data[location[0]][location[1] - 1] != letter:
        left = 1
    if location[0] == 0 or data[location[0] - 1][location[1]] != letter:
        top = 1
    if location[0] == len(data) - 1 or data[location[0] + 1][location[1]] != letter:
        bottom = 1
    if location[1] == len(data[0]) - 1 or data[location[0]][location[1] + 1] != letter:
        right = 1
    return Plant(letter, location, [left, top, bottom, right])

def create_region(plant):
    plants = [plant]
    plots = [plant.location]
    for p in plants:
        if p.location[0] != 0 and farm[p.location[0] - 1][p.location[1]] == p.letter and [p.location[0] - 1, p.location[1]] not in plots:
            plants.append(create_plant(p.letter, (p.location[0] - 1, p.location[1])))
            plots.append([p.location[0] - 1, p.location[1]])
        if p.location[1] != 0 and farm[p.location[0]][p.location[1] - 1] == p.letter and [p.location[0], p.location[1] - 1] not in plots:
            plants.append(create_plant(p.letter, (p.location[0], p.location[1] - 1)))
            plots.append([p.location[0], p.location[1] - 1])
        if p.location[0] != len(farm) - 1 and farm[p.location[0] + 1][p.location[1]] == p.letter and [p.location[0] + 1, p.location[1]] not in plots:
            plants.append(create_plant(p.letter, (p.location[0] + 1, p.location[1])))
            plots.append([p.location[0] + 1, p.location[1]])
        if p.location[1] != len(farm[0]) - 1 and farm[p.location[0]][p.location[1] + 1] == p.letter and [p.location[0], p.location[1] + 1] not in plots:
            plants.append(create_plant(p.letter, (p.location[0], p.location[1] + 1)))
            plots.append([p.location[0], p.location[1] + 1])
        farm[p.location[0]][p.location[1]] = '.'
    return Region(plants)

for row in range(len(farm)):
    for plot in range(len(farm[row])):
        if farm[row][plot] != '.':
            create_region(create_plant(farm[row][plot], (row, plot)))
    
price = 0
for region in Region.instances:
    price += region.price()
print(price)

print("Execution time: %s seconds" % (time.time() - start_time))


