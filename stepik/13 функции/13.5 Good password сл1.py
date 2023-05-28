# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):

    if len(password) < 8:
        return False
    elif len([i for i in password if i.isupper()]) < 1:
        return False
    elif len([i for i in password if i.islower()]) < 1:
        return False
    elif len([i for i in password if i.isdigit()]) < 1:
        return False
    else:
        return True





txt = 'aabbCC11OP'
print(is_password_good(txt))