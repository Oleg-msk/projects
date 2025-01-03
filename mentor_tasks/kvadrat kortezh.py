# Да прибудет с нами сила!

print()
print('Эта программа умеет вычислять:',
      'Периметр, Площадь и диагональ квадрата и возвращать значения в кортеже.', sep='\n')
n = int(input('Введите сторону квадрата: '))
def square(num):
    x = []
    p = num * 4
    x.append(p)
    s = num * num
    x.append(s)
    d = ((num ** 2) + (num ** 2)) ** 0.5
    x.append(d)
    return tuple(x)
print('Вывожу результат:')
print(square(n))
