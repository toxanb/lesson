# Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк.
# Пустую строку вместо первой строки ввода выводить не надо.
l = []
n = int(input().strip('#'))
for _ in range(n):
    s = input()
    if '#' in s:
        h = s.index('#')
        l.append(s[:h].strip())
    elif '#' not in s:
        l.append(s)
print(s)