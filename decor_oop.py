'''Задание 6 - А. Создай декоратор, который считает, сколько раз была вызвана обёрнутая функция.
'''

def call_counter(func):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        func(*args, **kwargs)
        counter += 1
        return f'Функция {func.__name__} была вызвана {counter} раз'
    return wrapper

@call_counter
def just_function(name):
    return name

print(just_function('Алихан'))
print(just_function('Айша'))
print(just_function('Айша'))
print(just_function('Айша'))

'''Создай декоратор @auth_required, который:
Запрашивает у пользователя логин и пароль перед вызовом функции.
Если введено правильно (admin, 1234) — функция выполняется.
Иначе — выводится “Доступ запрещён”.'''

def auth_required(func):
    def wrapper(*args, **kwargs):
        name, password = input('Введите имя: '), input('Введите пароль: ')
        if name == 'admin' and password == '1234':
            func(*args, **kwargs)
            return 'Доступ разрешен'
        else:
            return 'Доступ запрещен'
    return wrapper

@auth_required
def func():
    return 'Test function'
print(func())