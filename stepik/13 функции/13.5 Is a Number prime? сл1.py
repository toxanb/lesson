# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число
# и возвращает значение True если число является простым и False в противном случае.

def is_prime(num):
    #1
    # flag = False
    # count = 0
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         count +=1
    # if count == 2:
    #     flag = True
    # return flag

    #2
    return len([i for i in range(1,num+1) if num%i ==0] )==2
n = int(input())


print(is_prime(n))