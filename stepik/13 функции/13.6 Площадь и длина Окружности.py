# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения:
# длину окружности и площадь круга, ограниченного данной окружностью.
# объявление функции
# C = 2PR длинна окружности
# S = PR**2
from math import pi
def get_circle(radius):
    return 2*pi*radius, pi*radius**2

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)