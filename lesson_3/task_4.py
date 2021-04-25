import random

SIZE = 10
MIN_D = 0
MAX_D = 100
array = [random.randint(MIN_D, MAX_D) for _ in range(SIZE)]
print(array)

max_num = 0
max_count = 0
for d in array:
    new_count = array.count(d)
    if new_count > max_count:
        max_count = new_count
        max_num = d

print( max_num if max_count > 1 else f'Нет повторов' )
