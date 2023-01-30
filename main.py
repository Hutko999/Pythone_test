Operation = input(('Выберите операцию: '))
a = int(input('Введите первое число a: '))
b = int(input('Введите первое число b: '))

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


