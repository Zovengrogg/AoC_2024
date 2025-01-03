import time
start_time = time.time()

# files/day17_test.txt 4,6,3,5,6,3,5,2,1,0
with open('files/day17.txt', 'r') as file:
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

def get_combo_rep(operand):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return 'A'
    if operand == 5:
        return 'B'
    if operand == 6:
        return 'C'
    if operand == 7:
        print("Error: Invalid operand")
        exit()

def adv(operand):
    global A
    combo = get_combo(operand)
    combo_rep = get_combo_rep(operand)
    A = A // (2**combo)
    print(f'A = A // (2**{combo_rep})')
    return pointer + 2

def bxl(operand):
    global B
    B = B ^ operand
    print(f'B = B ^ {operand}')
    return pointer + 2

def bst(operand):
    global B
    combo = get_combo(operand)
    combo_rep = get_combo_rep(operand)
    B = combo % 8
    print(f'B = {combo_rep} % 8')
    return pointer + 2

def jnz(operand):
    print(A)
    if A != 0:
        print('RESET')
        return operand
    print('FINISH')
    return pointer + 2

def bxc(operand):
    global B
    global C
    B = B ^ C
    print('B = B ^ C')
    return pointer + 2

def out(operand):
    global output
    combo = get_combo(operand)
    combo_rep = get_combo_rep(operand)
    output += str(combo % 8) + ','
    print(f'output {combo_rep} % 8')
    return pointer + 2

def bdv(operand):
    global B
    combo = get_combo(operand)
    combo_rep = get_combo_rep(operand)
    B = A // (2**combo)
    print(f'B = A // (2**{combo_rep})')
    return pointer + 2

def cdv(operand):
    global C
    combo = get_combo(operand)
    combo_rep = get_combo_rep(operand)
    C = A // (2**combo)
    print(f'C = A // (2**{combo_rep})')
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

