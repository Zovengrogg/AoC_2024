# A more fun but not any more effecient way
import time
start_time = time.time()

with open('files/day11.txt', 'r') as file:
    pebbles = list(map(int, file.read().split()))

total_blinks = 25

def rule1(number):
    return [1]

def rule2(number):
    split_number = divmod(number, 10**(len(str(number))//2))
    return [split_number[0], split_number[1]]

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

def fill_out(pebble):
    pebbles = pebble
    for _ in range(total_blinks):
        next_numbers = []
        for number in pebbles[-1]:
            next_numbers.extend(resolve(number))
        pebbles[-1] = len(pebbles[-1])
        pebbles.append(next_numbers)
    pebbles[-1] = len(pebbles[-1])
    return pebbles

one_count = fill_out([[1]])
zero_count = [1] + one_count[:-1]
two_count = fill_out([[2]])
three_count = fill_out([[3]])
four_count = fill_out([[4]])
five_count = fill_out([[5]])
six_count = fill_out([[6]])
seven_count = fill_out([[7]])
eight_count = fill_out([[8]])
nine_count = fill_out([[9]])

blinks = 0
count = 0
while blinks < total_blinks:
    new_pebbles = []
    length = len(pebbles) - 1
    for index in range(length, -1, -1):
        number = pebbles[index]
        if number == 0:
            count += zero_count[total_blinks - blinks]
        elif number == 1:
            count += one_count[total_blinks - blinks]
        elif number == 2:
            count += two_count[total_blinks - blinks]
        elif number == 3:
            count += three_count[total_blinks - blinks]
        elif number == 4:
            count += four_count[total_blinks - blinks]
        elif number == 5:
            count += five_count[total_blinks - blinks]
        elif number == 6:
            count += six_count[total_blinks - blinks]
        elif number == 7:
            count += seven_count[total_blinks - blinks]
        elif number == 8:
            count += eight_count[total_blinks - blinks]
        elif number == 9:
            count += nine_count[total_blinks - blinks]
        else:
            new_pebbles.extend(resolve(number))
        pebbles.remove(number)
    blinks += 1
    pebbles = pebbles + new_pebbles


count += len(pebbles)
print(count)


print("Execution time: %s seconds" % (time.time() - start_time))