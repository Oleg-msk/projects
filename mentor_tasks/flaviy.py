n = int(input('Введите количество участников: '))
k = int(input('Введите шаг выбывания участиков: '))
s = [int(i) for i in range(1, n + 1)]
s_del = []
print(s)
cnt = 3
while len(s) != n :
    for i in range(len(s)):
        if s[i] % k == 0:
            s_del.append(s[i])
    for j in
print(s_del)