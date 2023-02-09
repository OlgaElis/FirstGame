player_1 = input('Input Your name: ')   #Ввод имени первого игрока
player_2 = input('Input Your name: ')   #Ввод имени второго игрока обязательно

symbol_1 = str(input('Choose "x" or "o": ')).lower()    #Выбор символа игры - крестик или нолик
if symbol_1 == 'x':  #Автоматическое присвоение другого символа второму игроку
    print(f'Ok, {player_2} will play "o".')
    symbol_2 = 'o'
else:
    print(f'Ok, {player_2}  will play "x"')
    symbol_2 = 'x'

dictionary_of_gamers = {symbol_1: player_1, symbol_2: player_2}  #Создание словаря

winner_1 = dictionary_of_gamers['o'] #Присвоение победителя в зависимости от крестика или нолика
winner_2 = dictionary_of_gamers['x']


def gamer_1(x):     #Функция ввода координат места, куда будет ставиться значок первого игрока
    a = list(x)     #Создание списка из координат
    a.remove(' ')   #Удаление из списка пробела
    a = [x + 1 for x in list(map(int, a))]      #Увеличение каждого элемента списка на +1, чтобы координаты на поле совпадали с реальными координатами в матрице поля
    field[a[0]][a[1]] = symbol_1     #Добавление символа на место координат
    for x in field:      #Вывод поля с введеным символом
        print('   '.join((map(str, x))))


def gamer_2(x):      #Аналогичная функция для второго игрока
    b = list(x)
    b.remove(' ')
    b = [x+1 for x in list(map(int, b))]
    field[b[0]][b[1]] = symbol_2
    for x in field:
        print('   '.join((map(str, x))))


def comb(field):    #Функция перебора победных комбинаций: равенство по строкам, столбцам и диагоналям всех элементов матрицы какому-то одному
    if field[1][1] == field[1][2] == field[1][3] == 'o' or field[1][1] == field[1][2] == field[1][3] == 'x':
        return 'Winner'
    elif field[2][1] == field[2][2] == field[2][3] == 'o' or field[2][1] == field[2][2] == field[2][3] == 'x':
        return 'Winner'
    elif field[3][1] == field[3][2] == field[3][3] == 'o' or field[3][1] == field[3][2] == field[3][3] == 'x':
        return 'Winner'
    elif field[1][1] == field[2][1] == field[3][1] == 'o' or field[1][1] == field[2][1] == field[3][1] == 'x':
        return 'Winner'
    elif field[1][2] == field[2][2] == field[3][2] == 'o' or field[1][2] == field[2][2] == field[3][2] == 'x':
        return 'Winner'
    elif field[1][3] == field[2][3] == field[3][3] == 'o' or field[1][3] == field[2][3] == field[3][3] == 'x':
        return 'Winner'
    elif field[1][1] == field[2][2] == field[3][3] == 'o' or field[1][1] == field[2][2] == field[3][3] == 'x':
        return 'Winner'
    elif field[1][3] == field[2][2] == field[3][1] == 'o' or field[1][3] == field[2][2] == field[3][1] == 'x':
        return 'Winner'
    else:
        return'No winner'


