# Подключите модуль random;
# Создайте строковые константы:
# digits: 0123456789;
# lowercase_letters: abcdefghijklmnopqrstuvwxyz;
# uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
# punctuation: !#$%&*+-=?@^_.
# Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле
import random
digits = '0123456789'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
amb = 'il1Lo0O'

chars = ''

# Программа должна запрашивать у пользователя следующую информацию:
#
# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?

countpasswords = int(input('Количество паролей ? : '))
lenght = int(input('Длинна пароля : '))

num = input('Включать ли цифры  ? y - да : ').strip()
low = input('Включать буквы верхнего регистра ? y - да : ').strip()
upp = input('Включать буквы нижнего регистра ? y - да : ').strip()
char = input('Включать символы? y - да : ').strip()
a = input('Исключать неоднозначные символы il1Lo0O y - да : ? ').strip()

# На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут быть в генерируемом пароле.

if num == 'y'.lower():
    chars += digits
if low == 'y'.lower():
    chars += lowercase
if upp == 'y'.lower():
    chars += uppercase
if char == 'y'.lower():
    chars += punctuation
if a == 'y':
    for i in 'il1Lo0O':
      chars = chars.replace(i,'')

# Напишите функцию generate_password(), которая принимает два аргумента:
# length: длину пароля;
# chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
def generate_password(lenght, chars):
    password = ''
    for _ in range(lenght):
        password += random.choice(chars)
    return password

for i  in range(countpasswords):
    print(generate_password(lenght, chars))
