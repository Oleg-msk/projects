# да прибудет с нами сила!

print()
print('Это программа для проверки списка чисел на простое число!')
print('*примичание: 1 относится к простым числам!')
print()
num = int(input('Введите количество чисел: '))
s = [int(input('Введите число: ')) for i in range(num)]
result = []

def is_pr(n):
    cnt = 0
    if n == 0:
         return False
    for j in range(1, n + 1):
        if n % j == 0:
            cnt +=1
            if cnt >= 3:
                return False
                break
    return True
for i in s:
    if is_pr(i) == True:
        result.append(True)
    else:
        result.append((False))
#print(s)
#print(result)
print()
for i in range(len(s)):
    print(f'{s[i]}: {result[i]}')