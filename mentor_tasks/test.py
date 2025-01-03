#Да прибудет с нами сила!
from operator import index

#n = int(input())
#print(*[[i for i in range(1, n + 1)] for i in range(n)], sep='\n')

#print(*[[j for j in range(1, i + 2)] for i in range(int(input()))], sep='\n')

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
matrix[h][g] = 'Q'
for i in range(n):
    if i == h:
        matrix[i][j] = 1
for i in range(n):
    for j in range(n):
        print(*matrix[i][j], end='  ')
    print()