import csv

file_path = 'files/day1_1.csv'

list1 = []
list2 = []

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        list1.append(int(row[0]))
        list2.append(int(row[1]))

sum = 0
for i in range(len(list1)):
    count = list2.count(list1[i])
    sum += count*list1[i]
    print(f'{list1[i]}, {count}')

print(sum)