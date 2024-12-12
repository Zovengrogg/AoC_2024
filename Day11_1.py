import time
start_time = time.time()

with open('files/day11.txt', 'r') as file:
    data = list(map(int, file.read().split()))

def rule1(number):
    return [1]

def rule2(number):
    return [int(str(number)[:len(str(number))//2]), int(str(number)[len(str(number))//2:])]

def rule3(number):
    return [number * 2024]

def resolve(number):
    new_data = []
    if number == 0:
        new_data.extend(rule1(number))
    elif len(str(number)) % 2 == 0:
        new_data.extend(rule2(number))
    else:
        new_data.extend(rule3(number))
    return new_data

blinks = 0
pebbles = data
while blinks < 25:
    new_pebbles = []
    for number in pebbles:
        new_pebbles.extend(resolve(number))
    pebbles = new_pebbles
    blinks += 1

print(len(pebbles))


print("Execution time: %s seconds" % (time.time() - start_time))