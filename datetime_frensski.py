'''Задание 1 - A:
Напиши программу, которая:
Запрашивает у пользователя дату его рождения в формате ГГГГ-ММ-ДД.
Выводит:
Сколько ему лет на текущий момент.
Сколько дней осталось до следующего дня рождения.'''


from datetime import datetime, timedelta, time, date

data = input('Ваш год рождения в (формате ГГГГ-ММ-ДД): ')
data = datetime.strptime(data, '%Y-%m-%d')
now_year = datetime.now()
years_old = int(now_year.strftime('%Y')) - int(data.strftime('%Y'))
if int(now_year.strftime('%m')) <= int(data.strftime('%m')) and int(now_year.strftime('%d') <= data.strftime('%d')):
    years_old = years_old - 1

if int(data.strftime('%m')) < int(now_year.strftime('%m')):
    result_days = datetime(year=int(now_year.strftime('%Y'))+1, month=int(data.strftime('%m')),
                           day=int(data.strftime('%d'))) - now_year
else:
    result_days = datetime(year=int(now_year.strftime('%Y')), month=int(data.strftime('%m')),
                           day=int(data.strftime('%d'))) - now_year
print(f'Ваш текущий возраст: {years_old} лет\nДо вашего дня рождения осталось: {result_days.days} дней')

'''Задание 1 - Б:
Симуляция расписания автобусов:
Программа должна выводить расписание автобуса каждые 15 минут, начиная с 06:00 до 23:00.
Для каждого времени нужно:
Вывести текущее время отправления.'''

hours_one = timedelta(hours=6, minutes=0, seconds=0)

while int(str(hours_one).split(':')[0]) != 23:
    now_datetime = datetime.now()
    now_time = now_datetime.strftime('%H:%M:%S')
    hours_one += timedelta(minutes=15)
    print(f'Текущее время отправления: {hours_one}')



