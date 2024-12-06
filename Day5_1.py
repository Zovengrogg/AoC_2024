file_path = 'files/day5_1.txt'
file_path_2 = 'files/day5_2.txt'

rules = []
with open(file_path, 'r') as file:
    data = file.read().splitlines()
    for d in data:
        rules.append(d.split('|'))

updates = []
with open(file_path_2, 'r') as file:
    data_2 = file.read().splitlines()
    for d in data_2:
        updates.append(d.split(','))

dict_rules = {}
for rule in rules:
    key = rule[0]
    value = dict_rules[key] + ',' + rule[1] if key in dict_rules else rule[1]
    dict_rules[key] = value

def check_rules(update):
    for page in range(0, len(update)):
        for prev in range(0, page):
            if update[page] in dict_rules:
                if update[prev] in dict_rules[update[page]]:
                    return False
    return True

sum = 0
for update in updates:
    if check_rules(update):
        middle_value = update[len(update) // 2]
        sum += int(middle_value)

print(sum)
