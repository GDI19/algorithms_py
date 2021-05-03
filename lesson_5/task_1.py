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
profit_comp = []
loss_comp = []

for i in range(1, count+1):
    comp_name = input('Название: ')
    profit_1 = int(input('Какая прибыль в 1 квартале: '))
    profit_2 = int(input('Какая прибыль в 2 квартале: '))
    profit_3 = int(input('Какая прибыль в 3 квартале: '))
    profit_4 = int(input('Какая прибыль в 4 квартале: '))
    profit_avrg = (profit_1 + profit_2 + profit_3 + profit_4)/4
    total_avrg += profit_avrg

    co_dict[comp_name] = [ profit_1, profit_2, profit_3, profit_4, profit_avrg]
    print()

avrg = total_avrg / count
for k in co_dict.keys():
    if co_dict[k][4] > avrg:
        profit_comp.append(k)
    else:
        loss_comp.append(k)

print(f'Средняя прибыль компаний: {avrg}')
print('Компании с прибылью выше средней:', ', '.join(profit_comp))
print(f'Компании с прибылью ниже средней:', ', '.join(loss_comp))
