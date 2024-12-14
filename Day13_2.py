import time
start_time = time.time()

with open('files/day13.txt', 'r') as file:
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
    machine[2][0] += 10000000000000
    machine[2][1] += 10000000000000
    B = (machine[0][1]*machine[2][0]-machine[0][0]*machine[2][1])/(machine[0][1]*machine[1][0]-machine[0][0]*machine[1][1])
    A = (machine[2][0]-machine[1][0]*B)/machine[0][0]
    if A.is_integer() and B.is_integer():
        tokens += int(B)
        tokens += 3*int(A)
print(tokens)

print("Execution time: %s seconds" % (time.time() - start_time))

