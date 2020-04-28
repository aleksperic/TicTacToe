import random

board = [' ' for i in range(10)]

def flip_the_coin():
    print("Fliping the coin...")
    flip = random.randint(0, 1)
    if flip == 0:
        flip = "Tail"
    else:
        flip = "Head"
    return flip

def first_to_play(choise, coin_flip):
    if choise == coin_flip:
        return "Player 1 go first, it's a {}, you'll play with X's!".format(coin_flip)
    else:
        return "Player 2 go first, it's a {}, you'll play with X's!".format(coin_flip)

def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def insert_letter(letter, position):
    board[position] = letter

def player_input(letter):
    run = True

    while run:

        position = input("Position (1-9): \n")
        try:
            position = int(position)
            if position > 0 and position < 10:
                if is_space_free(position):
                    run = False
                    insert_letter(letter, position)
                else:
                    print("Sorry this space is occupied...\nPick another!")
                    display_board(board)
            else:
                print("Please type number within the range 1-9!\n")
                display_board(board)
        except:
            print("Please type the number!\n")
            display_board(board)

def is_space_free(pos):
    return board[pos] == ' '

def is_win(board, letter):

    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
        (board[4] == letter and board[5] == letter and board[6] == letter) or \
        (board[7] == letter and board[8] == letter and board[9] == letter) or \
        (board[1] == letter and board[4] == letter and board[7] == letter) or \
        (board[2] == letter and board[5] == letter and board[8] == letter) or \
        (board[3] == letter and board[6] == letter and board[9] == letter) or \
        (board[1] == letter and board[5] == letter and board[9] == letter) or \
        (board[3] == letter and board[5] == letter and board[7] == letter)

def is_board_full(board):
    return board.count(' ') == 1

def play_again(again):
    if again.lower() == 'y':
        board_reset(board)
        return main()
    elif again.lower() == 'n':
        return quit(1)

def board_reset(board):
    for i in range(len(board)):
        board[i] = ' '

def main():
    print(
    '''
Welcome to Tic Tac Toe game!
Let's begin...

For the first move, we're going to flip the coin.
Pick:
0 - Tail
1 - Head
    ''')
    while True:
        try:
            choise = int(input("Player 1 pick: "))
            while choise != 0 and choise != 1:
                print("Wrong entry, please choose '0' for Tail or '1' for Head")
                choise = int(input('Your choise: '))
            break
        except ValueError:
            print("Try with 0 or 1")

    if choise == 0:
        choise = "Tail"
        print('Player 1 - Tail\nPlayer 2 - Head\n')
    else:
        choise = "Head"
        print('Player 1 - Head\nPlayer 2 - Tail\n')

    print(first_to_play(choise, flip_the_coin()) + '\n')

    display_board(board)

    while True:
        if not is_win(board, 'o'):
            print("X's move!")
            player_input(letter='x')
            display_board(board)
            if is_board_full(board):
                break
        else:
            print("Player 'O' won!")
            break
        if not is_win(board, 'x'):
            print("O's move!")
            player_input(letter='o')
            display_board(board)
        else:
            print("Player 'X' won!")
            break
    if is_board_full(board):
        print('Tie game!')
    play_again(input("Do you want to play again? Y/N: "))

main()