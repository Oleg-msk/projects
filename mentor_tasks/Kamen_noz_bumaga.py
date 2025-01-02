# Да прибудет с нами сила!
import random

s = ['камень', 'ножницы', 'бумага']

def is_game(x, y):
    otvet = 0
    if x == y == 'камень' or x == y == 'ножницы' or x == y == 'бумага':
        otvet = 1
        return otvet
    if x == 'камень' and y == 'ножницы' or x == 'ножницы' and y == 'бумага' or x == 'бумага' and y == 'камень':
        otvet = 2
        return otvet
    if x == 'камень' and y == 'бумага' or x == 'ножницы' and y == 'камень' or x == 'бумага' and y == 'ножницы':
        otvet = 3
        return otvet

print()
print()

print('Приветствую в игре!')

while True:
    print()
    print('Если хочешь сыграть, нажми "y": ')
    print('Если не хочешь играть, введи нажми любую кнопку: ')
    x = input()
    cnt_1 = 0
    cnt_2 = 0
    if x.lower() == 'y' or x.lower() == 'н':
        print('До сколька побед играем?')
        while True:
            n = input('Введите целое число: ')
            if n.isdigit():
                print('Отлично! Поехали...')
                for i in range(int(n)):
                    print()
                    print(f'Раунд {i + 1}:')
                    random.shuffle(s)
                    x_1 = random.choice(s)
                    print(f'У игрока 1 выпало значение: {x_1}')
                    #random.shuffle(s)
                    y_2 = random.choice(s)
                    print(f'У игрока 2 выпало значение: {y_2}')
                    z = is_game(x_1, y_2)
                    if z == 1:
                        cnt_1 += 1
                        cnt_2 += 1
                        print(f'Каждый игрок получил по одному баллу')
                    elif z == 2:
                        cnt_1 += 1
                        print(f'Балл достаётся игроку 1')
                    elif z == 3:
                        cnt_2 += 1
                        print(f'Балл достаётся игроку 2')
                    print()
                    input('Для продолжения нажмите любую клавишу...')
                if cnt_1 == cnt_2:
                    print()
                    print(f'Ничья! Возможно, надо сыграть ещё раз!')
                    break
                elif cnt_1 > cnt_2:
                    print()
                    print(f'Победил игрок 1. Поздравляем!')
                    break
                else:
                    print()
                    print(f'Победил игрок 2. Поздравляем!')
                    break
            else:
                print('Введено неверное значение!')

    else:
        break

print()
print('Спасибо за игру!', 'Возвращайся в следующий раз!', sep = '\n')