import random
import functions



print('             Welcome to game <<X and 0>>!!!!')
while True: #Настройка
    GameBoard = [' '] * 10
    player1_marker, player2_marker = functions.choose_your_fighter() #распаковка кортежа
    turn = functions.first_move()
    print(turn + ' ходит первым')

    play_game = input('Вы готовы?(Да / Нет): ' )

    if play_game.lower()[0] == 'д':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок 1':     #игрок1 ходит
            functions.display_board(GameBoard)
            position = functions.player_choice(GameBoard)
            functions.place_marker(GameBoard,player1_marker,position)

            if functions.win_check(GameBoard, player1_marker):
                functions.display_board(GameBoard)
                print('Победа игрока 1!!!')
                game_on = False
            else:
                if functions.full_board_check(GameBoard):
                    functions.display_board(GameBoard)
                    print('Ничья...')
                    break
                else:
                    turn = 'Игрок 2'
        else:    #игрок2 ходит
            functions.display_board(GameBoard)
            position = functions.player_choice(GameBoard)
            functions.place_marker(GameBoard, player2_marker,position)

            if functions.win_check(GameBoard, player1_marker):
                functions.display_board(GameBoard)
                print('Победа игрока 2!!!')
                game_on = False
            else:
                if functions.full_board_check(GameBoard):
                    functions.display_board(GameBoard)
                    print('Ничья...')
                    break
                else:
                    turn = 'Игрок 1' #никто не выиграл -> другой ходит

    if not functions.replay():
        break


    break
