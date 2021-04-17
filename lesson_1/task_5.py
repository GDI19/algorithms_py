print('Введите две буквы из латинского алфавита')

x = (input('Введите 1-ю букву: ')).lower()
y = (input('Введите 2-ю букву: ')).lower()

start = 96
a = ord(x) - start
b = ord(y) - start

diff = abs(a - b) - 1

print(f'У буквы {x} место в алфавите №: {a}')
print(f'У буквы {y} место в алфавите №: {b}')
print(f'Кол-во букв между {x} и {y}: {diff}')