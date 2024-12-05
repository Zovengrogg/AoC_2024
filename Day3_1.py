import re

with open('files/day3_1.txt', 'r') as file:
    content = file.read()

pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'

matches = re.findall(pattern, content)

sum = 0
for match in matches:
    numbers = re.findall(r'\d+', match)
    numbers = list(map(int, numbers))
    sum += numbers[0] * numbers[1]

print(sum)