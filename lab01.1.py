import math
from math import cosh, log

a = int(input('Enter a: '))
x = int(input('Enter x: '))

G = 10 * (10 * a ** 2 + 11 * a * x - 25 * x ** 2)/(- a ** 2 + a * x + 6 * x ** 2)

print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, G))

a = float(input('Enter a: '))
x = float(input('Enter x: '))

F = cosh(21 * a ** 2 - 34 * a * x + 9 * x ** 2)

print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, F))

a = int (input('Enter a: '))
x = int (input('Enter x: '))

Y = log(3 * a ** 2 - 25 * a * x + 8 * x ** 2 + 1)/log(10)

print('A={0}, X={1}, Result: {2:.6f}'.format(a, x, Y))
