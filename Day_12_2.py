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
        self.perimeter = sum(plant.perimeter for plant in plants)
        self.area = len(plants)
        self.letter = plants[0].letter
        Region.instances.append(self)
        

class Plant:
    instances = []
    def __init__(self, letter, location, perimeter):
        self.letter = letter
        self.location = location
        self.perimeter = perimeter
        Plant.instances.append(self)

def create_plant(letter, location):
    perimeter = 0
    if location[0] == 0 or data[location[0] - 1][location[1]] != letter:
        perimeter += 1
    if location[1] == 0 or data[location[0]][location[1] - 1] != letter:
        perimeter += 1
    if location[0] == len(data) - 1 or data[location[0] + 1][location[1]] != letter:
        perimeter += 1
    if location[1] == len(data[0]) - 1 or data[location[0]][location[1] + 1] != letter:
        perimeter += 1
    return Plant(letter, location, perimeter)

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
    price += region.perimeter * region.area
    # print(region.letter, region.perimeter, region.area)
print(price)

print("Execution time: %s seconds" % (time.time() - start_time))


