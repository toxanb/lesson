# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

#1 Решение
# l = []
# n = 1
# s = ''
# for i in range(97,123):
#     s = chr(i)*n
#     l.append(s)
#     n +=1
# print(l)


#2 Решение
# print(list([chr(96 + i) * i for i in range(1, 27)]))
