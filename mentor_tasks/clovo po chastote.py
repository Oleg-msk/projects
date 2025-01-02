#Да прибудет с нами сила!
print()

import collections
from statistics import multimode
from collections import Counter

from tomlkit import key_value

s = ('Давно выяснено,  что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. '
               'Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, '
               'а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации '
               '"Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы '
               'HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" '
               'сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы '
               'текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно '
               '(например, юмористические варианты).')


s = s.replace('.', '')
s = s.replace(',', '')
s = s.replace('-', '')
s = s.replace('!', '')
s = s.replace('?', '')
s = s.replace('"', '')
s = s.replace('(', '')
s = s.replace(')', '')
s = s.replace('  ', ' ')
s = s.split(' ')

n = ''
for i in s:
    if len(i) > len(n):
        n = i

print(n)
print(*multimode(s))
print('-' * 50)


z=[]
q = set([len(i) for i in s])

for key in collections.Counter(s):
    for i in range(len(q)): # видимо задаю неправильный диапозон
        if collections.Counter(s)[key] == 5: # вот тут не могу сделать перебор переменных
            z.append(key)
            #print(i)
            #print(key)
print(z)


print()
print(set(collections.Counter(s)[key] for key in collections.Counter(s)))
q = set([len(i) for i in s])
print(q)



