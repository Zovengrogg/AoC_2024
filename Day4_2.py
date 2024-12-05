import numpy as np
import re

# x is the index starting from the bottom left, going up the column, and then around the corner to the right on the top row
# y is how far along the diagonal of that x you are
# length is the size of the crossword (which is a square)
def convert_index(a, b, length, direction):
    if direction == 'r':
        if a < length:
            return [b, a - b]
        else:
            return [a - length + 1 + b, length - 1 - b]
    elif direction == 'l':
        if a < length:
            return [a - b, length - 1 - b]
        else:
            return [length - 1 - b, 2 * length - 2 - a - b]
    

with open('files/day4_test.txt', 'r') as file:
    data = file.read()

crossword = data.splitlines()

df_crossword = np.array([list(row) for row in crossword])

diagonal_r_crossword = []
diagonal_l_crossword = []

# WARNING: FRAGILE CODE UP AHEAD
    # Important for conversion logic that we start from negative and go to positive (bottom to top of crossword)
for i in range(-len(df_crossword)+1, len(df_crossword)):
    diagonal_r_crossword.append(''.join(df_crossword.diagonal(offset=i)))
    diagonal_l_crossword.append(''.join(np.fliplr(df_crossword).diagonal(offset=i)))


pattern = re.compile(r'MAS')
pattern2 = re.compile(r'SAM')

index = 0
right_indexes = []
for line in diagonal_r_crossword:
    mas_match = re.search(pattern, line)
    if mas_match:
        right_indexes.append(convert_index(index, mas_match.start(), len(crossword), 'r'))
    
    sam_match = re.search(pattern2, line)
    if sam_match:
        right_indexes.append(convert_index(index, sam_match.start(), len(crossword), 'r'))
    index += 1

index = 0
left_indexes = []
for line in diagonal_l_crossword[::-1]:
    mas_match = re.search(pattern, line)
    if mas_match:
        left_indexes.append(convert_index(index, mas_match.start(), len(crossword), 'l'))
    
    sam_match = re.search(pattern2, line)
    if sam_match:
        left_indexes.append(convert_index(index, sam_match.start(), len(crossword), 'l'))
    index += 1

count = 0
for r in right_indexes:
    for l in left_indexes:
        if r[1] == l[1] and r[0] == l[0] - 2:
            count += 1

print(count)

