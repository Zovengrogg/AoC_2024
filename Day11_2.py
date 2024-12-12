# A more fun but not any more effecient way
import time
start_time = time.time()

with open('files/day11.txt', 'r') as file:
    pebbles = list(map(int, file.read().split()))

# Create a map
# Create a function that will return the value of the map if the key exists
    # If the key does not exist, use rules to determine what is sent in callback function and save it
    # Then insert the return function value into the map undeer the key. Make sure to decrement the blinks
    # Key is the arguments of the function

dict_pebbles = {}
def blink(pebble, blinks):
    key = f"{pebble},{blinks}"
    if key in dict_pebbles:
        return dict_pebbles[key]
    
    if blinks == 0:
        value = 1
    elif pebble == 0:
        value = blink(1, blinks - 1)
    elif len(str(pebble)) % 2 == 0:
        split_number = divmod(pebble, 10**(len(str(pebble))//2))
        value = blink(split_number[0], blinks - 1) + blink(split_number[1], blinks - 1)
    else:
        value = blink(pebble * 2024, blinks - 1)
    dict_pebbles[key] = value
    return value

def solve(b):
    sum_pebbles = 0
    for x in pebbles:
        sum_pebbles += blink(x, b)
    return sum_pebbles

# print(solve(6))
# print(solve(25))
print(solve(75))

print("Execution time: %s seconds" % (time.time() - start_time))