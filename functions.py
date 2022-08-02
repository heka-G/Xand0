"                              крестики - нолики"

import random


def display_board(board):
    print('\n'*10)
    print(board[7] + '  | ' + board[8] + ' |  ' + board[9])
    print('---|---|---')
    print(board[4] + '  | ' + board[5] + ' |  ' + board[6])
    print('---|---|---')
    print(board[1] + '  | ' + board[2] + ' |  ' + board[3])


def choose_your_fighter():
    marker = ''
    while marker != 'X' and marker != '0':
        marker = input('Выберите, вы хотите играть за X или О: ')
    player1 = marker
    if player1 == 'X':
        player2 = '0'
    else:
        player2 = 'X'
    print(f'Player 1 is {player1}', f'|| Player 2 is {player2}')
    return(player1, player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or  #проверка всех комбинаций выигрыша
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def first_move():
    if random.randrange(0,101) < 50:
        return 'Игрок 1'
    else:
        return 'Игрок 2'

def space_check(board,position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    for space in range(len(board)):
        if space_check(board, space):
            return False
        else:
            return True

def player_choice(board):
    position = int(input('Введите на какую клетку хотите поставить(1-9): '))
    if space_check(board,position) == True:
        return position

def replay():
    x = input('Хотите ли вы сыграть еще раз? Yes / No: ').lower()
    if x == 'Yes'.lower():
        return True
    else:
        return False




