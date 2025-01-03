n = int(input())

def pascal(num):
    s = [[j + 1 for j in range(i + 1)] for i in range(num + 1)]
    return s


print(pascal(n))
