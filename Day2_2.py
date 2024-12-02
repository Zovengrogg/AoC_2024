import csv

input_file = 'files/day2_1.csv'

with open(input_file, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    list1 = []
    for row in reader:
        values = row[0].split()
        row = [int(value) for value in values]
        list1.append(row)

def check_safety(row):
    cont = True
    prev = row[0]
    if row[1] == prev:
        return False
    if row[1] > prev:
        for i in range(1, len(row)):
            if row[i] > prev:
                if row[i] - prev <= 3:
                    prev = row[i]
                else:
                    cont = False
                    break
            else:
                cont = False
                break
    if not cont:
        return False
    prev = row[0]
    if row[1] < prev:
        for i in range(1, len(row)):
            if row[i] < prev:
                if prev - row[i] <= 3:
                    prev = row[i]
                else:
                    cont = False
                    break
            else:
                cont = False
                break
    return cont

safe = 0
for row in list1:
    if check_safety(row):
        safe += 1
        continue
    for i in range(0, len(row)):
        alternate = row.copy()
        del alternate[i]
        if check_safety(alternate):
            safe += 1
            break

print(safe)