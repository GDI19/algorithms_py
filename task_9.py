""" Среди натуральных чисел, которые были введены
  найти наибольшее по сумме цифр. Вывести на экран
  это число и сумму его цифр.
"""
print('Чтобы узнать максимальную сумму цифр из чисел. '
      'Вводите числа по очереди. Для выхода введите 0')
max_num = 0
maximum = 0
while True:
    x = int(input('Введите число: '))
    result = 0
    if x > 0:
        for ch in str(x):
            result += int(ch)
        if maximum < result:
            maximum = result
            max_num = x
    else:
        break

print(f'Максимальная сумма цифр {maximum} у числа {max_num}')