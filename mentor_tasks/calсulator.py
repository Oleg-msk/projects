from poetry.core.packages.utils.utils import is_url
result = []
def is_valid(num):
    if num.isdigit():
        return True
    else:
        return False

print()
print('Добро пожаловать в калькулятор =)')
print()
print('Программа в разработке, но уже умеет следующее:', '- Сложение', '- Вычитание', '- Умножение', '- Деление',
      sep = '\n')
print()
while True:
    a = input('Введите значение: ')
    if is_valid(a) == False:
        print('Введено неверное значение: ')
    else:
        result.append(a)
        break
while True:
    operator = input('Введите знак: ')
    if operator != '=':
        if operator != "/":
            if operator != "+" and operator != "-" and operator != "*":
                print('Введён неверный знак. Введите: "+", "-", "*", "/"')
            else:
                result.append(operator)
                while True:
                    b = input('Введите значение: ')
                    if is_valid(b) == False:
                        print('Введено неверное значение: ')
                    else:
                        result.append(b)
                        break
        else:
            result.append(operator)
            while True:
                b = input('Введите значение: ')
                if int(b) != 0:
                    if is_valid(b) == False:
                        print('Введено неверное значение: ')
                    else:
                        result.append(b)
                        break
                else:
                    print('На ноль делить нельзя!!!')
    else:
        break
print()
print(f'Ответ равен: ', eval(' '.join(result)))
print('Спасибо! Обращайтесь ешё!')