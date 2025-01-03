# Да прибудет снами сила!

z = input('Введите значение: ')
u = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [i for i in z]
k = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
h = u[-int(y[1]) - 1]
g = int(k.get(z[0])) - 1
print(h)
print(g)

n = 8
matrix = [['.' for j in range(n)] for i in range(n)]

for i in range(n):
    matrix[h][i] = '*'
    matrix[i][g] = '*'

    matrix[i + abs(h - 2)][i] = '*'
for i in range(n - 1):
    matrix[i][n - (h - 2) - i] = '*'

matrix[h][g] = 'Q'
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end='  ')
    print()
