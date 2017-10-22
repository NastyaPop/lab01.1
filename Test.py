import math
from math import cosh, log

k = input('Если хотите вычислить G нажмите 1, если хотите вычислить F нажмите 2, если хотите вычислить Y нажмите 3\n')

if k == '1':
    a = int(input('Enter a: '))
    x = int(input('Enter x: '))
    d = - a ** 2 + a * x + 6 * x ** 2
    if d != 0:
        G = 10 * (10 * a ** 2 + 11 * a * x - 25 * x ** 2)/(- a ** 2 + a * x + 6 * x ** 2)
        print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, G))
    else: print('Введите другие значения для x и a')

elif k == '2':
    a = float(input('Enter a: '))
    x = float(input('Enter x: '))
    F = cosh(21 * a ** 2 - 34 * a * x + 9 * x ** 2)
    print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, F))
elif k == '3':
    a = int (input('Enter a: '))
    x = int (input('Enter x: '))
    Y = log(3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1)/log(10)
    print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, Y))
else: print('Вы ввели неправильное значение')