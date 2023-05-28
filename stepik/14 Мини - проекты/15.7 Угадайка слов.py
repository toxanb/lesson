# Подключите модуль random;
# Создайте глобальный список word_list, содержащий слова, которые будут использоваться в игре.
import random
word_list = ['олово','село']

# Напишите функцию get_word() которая возвращает случайное слово из списка word_list в верхнем регистре.

def get_word(list):
    word = random.choice(list)
    return word.upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                __ -__
                '''
    ]
    return stages[tries]

# Напишите функцию play(), в которой будет осуществляться основная логика игры.
# Функция play() принимает в качестве аргумента слово word, сгенерированное функцией  get_word().

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    count = 0
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(6))
#######################################################################################################################
    while tries != 0:
        print(f'У вас {tries} попыток')
        print(word_completion)
        answer = input('Введите букву или слово целиком : ').upper()
        if answer.isalpha() and len(answer) > 0: # Проверка на дурака
            if len(answer) == 1: # Если буква
                if answer  in guessed_letters:
                    print(f'Вы уже называли букву {answer}')
                else:
                    guessed_letters.append(answer) # Если буквы нет в списке букв то добавляем ее
                if answer in word: # Если буква в слове то  выводим ее на экран
                    for i in word:
                        if i == answer:
                            index = word.find(answer)
                            word_completion = word_completion[: index] + answer + word_completion[index + 1 :]
                            word = word.replace(word[index], '*',1)

                    if '_' not in word_completion:
                        guessed = True
                        break
            if len(answer) > 1 and answer not in guessed_words:
                guessed_words.append(answer)

                if answer == word:
                    guessed = True
                    break
            elif len(answer) > 1 and answer  in guessed_words :
                print(f'Слово {answer} уже было')
        else:
            print('Неверный ввод!!!')
        tries -= 1
    if guessed == True:
        print(f"""
                 ##########################
                 # ПОЗДРАВЛЯЕМ ВЫ ПОБЕДИЛИ #
                 ##########################
                 """)
    else:
        print("""
                ##########################
                #  ВЫ НЕ УГАДАЛИ СЛОВО   #
                ##########################
                """)


again = 'д'
while again == 'д'.lower():
    play(get_word(word_list))
    again = input('Хотите сыграть ещё раз? Д/Н ')