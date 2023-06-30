def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ')
    print('   |   |')
    print('__________\n')
    print('   |   |')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print('   |   |')
    print('__________\n')
    print('   |   |')
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ')
    print('   |   |')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)


def player_input():
    take_input = "NA"
    while not (take_input == 'X' or take_input == 'O'):
        take_input = input("Do you want to be 'X' or 'O':- ")
    if take_input == 'X':
        return 'X', 'O'
    elif take_input == 'O':
        return 'O', 'X'


# print(player_input())


def place_marker(board, take_input, position):
    board[position] = take_input


# place_marker(test_board, 'S', 8)
# display_board(test_board)


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right side
            (board[3] == mark and board[5] == mark and board[7] == mark) or  # diagonal
            (board[1] == mark and board[5] == mark and board[9] == mark))


# print(win_check(test_board, 'X'))


import random as ra


def choose_first():
    if ra.randint(0, 1) == 0:
        return 'player 1'
    else:
        return 'player 2'


def space_check(board, position):
    return board[position] == ' '


# print(space_check(test_board, 1))


def full_space(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# print(full_space(test_board))


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("chose your next position: (1-9)"))
    return position


# print(player_choice(test_board, 9))


def replay():
    replay_choice = input("Want to play again? (Y/N) ")
    if replay_choice.lower() == 'y':
        return True


# print(replay())


print('Welcome to Tic Tac Toe Game')

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? (Y/N)')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations! player1 has won the game")
                game_on = False
            else:
                if full_space(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Congratulations! Player2 has won the game")
                game_on = False
            else:
                if full_space(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
















































































































