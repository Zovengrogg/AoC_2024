import re

with open('files/day3.txt', 'r') as file:
    content = file.read()

sum = 0
parts = content.split('do()')
for part in parts:
    do = part.split('don\'t()')
    print('START ******', do[0])

    pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'

    matches = re.findall(pattern, do[0])

    for match in matches:
        numbers = re.findall(r'\d+', match)
        numbers = list(map(int, numbers))
        sum += numbers[0] * numbers[1]

print(sum)