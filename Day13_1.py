import time
start_time = time.time()

# files/day12_test.txt 480
with open('files/day13.txt', 'r') as file:
    # Create a list of lists broken down by 4 lines and split by ':' removing X+, Y+, Button, X=, y=
    # For example:
        # Button A: X+94, Y+34
        # Button B: X+22, Y+67
        # Prize: X=8400, Y=5400
        # 
    # would be broken down into: 
        # [['94', '34'], ['22', '67'], ['8400', '5400']]
    data = []
    while True:
        lines = [file.readline().strip() for _ in range(4)]
        if not lines[0]:
            break
        parsed_lines = []
        for line in lines[:-1]:
            parts = line.split(': ')[1].split(', ')
            parsed_line = [int(part[2:]) for part in parts]
            parsed_lines.append(parsed_line)
        data.append(parsed_lines)

tokens = 0
for machine in data:
    B = (machine[0][1]*machine[2][0]-machine[0][0]*machine[2][1])/(machine[0][1]*machine[1][0]-machine[0][0]*machine[1][1])
    A = (machine[2][0]-machine[1][0]*B)/machine[0][0]
    if A.is_integer() and B.is_integer():
        tokens += int(B)
        tokens += 3*int(A)
print(tokens)

print("Execution time: %s seconds" % (time.time() - start_time))

