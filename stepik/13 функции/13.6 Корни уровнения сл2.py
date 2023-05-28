# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения
#  ax**2+bx+c=0 и возвращает его корни в порядке возрастания
from math import sqrt
def solve(a, b, c):
    d = (b ** 2) - 4 * a * c # Дескриминант
    if d > 0:
        x1 = (-b + sqrt(d))/ (2 * a)
        x2 = (-b - sqrt(d))/ (2 * a)
    elif d == 0:
        x1 = -b  / (2 * a)
        x2 = x1
    if x1 > x2:
        x1 , x2 = x2, x1
    return x1 , x2

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)