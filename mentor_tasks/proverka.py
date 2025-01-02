#v = [int(el) for el in input().split()]
#u = [int(el) for el in input().split()]
#print(*[v[i] * u[i] for i in range(len(v))])
#print(sum([v[i] * u[i] for i in range(len(v))]))



print(sum([float(input()) > 37 for i in range(int(input('Введите количество людей: ')))]))