def no_one(field):   #Функция определения победителя при равенстве крестиков и ноликов
    if field[1][1] == field[1][2] == field[1][3] == 'o':
        return 'Winner o'
    elif field[1][1] == field[1][2] == field[1][3] == 'x':
        return 'Winner x'
    elif field[2][1] == field[2][2] == field[2][3] == 'o':
        return 'Winner o'
    elif field[2][1] == field[2][2] == field[2][3] == 'x':
        return 'Winner x'
    elif field[3][1] == field[3][2] == field[3][3] == 'o':
        return 'Winner o'
    elif field[3][1] == field[3][2] == field[3][3] == 'x':
        return 'Winner x'
    elif field[1][1] == field[2][1] == field[3][1] == 'o':
        return 'Winner o'
    elif field[1][1] == field[2][1] == field[3][1] == 'x':
        return 'Winner x'
    elif field[1][2] == field[2][2] == field[3][2] == 'o':
        return 'Winner o'
    elif field[1][2] == field[2][2] == field[3][2] == 'x':
        return 'Winner x'
    elif field[1][3] == field[2][3] == field[3][3] == 'o':
        return 'Winner o'
    elif field[1][3] == field[2][3] == field[3][3] == 'x':
        return 'Winner x'
    elif field[1][1] == field[2][2] == field[3][3] == 'o':
        return 'Winner o'
    elif field[1][1] == field[2][2] == field[3][3] == 'x':
        return 'Winner x'
    elif field[1][3] == field[2][2] == field[3][1] == 'o':
        return 'Winner o'
    elif field[1][3] == field[2][2] == field[3][1] == 'x':
        return 'Winner x'
    else:
        return'No winner'


try_again = 'yes'  #Объявление переменной для повтора игры, если игроки хотят еще поиграть

while try_again == 'yes':   #Пока игроки хотят играть, тело игры повторяется
    field = [[" ", 0, 1, 2],    #Объявление матрицы поля
        [0, "-", "-", "-"],
        [1, "-", "-", "-"],
        [2, "-", "-", "-"]]
    for x in field:     #Вывод матрицы поля
        print('   '.join((map(str, x))))
    place_1 = input(f'Chose place, gamer {player_1}. Print the number of the row and column, separated by space: ')  #Ввод координат месторасположения знака для первого игрока
    gamer_1(place_1)    #Вызов функции gamer_1 ввода знака для первого игрока от его координат
    c = 4   #Переменная-костыль, которая останавливает цикл на 66 строке в случае ничьей и полного заполнения поля
    for i in field:     #Заполнение поля
        for j in i:
            while j == '-' and c > 0:
                if comb(field) == 'Winner':     #Остановка цикла в случае победы игрока
                    break
                place_2 = input(f'Chose place, gamer {player_2}. Print the number of the row and column, separated by space: ')     #Ввод координат месторасположения знака для второго игрока
                gamer_2(place_2)    #Вызов функции gamer_2 ввода знака для первого игрока от его координат
                comb(field)     #Проверка выигрышных комбинаций на поле
                if comb(field) == 'Winner':  #Остановка цикла в случае победы игрока
                    break
                place_1 = input(f'Chose place, gamer {player_1}. Print the number of the row and column, separated by space: ')  #Аналогично, но для первго игрока. Проверка на прекращение цикла в случае победы первого игрока проводится на строке 67
                gamer_1(place_1)
                comb(field)
                c -= 1

    count_x = 0     #Счетчик крестиков
    count_o = 0     #Счетчик ноликов
    for i in field:     #Прохождение по итоговому полю, подсчет их количества
        for j in i:
            if j == 'x':
                count_x +=1
            elif j == 'o':
                count_o +=1

    if count_o > count_x and comb(field) == 'Winner':   #Если ноликов больше, чем крестиков, то выиграл игрок, играющий за нолики
        print(f'Gamer {winner_1} is winner!')
    elif count_o < count_x and comb(field) == 'Winner':     #Если крестиков больше, чем ноликов, то выиграл игрок, играющий за крерстики
        print(f'Gamer {winner_2} is winner!')
    elif count_o == count_x and comb(field) == 'Winner':    #Если их поровну, то проверит, для какого именно знака выполняется условие победы, и вывести победителя
        if no_one(field) == 'Winner o':
            print(f'Gamer {winner_1} is winner!')
        else:
            print(f'Gamer {winner_2} is winner!')
    else:   #В противном случае нет победителей
        print("No one winner, sorry.")

    try_again = input('Do you want play again? Answer "no" or "yes": ')     #Повторение игры, если игрок отвечает да. Если отвечает нет - то игра заканчивается
    if try_again == 'no':
        print("Let's play later. Bye!")
