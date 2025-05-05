'''Задание 7 - А:
Создай генератор, который:
Проходит по строке и возвращает только гласные буквы.
Пример: "Python is awesome" → o, i, a, e, o, e.'''

# words = ('a', 'e', 'i', 'o')
#
# def generator_word(text):
#     for i in text:
#         if i in words:
#             yield i
#
# for i in generator_word('Python is awesome'):
#     print(i)

'''Задание 7 - Б:
Напиши генератор, который:
Возвращает числа Фибоначчи до N-го элемента.
Пример: fib_gen(5) → 0, 1, 1, 2, 3'''

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_generator(10):
    print(num)


