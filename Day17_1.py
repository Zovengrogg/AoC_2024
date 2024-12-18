import time
start_time = time.time()

# files/day15_test_1.txt 2028
# files/day15_test_2.txt 10092
with open('files/day15.txt', 'r') as file:
    lines = file.readlines()


print("Execution time: %s seconds" % (time.time() - start_time))

