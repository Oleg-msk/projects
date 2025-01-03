#Да прибудет с нами сила

print()
print('Программа находит все положительные делители некоторых целых чисел!')
def all_divisors(number):
    return [i for i in range(2, number + 1, 2) if number % i == 0]
print(all_divisors(int(input('Введите целое число: '))))
