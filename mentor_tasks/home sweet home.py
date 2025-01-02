for _ in range(2):
    print()
n = 101
m = 20
for i in range(10, m):
    if i == 10 or i == m - 1:
        print(' ' * ((m - i) + 8), '* ' * ((i + 1) + 3)) # krusha
    else:
        print(' ' * ((m - i) + 8), '* ', ' ' * (13 + i), '*' )

for i in range(1, 10):
    if i == 3 or i == 7:
        print(' ' * 11, '*', ' ' * 9, '* ' * 9, ' ' * 8, '*') # verh i niz okon
    elif i == 5:
        print(' ' * 11, '*', ' ' * 9, '*', ' ' * 5, '* ' * 5, ' ' * 5, ' ' * 2, '*') # seredina okna
    elif i == 4 or i == 6:
        print(' ' * 11, '*', ' ' * 9, '*', ' ' * 5, '*', ' ' * 5, '*', ' ' * 9, '*')
    else:
        print(' ' * 11, '*', ' ' * 37, '*') # steny okna

for i in range(2):
    print('* ' * n) # fundament