'''Задача 8 - A. Дана строка с текстом:
text = "Мой email: test.email@mail.com, второй: work_2023@company.ru"
Задача:
Найти все email-адреса в строке.'''

text = 'Мой email: test.email@mail.com, второй: work_2023@company.ru'

import re

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.findall(pattern, text)
print(f'Почты: {result}')

'''Задание 8 - Б:
Создай скрипт, который:
Запрашивает у пользователя строку.
Проверяет, является ли она валидным номером телефона:
Формат: +7-XXX-XXX-XX-XX
Только цифры и дефисы.
Если формат неверный — выдаёт ошибку.'''

number = input('Введите номер: ')

pattern = r'\+7-\d{1,3}-\d{1,3}-\d{1,2}-\d{1,2}'

result = bool(re.fullmatch(pattern, number))
if result:
    print('Номер введен верно!')
else:
    print('Номер введен неверно!')