"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
timeinput = int(input('Пожалуйста, введите время в секундах: '))
print(f"Приведенное время в формате чч:мм:сс \n"
      f"{timeinput/3600} : {timeinput/60} : {timeinput}")