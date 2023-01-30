
a = int(input('Введите первое число a: '))
b = int(input('Введите первое число b: '))
Operation = input(('Выберите операцию: '))

if Operation == '+':
    print('{} + {}  '.format(a, b))
    print("Ответ:", a + b)

elif Operation == '-':
    print('{} - {}  '.format(a, b))
    print("Ответ:", a - b)

elif Operation == '*':
    print('{} * {} '.format(a, b))
    print("Ответ:",a * b)

elif Operation == '/':
    print('{} / {}  '.format(a, b))
    print("Ответ:", a / b)


