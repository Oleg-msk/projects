# Да прибудет с нами сила!
from itertools import count

print()
print('Программа умеет раздвать яблоки ученикам!', 'И считать кому сколько осталось!', sep='\n')
n = int(input('Введите количество яблок: '))
k = int(input('Введите количество учеников: '))
s = [[] for i in range(k)]
if k !=0:
    if n !=0:
        if n >= k:
            while n != n % k:
                n -= k
                for j in range(k):
                    s[j].append(1)
            for j in range(n):
                s[j].append(1)

            x = [len(el) for el in s]
            for i in set(x):
                print(f'Количество учеников = {x.count(i)}, получили по количеству яблок = {i}')
        else:
            print(f'Количество учеников = {n}, получили по количеству яблок = 1')
            print(f'Количество учеников = {k - n}, получили по количеству яблок = 0')
    else:
        print('Яблок нет. Ученики остались без яблок.')
else:
    print('Учеников нет. Яблоки остались не тронуты.')