import random

SIZE = 10
MIN_D = -100
MAX_D = 100
array = [random.randint(MIN_D, MAX_D) for _ in range(SIZE)]
print(array)

MIN_VALUE = -99999999999999999999999999999999

min_neg = MIN_VALUE
index_min = []
for i in range(len(array)):
    a = array[i]
    if a < 0:
        if a > min_neg:
            min_neg = a
            index_min.append(i)

if min_neg == MIN_VALUE and len(index_min) < 1:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Максимально отрицательное число: {min_neg} \nНаходится в массиве под индексом: {index_min[-1]}')


