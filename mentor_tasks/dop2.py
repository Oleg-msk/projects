num=int(input())
a=num//100
b=(num//10)%10
c=num%10
if a+1==b==c-1:
    print('True')
else:
    print('False')