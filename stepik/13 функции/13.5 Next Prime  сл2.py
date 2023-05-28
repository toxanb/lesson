# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.
def get_next_prime(num):

    while True:
        num += 1
        if len([i for i in range(1, num +1) if num % i == 0]) == 2:
            break
    return num

n = int(input())
print(get_next_prime(n))