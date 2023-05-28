# Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21


#1
# n = int(input())
# k = 1
# for i in range(1, n+1):
#     for j in range(k,k+i):
#         print(j, end='')
#     k = k + i
#     print()


#2
# n = int(input())
# t = 0
# for i in range(n):
#     for _ in range(i):
#         t +=1
#         print(t, end = ' ')
#     print()


