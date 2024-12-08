from itertools import product

with open('files/day7.txt', 'r') as file:
    content = file.read()
    calibrations = [[int(value) if value.isdigit() else value for value in line.replace(':', '').split()] for line in content.splitlines()]

def try_all_combinations(answer, calibration):
    operators = ['+', '*']
    for ops in product(operators, repeat=len(calibration)-1):
        total = calibration[0]
        for i, op in enumerate(ops):
            if op == '+':
                total += calibration[i+1]
            elif op == '*':
                total *= calibration[i+1]
        if total == answer:
            return True
    return False

correct_calibrations = 0
for line in calibrations:
    if try_all_combinations(line[0], line[1:]):
        correct_calibrations += line[0]

print(correct_calibrations)
