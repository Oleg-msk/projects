# 2. Создать калькулятор, который выполняет сложение, вычитание, умножение и сделение.

num_1 = float(input()) #Вводим первое число
num_2 = float(input()) #Вводим второе число
operator = input() #Вводим оператор
if operator == '+' or operator == '-' or operator == '/' or operator == '*':
    if num_2 != 0:
        if operator == '+':
            print (num_1 + num_2)
        elif operator == '-':
            print(num_1 - num_2)
        elif operator == '/':
            print(num_1 / num_2)
        elif operator == '*':
            print(num_1 * num_2)
    else:
        print('На ноль делить нельзя')
else:
    print('ошибка')