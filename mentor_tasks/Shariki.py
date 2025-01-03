#да прибудет с нами сила!

print()
print('Программа умеет удалять больше двух соседей(шариков) в ряду!')
print('У нас 10 цветов у шариков, соответственно у каждого цвета своя цифра от 0 до 9.')
s = [int(input('Введите элемент/цвет шарика (цифра от 0 до 9): ')) for i in range(int(input('Введите количество элементов/шариков (число): ')))]
print(s)
x = len(s)
print(f'Длина списка = {len(s)}')
cnt = 0
while True:
    for i in range(1, len(s) - 2):
        if s[-i] == s[-i - 1] == s[-i - 2]:
            print(f'Удалены: {s[-i]}')
            while s[-i] == s[-i - 1]:
                del s[-i]
                cnt += 1
            del s[-i]
            print(s)
            print(len(s))
            break
    else:
        break

print('-' * 30)
print(f'Шариков было уничтожено: {x - len(s)}')

