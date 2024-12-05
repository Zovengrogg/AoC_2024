import numpy as np
import re
with open('files/day4_test.txt', 'r') as file:
    data = file.read()

crossword = data.splitlines()

df_crossword = np.array([list(row) for row in crossword])
df_transpose_crossword = df_crossword.T
        
transpose_crossword = [''.join(row) for row in df_transpose_crossword]

diagonal_crossword = []

for i in range(-len(df_crossword)+4, len(df_crossword)-3):
    diagonal_crossword.append(''.join(df_crossword.diagonal(offset=i)))
    diagonal_crossword.append(''.join(np.fliplr(df_crossword).diagonal(offset=i)))

full_crossword = crossword + transpose_crossword + diagonal_crossword

pattern = re.compile(r'XMAS')
pattern2 = re.compile(r'SAMX')
xmas_count = sum(len(pattern.findall(line)) for line in full_crossword)
samx_count = sum(len(pattern2.findall(line)) for line in full_crossword)
total_count = xmas_count + samx_count
print(total_count)