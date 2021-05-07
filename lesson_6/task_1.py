"""
Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32
и заканчивая 127-м включительно.
Вывод выполнить в табличной форме:
по десять пар "код-символ" в каждой строке.
"""
import sys

start = 32
end = 127
step = 10


def ascii_print_1(start, end, step):
    memory_list = []
    while start < 127:
        if start == 122:
            step = 6

        result = ''
        memory_size = 0
        for i in range(start, start + step):
            result = result + str(i) + '  ' + chr(i) + '  '

        start = start + step
        print(result)
        print('-' * len(result))
        size_res = sys.getsizeof(result)
        print(size_res)
        print('-' * len(result))
        memory_size += size_res + start + end + step
        memory_list.append(memory_size)

    return memory_list


# print(ascii_print_1(start, end, step))
"""
За время работы функции используется 1451 bytes,
но т.к. строка перезаписывается то получается максимальный объем
используемый 388 байт Python 3.8.3 windows 10 (64x)"""


# ---------------------------------------------------------------------

def ascii_print_2(start, end, step):
    memory_list = []
    while start < 127:
        if start == 122:
            step = 6

        result = []
        memory_size = 0
        for i in range(start, start + step):
            result.append(str(i) + '  ' + chr(i) + '  ')

        start = start + step
        print(result)
        print('-' * len(result))
        size_res = sys.getsizeof(result)
        print(size_res)
        for item in result:
            item_size = sys.getsizeof(item)
            memory_size += item_size
            print(item_size)

        print('-' * len(result))
        memory_size += size_res

        memory_size = memory_size + start + end + step
        memory_list.append(memory_size)

    return memory_list


# print(ascii_print_2(start, end, step))
"""
за время функции используется 7441 bytes, но 
т.к. список перезаписывается то максимальный размер 
состовляет 1013 байт Python 3.8.3 windows 10 (64x)
"""
# ----------------------------------------------------------------------

list_ascii = [chr(i) for i in range(0, 128)]


def ascii_print_3(start, end, step):
    count = 1
    for i in range(start, end + 1):
        print(f'{i}  {list_ascii[i]}', end=' | ')
        if count % step != 0:
            count += 1
        else:
            print()
            count += 1


ascii_print_3(start, end, step)

"""
print(sys.getsizeof(list_ascii))
total_size = 0
for item in list_ascii:
    size = sys.getsizeof(item)
    total_size += size

print(total_size)

t_size = 0
for i in range(127):
    size = sys.getsizeof(i)
    print(i, size )
    t_size += size
print(t_size)

созданный список ASCII занимает 7640 bytes, Python 3.8.3 windows 10 (64x)
функция лишь обращается к этим значениям

Кроме этого в выше приведенных функциях не учитывался 
цикл for i in range(32,128) займет 2660 байт = (28b * 95)
"""
