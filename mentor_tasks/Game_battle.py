import random
hp_dragon = random.randint(80, 100)
hp_knight = random.randint(40, 50)
power_dragon = random.randint(10, 14)
power_knight = random.randint(5, 7)


print()
print('Приветствую тебя в Долине смерти!')
print('Кто ты воин? Назови своё имя... ')
name = input(': ')
print(f'Слава тебе, {name}!!!', 'Мы благодарим Богов, за то что они послали тебя в помощь.',
      'Кровожадный Дракон похитил дочь короля...', 'Готов ли ты освободить принцессу из заточения Дракона?', 'Если готов, ответь: да',
      'Если страшно, ответь: нет', sep = '\n')

while True:
    print('И каков будет твой ответ?')
    otvet = input(':')
    if otvet.lower() == 'нет':
        print('Под слова песни М. Круга:', 'Что ж ты фраер сдал назад? =)))', f'Прилетел Дракокон и сожрал рыцаря!',
              f'Вот так бесчестно погиб воин {name}.', 'Конец!', sep='\n')
        break
    elif otvet.lower() == 'да':
        print('Спасибо, что согласился помочь!', 'Чтобы убить Дракона, тебе нужно оружие.',
              'Но мы не знаем какое оружие сильнее наносит урон и какая броня даёт больше уровень жизни.',
              'Только судьба определит силу удара и уровень жизни случайным образом.',
              'Также мы не знаем какой урон наносит Дракон и уровень его жизни.', 'Всё случится по воле Богов!!!', sep='\n')
        print()
        print('Боги определили исход битвы.', 'Предоставляем параметры для игры:',
              f'У Дракона уровень жизни: {hp_dragon}', f'У рыцаря {name} уровень жизни: {hp_knight}',
              f'У дракона урон: {power_dragon}', f'У рыцаря {name} урон: {power_knight}', sep='\n')

        for _ in range(2):
            print()
        print('Началась самая эпичная битва Долины смерти!')
        print()
        cnt = 0
        while True:
            if hp_dragon >= power_knight * 2:
                print(f'Раунд {cnt + 1}')
                hp_dragon = hp_dragon - power_knight * 2
                print(f'Рыцарь нанёс двойной удар силой: {power_knight * 2}...')
                print(f'У Дракона осталось жизней: {hp_dragon}')
                hp_knight = hp_knight - (power_dragon - (power_dragon - power_knight))
                print(f'Дракон нанёс удар силой: {power_dragon}...')
                print(f'Броня отразила часть урона. У рыцаря осталось жизней: {hp_knight}')
                cnt += 1
                print()

            else:
                print(f'Раунд {cnt + 2}')
                hp_dragon = hp_dragon - power_knight * 2
                print(f'Рыцарь нанёс двойной удар силой: {power_knight * 2}...')
                print(f'Дракон убит! Победил рыцарь за {cnt} раундов!')
                print()
                print(f'Спасибо тебе храбрый рыцарь {name}!', 'Ты убил Дракона!!!',
                      'Спас дочь короля и всю Долину смерти.',
                      'В награду король дарит тебе сундук с золотом и отдаёт принцессу в жёны!',
                      'Все счастливы и празднуют победу.',
                      'Конец!', sep='\n')
                break
        break
    else:
        print('Прошу не мучай Короля, ответь: да/нет')













