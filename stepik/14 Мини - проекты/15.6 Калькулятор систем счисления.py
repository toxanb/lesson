# На вход программе подается натуральное число в десятичной системе счисления.
# Напишите программу, которая переводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.
def calculate(n):
    binary = bin(num)
    octal = oct(num)
    h = hex(num)
    print(binary[2:])
    print(octal[2:])
    print(h[2:].upper())


num = int(input('Введите число : '))
calculate(num)
