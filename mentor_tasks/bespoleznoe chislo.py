# Да прибудет с нами сила!

import random

print()
print(f'Привет!', f'Я программа, которая умеет:', f'- Создавать числовую последовательность по заданному числу элементов;',
      f'- Находить максимальное число;', f'- Находить самое близкое число к максимальному, ' f'которое поделено на длину последовательности;', sep = '\n')
print()
s = []
n = int(input('Введите натуральное число от 10 до 50: '))
for i in range(n):
    s.append(random.randint(0.0, 1000.0))
cnt = max(s)
x = max(s) / len(s)
for i in s:
    d = abs(i - x)
    if d < cnt:
        cnt = d
        isk = i
print()
print(f'Сгенерированная числовая последовательность с {n} элементов:')
print(s)
print()
print(f'Максимальное число = {max(s)}')
print(f'Искомое число = {isk}')
