print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

total_students = int(input('Количество учеников в классе? '))
grade_3 = grade_4 = grade_5 = 0

for student in range(total_students):
	grade = int(input('Оценка ученика №' + str(student + 1) + ': '))

	if grade == 5:
		grade_5 += 1
	elif grade == 4:
		grade_4 += 1
	elif grade == 3:
		grade_3 += 1

if grade_5 > grade_4 and grade_5 > grade_3:
	print('Сегодня больше отличников, ', grade_5)
elif grade_5 < grade_4 and grade_4 > grade_3:
	print('Сегодня больше хорошистов, ', grade_4)
elif grade_5 < grade_3 and grade_3 > grade_4:
	print('Сегодня больше троечников, ', grade_3)
elif grade_5 == grade_4 and grade_5 == grade_3 and grade_5 == grade_3:
	print('Сегодня всех одинаково, ', grade_5)
elif grade_5 == grade_4:
	print('Отличников и хорошистов больше, по ', grade_5)
elif grade_5 == grade_3:
	print('Отличников и троечников больше, по ', grade_5)
else:
	print('Хорошистов и троечников больше, по ', grade_4)
