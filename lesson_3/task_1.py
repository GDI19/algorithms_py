num_start = 2
num_fin = 99
div_start = 2
div_fin = 9

for i in range(div_start, div_fin + 1):
    result = 0
    for j in range(num_start, num_fin + 1):
        if j % i == 0:
            result += 1
    print(f'Для {i}: {result} чисел')
