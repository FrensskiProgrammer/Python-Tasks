'''Задача 3 - A:
Прочитать файл.
Посчитать общую стоимость всех товаров.
Найти товар с максимальной ценой.'''

import json

prices = 0
product, max_price = '', 0
with open('products.json') as file:
    obj = json.load(file)
    keys = [i for i in obj]
    for line in keys:
        result = obj[line]
        for key in result:
            name, price = key.get('name'), key.get('price')
            print(f'Имя товара: {name}\nСтоимость товара: {price}')
            prices += int(price)
            if int(price) >= max_price:
                max_price = int(price)
                product = name

print(f'Общая стоимость всех товаров: {prices}')
print(f'Товар с самой высокой стоимость: {product}')


'''Задание 3 - Б (запись):
Напиши программу, которая:
Запрашивает у пользователя название и цену нового товара.
Добавляет этот товар в products.json.
Если файла нет — создаёт его с нужной структурой.'''

name = input('Наименование товара: ')
price = int(input('Стоимость товара: '))

result = {'name': name, 'price': price}

with open('products_2.json', 'a', encoding='UTF-8') as file:
    obj = json.dump(result, file, ensure_ascii=False)
