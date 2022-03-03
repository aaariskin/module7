print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
#
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
last = 0
total_months = 10
count_rise = 0
count_down = 0

for month in range(total_months):
	salary = int(input('Введите доход за ' + str(month + 1) + ' месяц: '))
	if last > salary:
		count_down += 1
	elif last < salary:
		count_rise += 1
	last = salary
print('Отчет')
print('Повышений', count_rise, 'за', total_months, 'периодов.')
print('Понижений', count_down, 'за', total_months, 'периодов.')
print('Без изменений', total_months - (count_rise + count_down))
