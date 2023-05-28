# На вход программе подается натуральное число n, затем nn строк, затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
l = list([input() for _ in range(int(input()))])
l2 = list([input() for _ in range(int(input()))])

for i in l:
    for j in l2:
        if j.lower() not in i.lower():
            break
        else:
            print(i)
            break




