# Valentin 1 September 2017
# Решение квадратных уравнений

import math

while True:
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    c = float(input('Введите c: '))

    #total = str(a) + "x^2" + str(b) + "x" + str(c)
    #print("Итоговый вид уравнения: ", total)

    d = b ** 2 - 4 * a * c
    print("\nВычисляем дискриминант...")
    print("Дискриминант равняется", d)

    if d == 0:
        print("\nДискриминант равен 0")
        print("x =", -b/(2*a))
    elif d < 0:
        print("\nДискриминант меньше 0, решений нет")
    else:
        sqrtd = math.sqrt(d)
        print("\nКорень из дискриминанта равен ", sqrtd)
        x1 = (-b - math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        print("\nВычисляем корни...")

        print("\nПервый корень равен", x1)
        print("Второй корень равен", x2)

    while True:

        print("\nХотите решить ещё одно уравнение?")
        answer = input('Y/n(help - справка по командам) ')

        if answer == 'Y':
            break
        elif answer == 'n':
            exit()
        elif answer == 'help':
            print(open('help.txt', 'r').read())
        else:
            print("\nВведите Y или n (help - справка по командам)")