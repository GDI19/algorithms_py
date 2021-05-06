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
    memory_size = 0
    while start < 127:
        if start == 122:
            step = 6

        result = ''
        for i in range(start, start + step):
            result = result + str(i) + '  ' + chr(i) + '  '

        start = start + step
        print(result)
        print('-' * len(result))
        size_res = sys.getsizeof(result)
        print(size_res)
        print('-' * len(result))
        memory_size += size_res

    memory_size = memory_size + start + end + step

    print(memory_size) # 1451 bytes Python 3.8.3 windows 10 (64x)

# ascii_print_1(start, end, step)

# ---------------------------------------------------------------------

def ascii_print_2(start, end, step):
    memory_size = 0
    while start < 127:
        if start == 122:
            step = 6

        result = []
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

    print(memory_size) # 7441 bytes Python 3.8.3 windows 10 (64x)

# ascii_print_2(start, end, step)

