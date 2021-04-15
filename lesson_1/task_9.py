# ссылка на схему https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=lesson1#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FGDI19%2Falgorithms_py%2Fmain%2Flesson1

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
