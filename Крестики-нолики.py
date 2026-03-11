from random import choice

# можно сделать несколько игроков
# number_of_players = int(input('сколько игроков будет играть? '))
number_of_players = 2

# игра с компьтером
print('Будешь играть с компьютером?')
computer = (True if input('нажми "+" если ДА\nили любую клавишу если НЕТ\n') == '+' else False)

# назначает обозначение игроков
players = []
letter_computer = ''
while len(players) < number_of_players:
    if computer:
        letter_computer = choice('XO')
        players.append(letter_computer)
        print(f'Компьютер выбрал букву {letter_computer}\n')
    if not players:
        print('Первый игрок, ', end='')
    else:
        print('Второй игрок, ', end='')
    letter = input('выбери букву которой будешь играть - ')
    if letter.isalpha():
        if len(letter) == 1:
            if letter not in players:
                players.append(letter)
            else:
                print('эта буква занята')
        else:
            print('одну букву')
    else:
        print('букву')

# размер поля можно сделать другим, но тогда меняется характер игры и программу надо будет дописать.
field_size = 3
battlefield = [[' ' for _ in range(field_size)] for _ in range(field_size)]


def display_field():
    """
    отображение игрового поля
    :return:
    """
    print('\n ', 1, 2, 3)
    for i in range(len(battlefield)):
        print(i + 1, *battlefield[i])
    print()


def computer_progress():
    """
    Ход компьтерного игрока
    :return:
    """
    list_of_free_coordinates = []
    for row in range(field_size):
        for point in range(field_size):
            if battlefield[row][point] == ' ':
                list_of_free_coordinates.append((row, point))
    coordinates = choice(list_of_free_coordinates)
    battlefield[coordinates[0]][coordinates[1]] = letter_computer


# определяет конец игры без выигрыша.
# можно было сделать внутри функции, но тогда пришлось бы останавливать программу этой функцией,
# чтобы остановка программы была в одном месте вынес этот флаг наружу
ended_in_a_draw = False


def check_is_there_a_move(arg):
    """
    поиск выигрышной линии
    :param arg:
    :return:
    """
    return len(set(''.join(''.join(arg).split()))) > 1


def checking_for_a_draw():
    """
    проверка на ничью
    :return:
    """
    global ended_in_a_draw
    is_there_a_move = 8
    for horizontal in battlefield:
        if check_is_there_a_move(horizontal):
            is_there_a_move -= 1
    for i in range(field_size):
        list_of_winnings_columns = []
        for horizontal in battlefield:
            list_of_winnings_columns.append(horizontal[i])
        if check_is_there_a_move(list_of_winnings_columns):
            is_there_a_move -= 1
    list_of_winnings_diagonally = []
    for i in range(field_size):
        list_of_winnings_diagonally.append(battlefield[i][i])
    if check_is_there_a_move(list_of_winnings_diagonally):
        is_there_a_move -= 1
    list_of_winnings_diagonally = []
    for i in range(field_size):
        list_of_winnings_diagonally.append(battlefield[i][field_size - (i + 1)])
    if check_is_there_a_move(list_of_winnings_diagonally):
        is_there_a_move -= 1

    if not is_there_a_move:
        ended_in_a_draw = True
        return False

    return True


def check_winnings():
    """
    проверка на выигрыш
    :return:
    """
    for check_player in players:
        for horizontal in battlefield:
            if all(map(lambda x: x == check_player, horizontal)):
                return False
        for i in range(field_size):
            list_of_winnings_columns = []
            for horizontal in battlefield:
                list_of_winnings_columns.append(horizontal[i] == check_player)
            if all(list_of_winnings_columns):
                return False
        list_of_winnings_diagonally = []
        for i in range(field_size):
            list_of_winnings_diagonally.append(battlefield[i][i] == check_player)
        if all(list_of_winnings_diagonally):
            return False
        list_of_winnings_diagonally = []
        for i in range(field_size):
            list_of_winnings_diagonally.append(battlefield[i][field_size - (i + 1)] == check_player)
        if all(list_of_winnings_diagonally):
            return False
    return True


def next_player():
    """
    генератор следующего ирока
    :return:
    """
    while True:
        for player in players:
            yield player


dictionary_of_move_names = {'Первый': 'Первом',
                            'Второй': 'Втором',
                            'Третий': 'Третьем',
                            'Четвёртый': 'Четвёртом',
                            'Пятый': 'Пятом',
                            'Шестой': 'Шестом',
                            'Седьмой': 'Седьмом',
                            'Восьмой': 'Восьмом',
                            'Девятый': 'Девятом'}


def numbering_of_moves():
    """
    генератор, считает ходы
    :return:
    """
    for move in dictionary_of_move_names.keys():
        yield move


# ход игры

next_player = next_player()
player_walks = ''
move_number = numbering_of_moves()
last_move_number = ''
print('\nна поле тишина...')
display_field()
while check_winnings() and checking_for_a_draw():
    player_walks = next(next_player)
    last_move_number = next(move_number)
    print(f'{last_move_number} ход')
    print(f'ходит игрок - {player_walks}')
    if player_walks == letter_computer:
        computer_progress()
        display_field()
    else:
        print('введи координаты хода')
        print(f'      (должно быть число от 1 до {field_size})')
        player_move = [0, 0, True]
        while player_move[2]:
            while player_move[0] == 0:
                line = input('номер строки - ')
                if line in ''.join([str(i) for i in range(1, field_size + 1)]):
                    player_move[0] = int(line)
                else:
                    print(f'''   ! должно быть число от 1 до {field_size}''')
            while player_move[1] == 0:
                line = input('номер столбца - ')
                if line in ''.join([str(i) for i in range(1, field_size + 1)]):
                    player_move[1] = int(line)
                else:
                    print(f'''   ! должно быть число от 1 до {field_size}''')
            if battlefield[player_move[0] - 1][player_move[1] - 1] == ' ':
                battlefield[player_move[0] - 1][player_move[1] - 1] = player_walks
                display_field()
                player_move[2] = False
            else:
                print('эта клетка занята')
                player_move[0] = player_move[1] = 0


if ended_in_a_draw:
    print(f'''игра кончилась в ничью.
выигрывшего нет.
играем ещё раз?''')
else:
    print(f'''конец игры!
на {dictionary_of_move_names[last_move_number]} ходу
выиграл ирок --> {player_walks}
ПOЗДРАВЛЯЮ!!!''')
