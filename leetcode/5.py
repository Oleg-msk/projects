# 5. Реализовать факториал числа с использованием цикла.

n = int(input()) #вводим число
cnt = 1 #создаём переменную счётчик
for i in range(1, n + 1): #создаём цикл
    cnt *= i #перезаписываем в переменную результат умножения каждой итерации
if n >= 0:
    print(cnt) #выводим результат
else:
    print('введено неверное значение')