# На вход программе подается одна строка с буквами русского языка.
# Напишите программу, которая определяет количество гласных и согласных букв.

g, s, string = 0, 0, input()
for i in string:
    g += i in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
    s += i in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
print('Количество гласных букв равно', g)
print('Количество согласных букв равно', s)