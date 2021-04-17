
num = int(input('Введите 3-х значное число от 100 до 1000: '))

a = num // 100
b = num % 100 // 10
c = num % 100 % 10
print(a+b+c)
print(a*b*c)