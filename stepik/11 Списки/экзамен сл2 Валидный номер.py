# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером если она имеет формат:
# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
# 7-301-447-5820 YES
# 301-4477-5820 NO
s = '77-301-447-5820'.split('-')
s2 = ['8' , '77']
flag = 'YES'
for i in s:
    if  s[0] in s2:
        flag = 'NO'
        break
    if len(s)> 1 and len(s[1]) == 3  :
        if i.isdigit() or  s[0] == '7'   and i.isdigit():
            flag  = 'YES'
        else:
            flag = 'NO'
            break
    else:
        flag = 'NO'
print(flag)
print(len(s[0]))

