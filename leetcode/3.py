# 3. Написать функцию, которая определяет, является ли число четным.

num = float(input()) #введите число
if num % 2 == 0: #определяем остаток от числа при делении на 2
    print('Число чётное') #выводим результат в соответствии с условием
else:
    print('Число нечётное')