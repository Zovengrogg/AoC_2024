import time
start_time = time.time()

# files/day17_test.txt 117440
with open('files/day17_test.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    lines = lines[:3]+lines[4:]

A = int(lines[0].split(': ')[1])
B = int(lines[1].split(': ')[1])
C = int(lines[2].split(': ')[1])
instructions = [int(number) for number in lines[-1].split(': ')[1].split(',')]
pointer = 0
output = ''

def get_combo(operand):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    if operand == 7:
        print("Error: Invalid operand")
        exit()

def adv(operand):
    global A
    combo = get_combo(operand)
    A = A // (2**combo)
    return pointer + 2

def bxl(operand):
    global B
    B = B ^ operand
    return pointer + 2

def bst(operand):
    global B
    combo = get_combo(operand)
    B = combo % 8
    return pointer + 2

def jnz(operand):
    if A != 0:
        return operand
    return pointer + 2

def bxc(operand):
    global B
    global C
    B = B ^ C
    return pointer + 2

def out(operand):
    global output
    combo = get_combo(operand) % 8
    output += str(combo) + ','
    return pointer + 2

def bdv(operand):
    global B
    combo = get_combo(operand)
    B = A // (2**combo)
    return pointer + 2

def cdv(operand):
    global C
    combo = get_combo(operand)
    C = A // (2**combo)
    return pointer + 2

while pointer < len(instructions) - 1:
    opcode = instructions[pointer]
    operand = instructions[pointer + 1]
    if opcode == 0:
        pointer = adv(operand)
    elif opcode == 1:
        pointer = bxl(operand)
    elif opcode == 2:
        pointer = bst(operand)
    elif opcode == 3:
        pointer = jnz(operand)
    elif opcode == 4:
        pointer = bxc(operand)
    elif opcode == 5:
        pointer = out(operand)
    elif opcode == 6:
        pointer = bdv(operand)
    elif opcode == 7:
        pointer = cdv(operand)
    else:
        print("Error: Invalid opcode")
        exit()

print(output[:-1])
print("Execution time: %s seconds" % (time.time() - start_time))

