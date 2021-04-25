import random

SIZE = 10
MIN_D = 0
MAX_D = 100
array = [random.randint(MIN_D, MAX_D) for _ in range(SIZE)]
print(array)

odd_num_index = []
for i in range(len(array)):
    if array[i] % 2 != 0:
        odd_num_index.append(i)

print(odd_num_index)