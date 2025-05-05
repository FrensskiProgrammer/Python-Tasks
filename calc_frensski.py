'''Задание 5 - А:
Создай калькулятор:
Запрашивает два числа и операцию (+, -, *, /).
Выполняет операцию.
Обрабатывает деление на ноль, ввод нечисел, неверные операции через try-except.'''

try:
    x, y = [int(input('Число: ')) for _ in range(2)]
    operation = input('Какую из операций выполнить(+,-,*, /): ')

    if operation == "+":
        print(x+y)
    elif operation == "-":
        print(x-y)
    elif operation == "*":
        print(x*y)
    elif operation == "/":
        print(x / y)
    else:
        print('Неверная операция')
except (ZeroDivisionError, TypeError, ValueError):
    print('Неверная операция')

'''Задание 5 - Б. Создай скрипт, который:
Открывает файл по имени, введённому пользователем.
Если файл не найден — сообщает об ошибке.
Если формат содержимого не читаемый (json, csv и т.д.) — сообщает об ошибке.
'''

filename = input('Название файла: ')

try:
    open(filename)
    if not filename.endswith('.txt'):
        raise ValueError('Нечитаемый тип файла')
    else:
        print('Открытие файла прошло успешно')
except FileNotFoundError:
    print('Такого файла не существует')