first = int(input('Введите ваше чило: '))
second = int(input('Введите ваше чило: '))
thrid = int(input('Введите ваше чило: '))

if first == second and second == thrid and first == thrid:
     print(3)
elif first == second or second == thrid or first == thrid:
     print(2)
else:
    print(0)