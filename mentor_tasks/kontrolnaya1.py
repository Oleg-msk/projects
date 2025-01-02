a = input('Введите значение:')

if a.isalpha():
    a = int(input('Введите только числа:'))
    operator = input('Введите оператор:')
    if operator == '+' or operator == '-' or operator == '/' or operator == '*':
        b = input('Введите значение:')
        if b.isalpha():
            b = int(input('Введите только числа:'))
            if operator == '+':
                print(a + b)
            elif operator == '-':
                print(a - b)
            elif operator == '/':
                print(a / b)
            elif operator == '*':
                print(a * b)
        else:
            b = int(b)
            if operator == '+':
                print(a + b)
            elif operator == '-':
                print(a - b)
            elif operator == '/':
                print(a / b)
            elif operator == '*':
                print(a * b)

    else:
        operator = input('Введите верный оператор:')

else:
    a = int(a)
    operator = input('Введите оператор:')
    if operator == '+' or operator == '-' or operator == '/' or operator == '*':
        b = input('Введите значение:')
        if b.isalpha():
            b = int(input('Введите только числа:'))
            if operator == '+':
                print(a + b)
            elif operator == '-':
                print(a - b)
            elif operator == '/':
                print(a / b)
            elif operator == '*':
                print(a * b)
        else:
            b = int()
            if operator == '+':
                print(a + b)
            elif operator == '-':
                print(a - b)
            elif operator == '/':
                print(a / b)
            elif operator == '*':
                print(a * b)

