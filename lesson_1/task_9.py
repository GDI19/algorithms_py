print('Введите три числа')
a = int(input('первое число a: '))
b = int(input('первое число b: '))
c = int(input('первое число c: '))

if a > b:
    if b > c:
        print(f'Число {b} является средним')
    else:
        if a > c:
            print(f'Число {c} является средним')
        else:
            print(f'Число {a} является средним')
elif a < b:
    if a > c:
        print(f'Число {a} является средним')
    else:
        if b > c:
            print(f'Число {c} является средним')
        else:
            print(f'Число {b} является средним')
