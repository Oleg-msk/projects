#Да прибудет с нами сила!

print()
print('Программа проверяет, является ли число - числом Армстронга!')
n = int(input('Введите число: '))
x = n
l = len(str(n))
s = []
while n != 0:
    dig = n % 10
    s.append((dig) ** l)
    n = n // 10
if sum(s) == x:
    print(f'Число {x} - является числом Армстронга.')
else:
    print(f'Число {x} - не является числом Армстронга.')