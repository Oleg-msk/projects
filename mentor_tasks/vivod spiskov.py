#Да прибудет с нами сила!

print()
print('Программа умееет выводить списки всех возможных комбинаций элементов введенной строки!')
s = input('Введите элементы строки через пробел: ').split(' ')
s_all = [[] for i in range(len(s))]
s_all.append(s)
s_all.append([])
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] != s[j]:
            s_all[i].append(s[j])
for i in range(len(s)):
    s_all.append(s[i].split())
print()
print('Вывожу список комбинаций списков: ')
print(s_all)







