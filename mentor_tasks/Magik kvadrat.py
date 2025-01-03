#Да прибудет с нами сила!

print()
print('Это программа определяет, является ли матрица магическим квадратом.')
print()
n = int(input('Введите количество строк и количество элементов в строке квадратной матрицы: '))
s = [[] for i in range(n)]
s_d = []
s_d2 = []
s_all = []
m =[]
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(int(input('Введите число: ')))
for i in range(n):
    s_d.append(m[i][i])
    s_d2.append(m[n - i - 1][i])
    for j in range(n):
        s[i].append(m[j][i])
    s_all.append(sum(m[i]))
    s_all.append(sum(s[i]))
s_all.append(sum(s_d))
s_all.append(sum(s_d2))
print()
print('Вывожу ответ:')
if len(set(s_all)) == 1:
    print('YES')
else:
    print('NO')
