# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text
# и возвращает значение True если указанный текст является палиндромом и False в противном случае.
def is_palindrome(text):
    s = ''
    for i in text:
        if i in ' !?.,-':
            continue
        else:
            s += i.lower()
    return s == s[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))