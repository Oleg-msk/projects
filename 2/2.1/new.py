a=int(input())
c=int(input())
b=input()
if b=='+' or b=='-' or b=='/' or b=='*':
    if c!=0:
        if b=='+':
            print(a+c)
        elif b=='-':
            print(a-c)
        elif b=='/':
            print(a/c)
        elif b=='*':
            print(a*c)
    else:
        print('На ноль делить нельзя')
else:
    print('ошибка')