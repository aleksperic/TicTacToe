import random

#Creating board with 10 " " spaces
board = [' ' for i in range(10)]

#Flip the coin function, uses no arguments, returns random value between 0 and 1 (Tail or Head)
def flip_the_coin():
    print("Fliping the coin...")
    flip = random.randint(0, 1)
    if flip == 0:
        flip = "Tail"
    else:
        flip = "Head"
    return flip

#First to play function, takes 2 args (choise - user input, coin flip - flip_the_coin function)
#Returns message which player should go first based on a user input and random output from flip_the_coin func
def first_to_play(choise, coin_flip):
    if choise == coin_flip:
        return "Player 1 go first, it's a {}, you'll play with X's!".format(coin_flip)
    else:
        return "Player 2 go first, it's a {}, you'll play with X's!".format(coin_flip)

#Fuction which dispays the board to the users in terminal
def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

#Function for inserting a letter 'X' or 'O' to the board
def insert_letter(letter, position):
    board[position] = letter

#Function which asks for a player input
def player_input(letter):
    run = True

    #We use boolean variable run with while loop in order to check few conditions which should be meet
    while run:
        #Asking user to input the position for letter to put into the board
        position = input("Position (1-9): \n")
        try:
            #Trying to cast input to a int variable
            position = int(position)
            #If we were able to to cast input to a int value, now we're checking did the user entered valid position
            if position > 0 and position < 10:
                #If the position is valid (between 0 and 10), we're now checking if the space at given position is free
                #calling function is_space_free with inputed position as an argument, we're reciving True is free
                #or False if it isn't
                if is_space_free(position):
                    #If the space is free, we can call insert letter function
                    #and we are terminating while loop changing run variable to False
                    insert_letter(letter, position)
                    run = False
                else:
                    #Message if space is not free, after checking through is_space_free function, asking for another position
                    print("Sorry this space is occupied...\nPick another!")
                    display_board(board)
            else:
                #Message if player didn't input position within the range, asking to enter between 1-9
                print("Please type number within the range 1-9!\n")
                display_board(board)
        except:
            #User didn't enter a number! Loops again.
            print("Please type the number!\n")
            display_board(board)

#Function which checks is if the inputed position is free (True if it is, False if it isn't
def is_space_free(pos):
    return board[pos] == ' '

#Function which check if player won the game
def is_win(board, letter):

    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
        (board[4] == letter and board[5] == letter and board[6] == letter) or \
        (board[7] == letter and board[8] == letter and board[9] == letter) or \
        (board[1] == letter and board[4] == letter and board[7] == letter) or \
        (board[2] == letter and board[5] == letter and board[8] == letter) or \
        (board[3] == letter and board[6] == letter and board[9] == letter) or \
        (board[1] == letter and board[5] == letter and board[9] == letter) or \
        (board[3] == letter and board[5] == letter and board[7] == letter)

#Function that check is the board full, returns True if there is only one free space in the board
#since we created board with 10 free spaces and we're using 9 for gameplay
def is_board_full(board):
    return board.count(' ') == 1

#Function which asks players to play again
def play_again(again):
    #If input is Y, resetin the board and plays the game again
    if again.lower() == 'y':
        board_reset(board)
        return main()
    #If input is N, terminating the game
    elif again.lower() == 'n':
        return quit(1)

#Function for reseting the board to 10 " " spaces
def board_reset(board):
    for i in range(len(board)):
        board[i] = ' '

#Main function - gameplay
def main():

    #Game intro
    print(
    '''
Welcome to Tic Tac Toe game!
Let's begin...

For the first move, we're going to flip the coin.
Pick:
0 - Tail
1 - Head
    ''')

    #Users picking Head or Tail for flip_the_coin function to determinate which one is going first
    while True:
        try:
            #Aksing player 1 to pick Head or Tail
            choise = int(input("Player 1 pick: "))
            #Looping while they meet the criteria, with following message, if the criteria is met, breaking the loop
            while choise != 0 and choise != 1:
                print("Wrong entry, please choose '0' for Tail or '1' for Head")
                choise = int(input('Your choise: '))
            break
        #Exception if they put anything that is not a number, looping again
        except ValueError:
            print("Try with 0 or 1")
    #If all criterias are met, assigning players picks to variable choise

    if choise == 0:
        choise = "Tail"
        print('Player 1 - Tail\nPlayer 2 - Head\n')
    else:
        choise = "Head"
        print('Player 1 - Head\nPlayer 2 - Tail\n')
    #Callig function first to play with player chioses and flip_the_coin function as an arguments
    print(first_to_play(choise, flip_the_coin()) + '\n')

    #Display the board to users
    display_board(board)

    #Gameplay
    while True:
        #Checking if 'O' player didn't won, if not player 'X' is playing
        if not is_win(board, 'o'):
            print("X's move!")
            player_input(letter='x')
            display_board(board)
            #Checking if the board is full, if it is, breaking the loop, if not gameplay continues
            if is_board_full(board):
                break
        #If 'O' player won, breaking the loop
        else:
            print("Player 'O' won!")
            break
        #Checking if 'X' player didn't won, if not player 'O' is playing
        if not is_win(board, 'x'):
            print("O's move!")
            player_input(letter='o')
            display_board(board)
        #If 'X' player won, breaking the loop
        else:
            print("Player 'X' won!")
            break
    #In case nobody won, and board is full, it'a a draw
    if is_board_full(board):
        print('Tie game!')
    #Asking players to play again
    play_again(input("Do you want to play again? Y/N: "))

#Running the main loop
main()