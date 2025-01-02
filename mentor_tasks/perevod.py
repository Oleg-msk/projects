#spisok = ['байт', 'килобайт', 'мегабайт', 'гигабайт', 'терабайт', 'петабайт']
spisok = ['б', 'Кб', 'Мб', 'Гб', 'Тб', 'Пб']
print()
print(f'Вас приветствует конвертер "Байтик"!', )
print(f'Я умею переводить значения от байта до петобайта и обратно.')
print()
while True:
    print('Введите число: ')
    n = input()
    if n.isdigit():
        while True:
            print()
            chto = input('Введите, что хотите перевести (б, Кб, Мб, Гб, Тб, Пб): ')
            if chto in 'б, Кб, Мб, Гб, Тб, Пб':
                for c in spisok:
                    if c == chto:
                        x = spisok.index(c)
                        while True:
                            print()
                            vo_ctho = input('Введите, во что хотите перевести (б, Кб, Мб, Гб, Тб, Пб): ')
                            if vo_ctho in 'б, Кб, Мб, Гб, Тб, Пб':
                                for c in spisok:
                                    if c == vo_ctho:
                                        y = spisok.index(c)
                                        print()
                                        if x > y:
                                            print(f'{n} {chto} = {float(n) * (2 ** (10 * abs(x - y)))} {vo_ctho}')
                                            break
                                        else:
                                            print(f'{n} {spisok[x]} = {float(n) / (2 ** (10 * abs(x - y)))} {spisok[y]}')
                                            break
                                break

                            else:
                                print('Введено неверное значение!')
                break
            else:
                print('Введено неверное значение!')
        break
    else:
        print('Введено неверное значение!')
