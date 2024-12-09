import time
start_time = time.time()

with open('files/day9.txt', 'r') as file:
    data = file.read()
    # Divides the data into used memory and free space since they are alternating in the data
    used_memory = [int(data[i]) for i in range(len(data)) if i % 2 == 0]
    free_space = [int(data[i]) for i in range(len(data)) if i % 2 != 0]




# Creates a full list of used memory without the freespace
index = 0
memory = []
for x in range(0, len(used_memory)):
    memory.extend([index] * int(used_memory[x]))
    index += 1

# Using the free space as a guide to move the memory around
x = 0
while memory[memory.index(x+1)] < memory[len(memory)-free_space[x]]:
    moved_memory = memory[-free_space[x]:]
    moved_memory = moved_memory[::-1]
    memory = memory[:memory.index(x+1)] + moved_memory + memory[memory.index(x+1):len(memory)-free_space[x]]
    x += 1
    while free_space[x] == 0:
        x += 1

result = sum(index * value for index, value in enumerate(memory))
print(f"Sum of the values of memory multiplied by their index: {result}")
    

print("Execution time: %s seconds" % (time.time() - start_time))