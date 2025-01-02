from math import log2
from math import ceil
import random
x = random.randint(1, 10)

def is_valid(n):
    if n.isdigit() and 1 < int(n) <= 10 and int(n) % 1 == 0:
        return True
    else:
        return False

def is_sravnenie(k):
    if k == x:
        return True
    else:
        return False


print('Добро пожаловать в числовую угадайку!')
print('У вас есть пять попыток для победы!')

while True:
    print('Введите целое число от 1 до 10: ')
    num = input()
    if (is_valid(num)) == False:
        print('А может быть все-таки введем целое число от 1 до 10?')
    if (is_valid(num)) == True:
        for i in range(3):
            if print(is_sravnenie(num)) == False:
                continue
            else:
                break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')