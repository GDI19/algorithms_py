""""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия.
Программа должна определить
среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
2
рога
4
4
4
4
копыта
6
6
6
6
средняя прибыль 20
прибыльная копыта
убыточная рога
"""
count = int(input('Сколько компаний: '))

total_avrg = 0
co_dict = {}
profit_comp = ['name']
biggest_prof_avr = float('-inf')
loss_comp = ['Нет']
loss_avrg = float('inf')

for i in range(1, count+1):
    comp_name = input('Название: ')
    profit_1 = int(input('Какая прибыль в 1 квартале: '))
    profit_2 = int(input('Какая прибыль в 2 квартале: '))
    profit_3 = int(input('Какая прибыль в 3 квартале: '))
    profit_4 = int(input('Какая прибыль в 4 квартале: '))
    profit_avrg = (profit_1 + profit_2 + profit_3 + profit_4)/4
    total_avrg += profit_avrg

    co_dict[i] = [comp_name, profit_1, profit_2, profit_3, profit_4, profit_avrg]

    if profit_avrg > biggest_prof_avr:
        profit_comp[0] = co_dict[i][0]
        biggest_prof_avr = profit_avrg
    if count > 1:
        if profit_avrg < loss_avrg:
            loss_comp[0] = co_dict[i][0]
            loss_avrg = profit_avrg
    print(profit_comp, loss_comp)

# avrg = total_avrg / count
print(f'Средняя прибыль от компаний: {total_avrg}')

print(f'Самая прибыльная компания: {profit_comp[0]}')
print(f'Самая убыточная компания: {loss_comp[0]}')