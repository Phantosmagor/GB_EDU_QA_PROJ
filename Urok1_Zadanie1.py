"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

txt1 = "Это - переменная формата Str (String)"
int1 = 15 #"Это - перменная формата Int (Ingeter)"
Float1 = 36.12 #"Это - переменная формата Float"
Bool1 = True  #"Это переменная формата Bool(Boolean)"
print(f"txt1 - {txt1} и её значение\nint1 - Это - перменная формата Int (Ingeter) и её значение:"
      f" {int1}\nFloat1 - Это - перменная формата Int (Float) и её значение: {Float1}\n"
      f"Bool1 - Это - перменная формата Int (Bool) и её значение: {Bool1}\n")

yourname = input('Придумайте имя учётной записи и введите его:')
youremail = input('введите Ваш адрес электронной почты:')
yourpwd = input('Придумайте и введите пароль для учётной записи:')
yourage = int(input('Пожалуйста, укажите Ваш возраст: '))
print(f"Ваши данные для входа , проверьте правильность и"
      f"запомните их:\n Имя учётной записи: {yourname}\n Ваша электронная почта: "
      f"{youremail} \n "
      f"Ваш пароль: {yourpwd}\n Ваш возраст: {yourage}")
