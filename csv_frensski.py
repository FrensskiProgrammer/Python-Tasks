from csv import DictReader, DictWriter

'''Задача 2 - A:
Прочитать данные с помощью модуля csv.
Найти средний балл студентов и вывести имя студента с наивысшим баллом.'''

counter = 0
scores = 0
student, max_score = '', 0
with open('students.csv') as file:
    obj = DictReader(file, delimiter=',')
    for line in obj:
        counter += 1
        name, age, score = line['name'], line['age'], line['score']
        print(f'Имя: {name}\nВозвраст: {age}\nБаллы: {score}\n')
        scores += int(line['score'])

        if int(score) >= max_score:
            max_score = int(score)
            student = name

middle_score = scores / counter

print(f'Средний балл всех учеников: {round(middle_score, 2)}')
print(f'Имя студента с наивысшим баллом: {student}')

'''Задание 2 - Б (запись):
Создай программу, которая:
Запрашивает у пользователя имя, возраст и оценку.
Добавляет эту информацию в файл students.csv в формате CSV.
Если файла нет — создай и добавь заголовки.
'''

name = input('Имя: ')
age = int(input('Возраст: '))
score = int(input('Оценка: '))

columns = ['name', 'age', 'score']

with open('students_2.csv', 'a', encoding='UTF-8', newline="") as file:
    obj = DictWriter(file, fieldnames=columns, delimiter=',')
    obj.writeheader()
    obj.writerow({'name': name, 'age': age, 'score': scores})

