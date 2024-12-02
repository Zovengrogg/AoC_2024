import csv

file_path = 'files/day1_1.csv'

list1 = []
list2 = []

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        list1.append(int(row[0]))
        list2.append(int(row[1]))

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    sum += diff
    print(f'{list1[i]} - {list2[i]} = {diff}')

print(sum)