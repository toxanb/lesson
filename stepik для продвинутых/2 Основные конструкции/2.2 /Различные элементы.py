# На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию.
# Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.
num = input().split(' ')
num2 = list()
print(len([num2.append(i) for i in num   if i not in num2]))
