# Проект "Wordle". V-0.3.5.2

# vvv Часть 0.1: Импортирование и определение функций-------------------------------------------------------------------
import random
from extra import text_read

def round_alt(num: float):
    num = float(num)
    integer, decimal_ = str(num).split('.')
    integer = int(integer)
    low_values = ('0', '1', '2', '3', '4')
    if decimal_[0] in low_values:
        result = integer
    else:
        if num >= 0:
            result = integer + 1
        else:
            result = integer - 1
    return result


# vvv Часть 0.2: Подготовка(задание значений переменным)----------------------------------------------------------------
(word, difficulty, language, duration, mode, mode_type, words, r, language_ID, difficulty_ID, duration_ID, mode_ID,
 mode_type_ID, error_ID, attempt_loss, attempts_recover, total_points, length, green_counter, yellow_counter,
 grey_counter) = '','','','','','','','', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
(russian_words, russian_easy, russian_normal, russian_hard, russian_extreme, english_words, english_easy,
 english_normal, english_hard, english_extreme, user_words,
 guessed_words) = [], [], [], [], [], [], [], [], [], [], [], []
continuation = 1
rand_mode, rand_language, rand_difficulty, win, lose, guessed = False, False, False, False, False, False
russian_letters = tuple('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
english_letters = tuple('abcdefghijklmnopqrstuvwxyz')
letters = {1:russian_letters,2:english_letters}
game_mode = {11:russian_easy, 12:russian_normal, 13:russian_hard, 14:russian_extreme,
             21:english_easy, 22:english_normal, 23:english_hard, 24:english_extreme}
point_loss_lib = {1:25, 2:20, 3:10, 4:5}
word_length = {1:(4, 5), 2:(6, 7), 3:(8, 10), 4:(11, 15)}
functions = {'#':1, '/':2}
duration_text = {1:'Продолжительность - одна игра.', 2:'Продолжительность - на рекорд.',
                 3:'Продолжительность - бесконечная.'}
mode_text = {1:'Режим - классический.', 2:'Режим - набор букв.', 3:'Режим - 5 букв.'}
mode_win_text = {1:'слово!', 2:'набор букв!', 3:'все слова!'}
sentence_start_text = {1: 'Загаданное слово', 2: 'Загаданный набор букв', 3: 'Загаданные слова'}
mode_type_text = {1:'Тип режима - классический.', 2:'Тип режима - модифицированный.'}
language_text = {1:' на русском языке.', 2:' на английском языке.'}
difficulty_text = {1:'Уровень сложности - лёгкий.', 2:'Уровень сложности - средний.',
                   3:'Уровень сложности - сложный.', 4:'Уровень сложности - очень сложный.'}
file_r = open(r'C:\Users\Admin\Downloads\russian (1).txt', 'r', encoding='windows-1251')
for line in file_r:
    line_ = line[0: -1]
    russian_words.append(line_)
    if len(line_) > 10 and line_.isalpha() and line_.islower():
        russian_extreme.append(line_)
    elif 8 <= len(line_) <= 10 and line_.isalpha() and line_.islower():
        russian_hard.append(line_)
    elif 6 <= len(line_) <= 7 and line_.isalpha() and line_.islower():
        russian_normal.append(line_)
    elif 4 <= len(line_) <= 5 and line_.isalpha() and line_.islower():
        russian_easy.append(line_)
file_r.close()
file_e = open(r'C:\Users\Admin\Downloads\words_alpha.txt', 'r')
for line in file_e:
    line_ = line[0: -1]
    english_words.append(line_)
    if len(line_) > 10 and line_.isalpha() and line_.islower():
        english_extreme.append(line_)
    elif 8 <= len(line_) <= 10 and line_.isalpha() and line_.islower():
        english_hard.append(line_)
    elif 6 <= len(line_) <= 7 and line_.isalpha() and line_.islower():
        english_normal.append(line_)
    elif 4 <= len(line_) <= 5 and line_.isalpha() and line_.islower():
        english_easy.append(line_)
file_e.close()
# vvv Часть 1: Настройки------------------------------------------------------------------------------------------------
while True:
    duration = input('\nВведите продолжительность или номер (одна игра(1), на рекорд(2) или бесконечная(3)): ')
    if duration == 'одна игра' or duration == '1':
        duration_ID = 1
        break
    elif duration == 'на рекорд' or duration == '2':
        duration_ID = 2
        break
    elif duration == 'бесконечная' or duration == '3':
        duration_ID = 3
        break
    else:
        print('Продолжительность введена некорректно.')
while True:
    mode = input('\nВведите режим или номер (классический(1), набор букв(2), 5 слов(3) или случайный(4)): ')
    if mode == 'классический' or mode == '1':
        mode_ID = 1
        break
    elif mode == 'набор букв' or mode == '2':
        mode_ID = 2
        break
    elif mode == '5 слов' or mode == '3':
        mode_ID = 3
        break
    elif mode == 'случайный' or mode == '4':
        mode_ID = 4
        break
    else:
        print('Режим введён некорректно.')
while True:
    mode_type = input('\nВведите тип режима или номер (классический(1) или модифицированный(2)): ')
    if mode_type == 'классический' or mode_type == '1':
        mode_type_ID = 1
        break
    elif mode_type == 'модифицированный' or mode_type == '2':
        mode_type_ID = 2
        break
    else:
        print('Тип режима введён некорректно.')
while True:
    language = input('\nВведите язык или номер (русский(1), английский(2) или случайный(3)): ')
    if language == 'русский' or language == '1':
        language_ID = 1
        break
    elif language == 'английский' or language == '2':
        language_ID = 2
        break
    elif language == 'случайный' or language == '3':
        language_ID = 3
        break
    else:
        print('Язык введён некорректно.')
while True:
    difficulty = input('\nВведите уровень сложности или номер '
                       '(лёгкий(1), средний(2), сложный(3), очень сложный(4) или случайный(5)): ')
    if difficulty == 'лёгкий' or difficulty == '1':
        difficulty_ID = 1
        break
    elif difficulty == 'средний' or difficulty == '2':
        difficulty_ID = 2
        break
    elif difficulty == 'сложный' or difficulty == '3':
        difficulty_ID = 3
        break
    elif difficulty == 'очень сложный' or difficulty == '4':
        difficulty_ID = 4
        break
    elif difficulty == 'случайный' or difficulty == '5':
        difficulty_ID = 5
        break
    else:
        print('Уровень сложности введён некорректно.')
while True:
    attempts = input('\nВведите количество попыток (от 1 до 1000): ')
    if attempts.isdigit() and len(attempts)<4 and attempts != '0':
        attempts = int(attempts)
        multiplier = 100 / attempts
        break
    else:
        print('Количество попыток введено некорректно.')
attempts_recover = attempts
if language_ID == 3:
    rand_language = True
if difficulty_ID == 5:
    rand_difficulty = True
if mode_ID == 4:
    rand_mode = True
#elif mode_ID == 2:
# vvv Часть 2: Игра-----------------------------------------------------------------------------------------------------
while continuation > 0:
    # vvv Часть 2.1: Подготовка к новому раунду-------------------------------------------------------------------------
    if rand_mode:
        mode_ID = random.randint(1,3)
    if rand_language:
        language_ID = random.randint(1,2)
    if rand_difficulty:
        difficulty_ID = random.randint(1,4)
    attempts = attempts_recover
    print('\n', duration_text.get(duration_ID), sep='')
    print(mode_text.get(mode_ID))
    print(mode_type_text.get(mode_type_ID))
    print(sentence_start_text.get(mode_ID) + language_text.get(language_ID))
    print(difficulty_text.get(difficulty_ID))
    print(f'У вас {attempts} попыток.')
    print(f'Очков : {total_points}', '', sep='\n')
    if mode_ID == 1:
        word = random.choice(game_mode.get(language_ID * 10 + difficulty_ID))
    elif mode_ID == 2:
        a = ''
        for i in range(5 + (difficulty_ID - 1) * 2):
            a += random.choice(letters.get(language_ID))
        word = a
    else:
        length = random.choice(word_length.get(difficulty_ID))
        if language_ID == 1:
            word = 'й' * length
        else:
            word = 'q' * length
        guessed_words = []
        random.shuffle(game_mode.get(language_ID * 10 + difficulty_ID))
        for i in game_mode.get(language_ID * 10 + difficulty_ID):
            if len(i) == length and len(guessed_words) <= 4:
                guessed_words.append(i)
        print(guessed_words)# (для проверки)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    print(word)# (для проверки)+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if mode_ID == 1:
        points = len(word) * 100
    elif mode_ID == 2:
        points = len(word) * 300
    else:
        points = length * 2500
    point_loss = point_loss_lib.get(difficulty_ID)
    continue_ = True
    # vvv Часть 2.2: Действие-------------------------------------------------------------------------------------------
    while continue_:
        # vvv Часть 2.21: Подготовка к раскрытию букв-------------------------------------------------------------------
        words, user_words, attempt_loss, error_ID, special_guess, special_guess_number = '', [], 0, 0, 0, 0
        grey_counter, yellow_counter, green_counter = 0, 0, 0
        lose, win, guessed = False, False, False
        print('Введите слово из', len(word), 'букв:', end=' ')
        user_word = input().lower()
        while True:
            if mode_type_ID == 2 and not '!' in user_word and not '№' in user_word:
                for i in user_word:
                    if i == '#' or i == '/':
                        attempt_loss += functions.get(i)
                        if words:
                            user_words.append(words)
                        words = ''
                    else:
                        words += i
                if words:
                    user_words.append(words)
            elif mode_type_ID == 2 and '!' in user_word and user_word.find('!!') == -1:
                if (user_word[0] == '!' and user_word.find('!') == 0 and user_word.count('!') == 1
                        and len(user_word) == 2 and user_word[1].isalpha()
                        and bool(user_word[1].isascii() == word.isascii())):
                    words = user_word[1] * len(word)
                    special_guess = 1
                    attempt_loss = len(word) - 1
                else:
                    error_ID = 1
                    print('Функция использована неправильно.')
            elif mode_type_ID == 2 and '№' in user_word and user_word.find('№№') == -1:
                special_guess_number = int(user_word[1:len(user_word)])\
                    if (user_word[1:len(user_word)].isdigit() == True
                        and 0 < int(user_word[1:len(user_word)]) <= len(word)) else 0
                if (user_word[0] == '№' and user_word.find('№') == 0 and user_word.count('№') == 1
                        and 2 <= len(user_word) <= len(str(len(word))) + 1 and special_guess_number != 0):
                    special_guess = 2
                    attempt_loss = len(word) * 2 - 1
                else:
                    error_ID = 1
                    print('Функция использована неправильно.')
            elif mode_type_ID == 2 and '!!' in user_word:
                if mode_ID == 3 and len(guessed_words) != 1:
                    if (user_word.find('!!') == 0 and user_word.count('!!') == 1 and len(user_word) == 3
                            and user_word[2].isalpha() and bool(user_word[2].isascii() == word.isascii())):
                        words = user_word[2] * len(word)
                        special_guess = 3
                        attempt_loss = len(guessed_words) * len(word) - 1
                    else:
                        error_ID = 1
                        print('Функция использована неправильно.')
                else:
                    error_ID = 1
                    print('Невозможно использовать данную функцию.')
            elif mode_type_ID == 2 and '№№' in user_word:
                if mode_ID == 3 and len(guessed_words) != 1:
                    special_guess_number = int(user_word[2:len(user_word)])\
                        if (user_word[2:len(user_word)].isdigit()
                            and 0 < int(user_word[2:len(user_word)]) <= len(word)) else 0
                    if (user_word.find('№№') == 0 and user_word.count('№№') == 1 and
                            3 <= len(user_word) <= len(str(len(word))) + 2 and special_guess_number != 0):
                        special_guess = 4
                        attempt_loss = len(guessed_words) * len(word) * 2 - 1
                    else:
                        error_ID = 1
                        print('Функция использована неправильно.')
                else:
                    error_ID = 1
                    print('Невозможно использовать данную функцию.')
            elif mode_type_ID == 1:
                user_words.append(user_word)
            while True:
                if user_word.count('/') + 1 != len(user_words) and special_guess == 0 and error_ID == 0:
                    error_ID = 1
                    print('Функции использованы неправильно.')
                    break
                elif attempts - attempt_loss <= 0:
                    error_ID = 1
                    print('Затрата попыток превышает число оставшихся попыток.')
                    break
                else:
                    break
            break
        for i in range(len(user_words)):
            m = user_words[i]
            if (not m.isalpha and user_word != '*guess'
                    or not bool(word.isascii() == m.isascii()) and user_word != '*guess'
                    or m.isascii() == False and not m in russian_words and user_word != '*guess'
                    or m.isascii() == True and not m in english_words and user_word != '*guess'
                    or len(user_word) != len(word) and user_word != '*guess'):
                error_ID = 2
        if error_ID != 0:
            if error_ID == 2:
                print('Пожалуйста, введите слово(а) из', len(word), 'букв на заданном языке.')
            continue
        if mode_ID == 1:
            if user_word == word:
                win = True
            elif user_word == '*guess':
                print('Невозможно применить данную команду.')
                continue
            else:
                lose = True
        elif mode_ID == 2:
            if user_word == '*guess':
                while True:
                    user_word = input('Введите загаданный набор букв: ')
                    if (not user_word.isalpha() or len(user_word) != len(word)
                        or language_ID == 1 and
                        len(text_read(ascii(user_word), start_substring="'", end_substring="'")) != len(user_word)*6
                        or language_ID == 2 and
                        len(text_read(ascii(user_word), start_substring="'", end_substring="'")) != len(user_word)):
                        print(f'Пожалуйста, введите набор из {len(word)} букв заданного языка.')
                        continue
                    break
                if user_word != word:
                    print('Неверный ответ!')
                    special_guess = -1
                    lose = True
                else:
                    win = True
            else:
                if user_word != word:
                    lose = True
                else:
                    win = True
        elif mode_ID == 3:
            if len(guessed_words) == 1 and user_word in guessed_words:
                win = True
            else:
                lose = True
        # vvv Часть 2.22: Раскрытие букв--------------------------------------------------------------------------------
        if win:
            print(f'Поздравляем, вы угадали {mode_win_text.get(mode_ID)}',
                  end=' ' * (48 - len(mode_win_text.get(mode_ID))))
            for i in user_word:
                print('\033[42m', i, '\033[0m', end=' ')
            continue_ = False
            break
        if lose:
            if mode_ID == 3 and user_word in guessed_words and len(guessed_words) != 1:
                attempts += 1
                guessed = True
            print(f'Оставшиеся попытки: {attempts - 1 - attempt_loss}',
                  ' ' * (51 - len(str(attempts - 1 - attempt_loss))), end='')
            if mode_ID != 3 or len(guessed_words) == 1:
                if mode_ID == 3:
                    word = guessed_words[0]
                if special_guess == 0:
                    for i in range(len(user_word)):
                        n = user_word[i]
                        if user_word[i] == word[i]:
                            print('\033[42m', n, '\033[0m', end=' ')
                        elif user_word[i] in word and user_word[i] != word[i]:
                            print('\033[43m', n, '\033[0m', end=' ')
                        elif user_word[i] == '#' or user_word[i] == '/':
                            print('\033[40m', n, '\033[0m', end=' ')
                        else:
                            print('\033[47m', n, '\033[0m', end=' ')
                elif special_guess == 1:
                    for i in range(len(words)):
                        if words[i] == word[i]:
                            print('\033[42m', words[i], '\033[0m', end=' ')
                        else:
                            print('\033[40m', '_', '\033[0m', end=' ')
                elif special_guess == 2:
                    for i in range(len(word)):
                        if i + 1 != special_guess_number:
                            print('\033[40m', '_', '\033[0m', end=' ')
                        else:
                            print('\033[42m', word[i], '\033[0m', end=' ')
            else:
                r = random.choice(guessed_words)
                if special_guess == 0:
                    if user_word in guessed_words:
                        guessed_words.remove(user_word)
                    for i in guessed_words:
                        for l in range(len(i)):
                            if user_word[l] == i[l]:
                                green_counter += 10 ** l
                            elif user_word[l] in i and user_word[l] != i[l]:
                                yellow_counter += 10 ** l
                            else:
                                grey_counter += 10 ** l
                    green_counter = f'{green_counter:0{len(word)}}'
                    green_counter = green_counter[::-1]
                    yellow_counter = f'{yellow_counter:0{len(word)}}'
                    yellow_counter = yellow_counter[::-1]
                    grey_counter = f'{grey_counter:0{len(word)}}'
                    grey_counter = grey_counter[::-1]
                    for i in range(len(user_word)):
                        n = user_word[i]
                        if green_counter[i] == str(len(guessed_words)):
                            print('\033[42m', n, '\033[0m', end=' ')
                        elif yellow_counter[i] == str(len(guessed_words)):
                            print('\033[43m', n, '\033[0m', end=' ')
                        elif grey_counter[i] == str(len(guessed_words)) and n != '#' and n != '/':
                            print('\033[47m', n, '\033[0m', end=' ')
                        elif grey_counter[i] == '0':
                            print('\033[45m', n, '\033[0m', end=' ')
                        elif user_word[i] == '#' or user_word[i] == '/':
                            print('\033[40m', n, '\033[0m', end=' ')
                        else:
                            print('\033[44m', n, '\033[0m', end=' ')
                    print('')
                    if guessed:
                        print('Поздравляем, вы угадали одно из слов!', ' '*72, sep = '\n', end = '')
                        for i in range(len(grey_counter)):
                            n = grey_counter[i]
                            if user_word[i] != '#' and user_word[i] != '/':
                                print('\033[47m', n, '\033[0m', end=' ')
                            else:
                                print('\033[40m', user_word[i], '\033[0m', end=' ')
                    else:
                        print('',' '*72, sep = '\n', end = '')
                        for i in range(len(grey_counter)):
                            n = grey_counter[i]
                            if user_word[i] != '#' and user_word[i] != '/':
                                print('\033[47m', n, '\033[0m', end=' ')
                            else:
                                print('\033[40m', user_word[i], '\033[0m', end=' ')
                    print(f'\nОставшихся слов: {len(guessed_words)}', ' '*72, sep = '\n', end = '')
                    for i in range(len(yellow_counter)):
                        n = yellow_counter[i]
                        if user_word[i] != '#' and user_word[i] != '/':
                            print('\033[43m', n, '\033[0m', end=' ')
                        else:
                            print('\033[40m', user_word[i], '\033[0m', end=' ')
                    print('')
                    print('', ' '*72, sep = '\n', end = '')
                    for i in range(len(green_counter)):
                        n = green_counter[i]
                        if user_word[i] != '#' and user_word[i] != '/':
                            print('\033[42m', n, '\033[0m', end=' ')
                        else:
                            print('\033[40m', user_word[i], '\033[0m', end=' ')
                    print('')
                elif special_guess == 1:
                    for i in range(len(words)):
                        if words[i] == r[i]:
                            print('\033[42m', words[i], '\033[0m', end=' ')
                        else:
                            print('\033[40m', '_', '\033[0m', end=' ')
                    print('')
                elif special_guess == 2:
                    for i in range(len(r)):
                        if i + 1 != special_guess_number:
                            print('\033[40m', '_', '\033[0m', end=' ')
                        else:
                            print('\033[42m', r[i], '\033[0m', end=' ')
                    print('')
                elif special_guess == 3:
                    for i in guessed_words:
                        for n in range(len(i)):
                            if i[n] == words[n]:
                                print('\033[42m', i[n], '\033[0m', end=' ')
                            else:
                                print('\033[40m', '_', '\033[0m', end=' ')
                        if i != guessed_words[-1]:
                            print('', '',' ' * 72, sep='\n', end='')
                        else:
                            print('', ' ' * 72, sep='\n', end='')
                elif special_guess == 4:
                    for i in guessed_words:
                        for n in range(len(i)):
                            if n + 1 != special_guess_number:
                                print('\033[40m', '_', '\033[0m', end=' ')
                            else:
                                print('\033[42m', i[n], '\033[0m', end=' ')
                        if i != guessed_words[-1]:
                            print('', '',' ' * 72, sep='\n', end='')
                        else:
                            print('', ' ' * 72, sep='\n', end='')
            attempts -= 1 + attempt_loss
            points -= (1 + attempt_loss) * point_loss if points - (1 + attempt_loss) * point_loss >= 0 else points
            print('')
            if attempts <= 0:
                continue_ = False
                break
    # vvv Часть 2.3: Завершение действия
    if not continue_ and attempts > 0:
        total_points += round_alt(points * multiplier)
        print('')
        if duration_ID == 1:
            continuation = 0
        elif duration_ID == 2:
            continuation = 1
            attempts_recover = attempts
    else:
        if mode_ID != 3:
            print(f'\nВы проиграли! {sentence_start_text.get(mode_ID)} - "{word}"')
        else:
            print(f'\nВы проиграли! Оставшиеся загаданные слова - "{', '.join(guessed_words)}"')
        if duration_ID != 3:
            continuation = 0
        else:
            total_points = 0
# vvv Часть 3: Конец----------------------------------------------------------------------------------------------------
print(f'\nВсего вы набрали {total_points} очков.')