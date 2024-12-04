import csv

input_file = 'files/day2_1.csv'

with open(input_file, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    list1 = []
    for row in reader:
        values = row[0].split()
        row = [int(value) for value in values]
        list1.append(row)

def check_safety(row, tolerance):
    cont = True
    prev = row[0]
    errors = 0
    if row[1] == prev:
        errors += 1
        row = row[1:]
        prev = row[0]
        if row[1] == prev or errors > tolerance:
            return False, 1
    if row[1] > prev or row[2] > row[1]:
        for i in range(1, len(row)):
            if row[i] > prev:
                if row[i] - prev <= 3:
                    prev = row[i]
                else:
                    errors += 1
                    if errors > tolerance:
                        cont = False 
                        break
            else:
                errors += 1
                if errors > tolerance:
                    cont = False
                    break
        if cont:
            return True , i
    if not cont:
        return False, i
    prev = row[0]
    if row[1] < prev or row[2] < row[1]:
        for i in range(1, len(row)):
            if row[i] < prev:
                if prev - row[i] <= 3:
                    prev = row[i]
                else:
                    errors += 1
                    if errors > tolerance:
                        cont = False
                        break
            else:
                errors += 1
                if errors > tolerance:
                    cont = False
                    break
    return cont, i

safe = 0
for row in list1:
    safety, index = check_safety(row, 1)
    if safety:
        safe += 1
    else:
        alternate = row.copy()
        del alternate[0]
        safety, error = check_safety(alternate, 0)
        if safety:
            safe += 1
            continue
        alternate = row.copy()
        del alternate[index - 1]
        safety, error = check_safety(alternate, 0)
        if safety:
            safe += 1
            continue
        if index == len(row) - 1:
            print(row)
            continue
        alternate = row.copy()
        del alternate[index + 1]
        safety, error = check_safety(alternate, 0)
        if safety:
            safe += 1
            continue
        print(row)

print(safe)