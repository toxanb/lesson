# На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.
print( *[int(i) for i in input().split() if i.isdigit()],sep = '')


