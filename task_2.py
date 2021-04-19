num = input('Введите число для подсчета четных и не четных цифр: ')

odd = 0
even = 0

if int(num) > 0:
    for d in num:
        if int(d) % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'В числе {num}: \n- четных цифр {even} \n- не четных цифр {odd}')