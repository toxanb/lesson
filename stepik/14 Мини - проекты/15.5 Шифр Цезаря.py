# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
# Она должна запрашивать у пользователя следующие данные:
#
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).

# #dec = input('Шифрование "+" или Дешифрование "-" : ')
# dec = '-'
# #lang = input('Выберите язык шифрования ru/en : ')
# lang = 'en'
# #text = input('Введите текст : ')
# text = 'Hawnj pk swhg xabkna ukq nqj.'
# rot = int(input('Шаг сдвига : '))
#
#
#
#
# # Функция Шифрования Ру
# def ecrypt_ru(text, rot):
#     result = ''
#     for i in text:
#         char = (ord(i) + rot)
#         if i in ' !?.,0123456789':
#             result += i
#         elif char > 1103:
#             result += chr(char - 32)
#         else:
#             result +=  chr(char)
#     return result
#
#
# # Функция Шифрования En
# def ecrypt_en(text, rot):
#     result = ''
#     for i in text:
#         char = (ord(i) + rot)
#         if i in ' !?.,0123456789':
#             result += i
#         elif chr(ord(i)).isupper() and char > 90:
#             result += chr(char - 26)
#         elif chr(ord(i)).islower() and char > 122:
#             result += chr(char - 26)
#         else:
#             result +=  chr(char)
#     return result
#
#
# # Функция Расшифровки ru
# def decoding_ru(text, rot):
#     result = ''
#     for i in text:
#         char = (ord(i) - rot)
#         if i in ' !?.,0123456789':
#             result += i
#         elif chr(ord(i)).isupper() and char < 1040:
#             result += chr(char + 32)
#         elif chr(ord(i)).islower() and char < 1072:
#             result += chr(char + 32)
#         else:
#             result += chr(char)
#     return result
#
#
#
# # Функция Расшифровки en
# def decoding_en(text, rot):
#     result = ''
#     for i in text:
#         char = (ord(i) - rot)
#         if i in ' !?.,0123456789':
#             result += i
#         elif chr(ord(i)).isupper() and char < 65:
#             result += chr(char + 26)
#         elif chr(ord(i)).islower() and char < 97:
#             result += chr(char + 26)
#         else:
#             result += chr(char)
#     return result
#
#
#
# if dec == '+' and lang == 'ru' :
#     print(ecrypt_ru(text, rot))
# elif dec == '+' and lang == 'en':
#     print(ecrypt_en(text, rot))
#
# if dec == '-' and lang == 'ru' :
#     print(decoding_ru(text, rot))
# elif  dec == '-' and lang == 'en':
#     print(decoding_en(text, rot))
