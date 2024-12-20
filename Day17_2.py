import time
start_time = time.time()

# files/day17_test.txt 117440
with open('files/day17.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    lines = lines[:3]+lines[4:]

A = 0
B = int(lines[1].split(': ')[1])
C = int(lines[2].split(': ')[1])
instructions = [int(number) for number in lines[-1].split(': ')[1].split(',')]
pointer = 0
output = []

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
    combo = get_combo(operand)
    output.append(combo % 8)
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

def perform_forward_instruction(opcode, operand):
    global pointer
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

def run_forward():
    global pointer
    global output
    pointer = 0
    output = []
    while pointer < len(instructions) - 1:
        opcode = instructions[pointer]
        operand = instructions[pointer + 1]
        perform_forward_instruction(opcode, operand)

# 2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0

# B = A % 8            B is the last 3 bits of A
# B = B ^ 1            Flip the last bit of B
# C = A // (2**B)      C is the first len(A) - B bits of A
# B = B ^ 5            Flip the 3rd to last and last bits of B
# B = B ^ C             
# output B % 8
# A = A // (2**3)

# Since A only gets reassigned once at the end and we need the program to run 16 times 
# We need A to be between 8^15 and 8^16 (not includeing 8^16) to get the correct output 
# That is 246290604621824 possible values for A which is too much to brute force but it is a start
# We know the first value of A must make the first output 2

# B = [0, 1, 2, 3, 4, 5, 6, 7]
# B = [1, 0, 3, 2, 5, 4, 7, 6]
# C = A // (2**B)
# B = [4, 5, 6, 7, 0, 1, 2, 3]

# Solving for first output 2
#                                Brackets [] mean exactly those bits parenthesis () mean those bits come at the end with x being wild
#                                                                       X                X                                       X   
#                                                                    A=(xxx)  A=(xxx) A=(xxx) A=(xxx) A=(xxx) A=(xxx) A=(xxx) A=(xxx)              
# B = A % 8            B is the last 3 bits of A                     B=[001]  B=[010] B=[011] B=[100] B=[101] B=[110] B=[111] B=[000]
# B = B ^ 1            Flip the last bit of B                        B=[000]  B=[011] B=[010] B=[101] B=[100] B=[111] B=[110] B=[001]
# C = A // (2**B)      C is the first len(A) - B bits of A           C=(001)  C=(100) C=(xx0) C=(010) C=(011) C=(000) C=(001) C=(x00) <- C=(001)  C=(xx0) C=(xxx) C=(xxx) C=(xxx) C=(xxx) C=(xxx) C=(x00)
# B = B ^ 5            Flip the 3rd to last and last bits of B       B=[101]  B=[110] B=[111] B=[000] B=[001] B=[010] B=[011] B=[100]
# B = B ^ C            Last 3 bits of C XOR with B to make 010       B=(100)  B=(010) B=(011) B=(010) B=(010) B=(010) B=(010) B=(x00)
# output B % 8         The last 3 bits of B are 010                           A=(100010)
# A = A // (2**3)                                                                             A=(010xx100)
#                                                                                                     A=(011x101)
#                                                                                                             A=(000xxxx110)
#                                                                                                                     A=(001xxx111)
# Repeat above using                                                 A=(100) A=(0xx) A=(xxx) A=(xxx)

# After first manual pass we know A has to end with (in binary) 100010,   010xx100,   011x101,                  000xxxx110,                                001xxx111
#                                                                 34,    68/76/84/92,  87/95,  6/14/22/30/38/46/54/62/70/78/96/104/112/120/128/136,   7/15/23/31/39/47/55/63             

# But we make this into an algorithm

# How did I solve the first output?
# The last 3 bits of B must be the bin(instruction[0])[2:] by the output
# Before that, B is reassigned by B XOR C, both of which we don't have information on yet
# So, start at the beginning and work your way to the end
# The last 3 bits of A can be anything so B can be anything, we have 8 cases
# For all cases:
#     B = B ^ 1
#     if B == 000 then C = (001) 
#     if B == 001 then C = (x00)
#     if B == 010 then C = (xx1)
#     else C = (xxx)
#     B = B ^ 5
#     try can you replace 'x' in C such that B ^ C = bin(instruction[0])[2:] OR B ^ bin(instruction[0])[2:] == C where x is wild

# We then cut of the B portion of A with A = A // (2**B)
# We know some more information about A depending on the initial B and the found C that we need to maintain
# Recursively solve the problem for the next output for each remaining possible A 

#                         T   B   M   T   O
# Brute force (too large 246,290,604,621,824) coming up with better solution by trying to reduce this
# for temp in range(8**(len(instructions)-1), 8**len(instructions)):
#     A = temp
#     run_forward()
#     if output == instructions:
#         print(temp)
#         break


As=[bin(x)[2:].zfill(3) for x in range(8)]
A_mem = [bin(x)[2:].zfill(3) for x in range(8)]
temp = []
temp_mem = []
for i in range(len(instructions)):
    temp.clear()
    temp_mem.clear()
    while len(As) > 0:
        a = As.pop()
        a_mem = A_mem.pop()
        A = int(a, 2)
        B = A & 0b111
        B = B ^ 1
        ogB = B
        if A & 0b111 == 0b000:
            C = ['100', '000']
        elif A & 0b111 == 0b001:
            C = ['001']
        elif A & 0b111 == 0b011:
            C = ['000', '010', '100', '110']
        else:
            C = [bin(x)[2:].zfill(3) for x in range(8)]
        B = B ^ 5
        c = bin(B ^ int(instructions[i]))[2:].zfill(3)
        if c in C:
            if len(a) > ogB:
                if len(a) - 3 <= ogB:
                    if a[:len(a) - ogB - 1] == c[:len(a) - ogB - 1]:
                        newA = c + a[len(a) - ogB - 1:-3]
                        temp.append(newA)
                        temp_mem.append(newA+a_mem[-i*3:])
                elif a[len(a)-ogB-3:len(a)-ogB] == c:
                    temp.append(a[:-3])
                    temp_mem.append(a[:-3]+a_mem[-i*3:])
            else:
                if ogB > 3:
                    newA = [c + bin(x)[2:].zfill(ogB-3) for x in range(2**(ogB-3))]
                    for nA in newA:
                        temp_mem.append(nA + a_mem[-i*3:])
                        temp.append(nA)
                else:
                    newA = bin(int(c[:ogB],2))[2:].zfill(3)
                    temp.append(newA)
                    temp_mem.append(newA + a_mem[-i*3:])
    if temp != []:
        As = temp.copy()
        A_mem = temp_mem.copy()

print("Execution time: %s seconds" % (time.time() - start_time))

