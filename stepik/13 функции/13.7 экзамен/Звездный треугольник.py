# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой равными  15 и 8 соответственно:

def draw_triangle():
    star = '*'
    for i in range(0, 8):
        print((' '* (8-i-1) ) + '*' * (1 + i * 2))





# основная программа
draw_triangle()  # вызов функции