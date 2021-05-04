"""
Написать программу сложения и умножения
двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция,
элементы которой — цифры числа.

Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма [‘C’, ‘F’, ‘1’],
произведение [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque
# hex_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]

a = deque(input('Веведите 1 число: ').upper())
b = deque(input('Веведите 2 число: ').upper())
sign = '+' #input('Веведите знак сложения (+) или умножения (*): ')
print()
print(a)
print(sign)
print(b)


from_hex = {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15}

to_hex = {0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'}

first = a.copy()
second = b.copy()

if len(first) < len(second):
    first, second = second, first

second.extendleft('0' * (len(first)-len(second)))

if sign == '+':
    summ = deque()
    i = -1
    dec = 0
    while abs(i) <= max(len(a), len(b)):
        num = from_hex[first[i]] + from_hex[second[i]]
        i -= 1
        num += dec
        dec = 0
        if num > 15:
            dec = 1
            num = num - 16
        ch = to_hex[num]
        summ.appendleft(ch)
    if dec > 0:
        summ.appendleft(str(dec))
    print('-' * 20)
    print(summ)
