import time
start_time = time.time()

with open('files/day9.txt', 'r') as file:
    data = file.read()
    # Divides the data into used memory and free space since they are alternating in the data
    used_memory = [int(data[i]) for i in range(len(data)) if i % 2 == 0]
    free_memory = [int(data[i]) for i in range(len(data)) if i % 2 != 0]


memory = []
index = 0
for x in range(0, len(used_memory)-1):
    memory.extend([index] * int(used_memory[x]))
    memory.extend(['.'] * int(free_memory[x]))
    index += 1

memory.extend([index] * int(used_memory[len(used_memory)-1]))

for x in range(len(used_memory)-1, 0, -1):
    moved_memory = used_memory[x]
    # first_free_index = next(i for i, v in enumerate(free_memory) if v > 0)
    for y in range(0, x):
        if moved_memory <= free_memory[y]:
            memory = memory[:memory.index(y+1)-free_memory[y]] + memory[memory.index(x):memory.index(x)+moved_memory] + memory[memory.index(y+1) - free_memory[y] + moved_memory:memory.index(x)] + ['.'] * moved_memory + memory[memory.index(x)+moved_memory:]
            free_memory[y] -= moved_memory
            break

memory = [0 if x == '.' else x for x in memory]
result = sum(index * value for index, value in enumerate(memory))
print(f"Sum of the values of memory multiplied by their index: {result}")
    

print("Execution time: %s seconds" % (time.time() - start_time))