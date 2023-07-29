# Greetings


""" SUBJECT = ICT 
ASSIGNMENT = FINAL LAB PROJECT
SIR = SIR KHURRAM IQBAL
THIS GAME IS PROGRAMMED BY UMER FAROOQ CYBER SECURITY FIRST SEMESTER COMSATS UNIVERSITY ISLAMABAD
REG NO# FA22-BCT-036 
"""


import random
print(
    '''
**************************************************************HEY THERE ! WELCOME TO*************************************************************
                                                                   TIC TAC TOE
*****************************************************THE GAME WAS GENERATED AND PROGRAMMED BY*****************************************************
                                                               UMER FAROOQ (BCT-036)

********************************************************LETS START THE GAME AND HAVE SOME FUN*****************************************************

********************************************************YOU HAVE TO WIN THE GAME BUT YOU CAN'T****************************************************
''')

print("             PLEASE!! FOLLOW THE GIVEN INSTRUCTIONS:")

repeat = "Y"
while repeat == "Y":
    gamerunning = True
    # input the names
    while True:
        inp_name1 = input("Player1 enter your name :   \n -->  ").upper()
        if inp_name1.isalpha() is False:
            print("Enter letters only")
        else:
            print("Select the icon")
            break
    inp_name2 = "COMPUTER"
    # board variable
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # fuction to print the board

    def printboard(board):
        print("\t-------------------")
        print("\t |", board[0][0], " | ", board[0][1], " | ", board[0][2], "|")
        print("\t-|----|-----|----|-")
        print("\t |", board[1][0], " | ", board[1][1], " | ", board[1][2], "|")
        print("\t-|----|-----|----|-")
        print("\t |", board[2][0], " | ", board[2][1], " | ", board[2][2], "|")
        print("\t-------------------")

    # Choosing the icon
    while True:
        icon = input(
            inp_name1 + " please select from 'X' or 'O' :  \n -->  ").upper()
        if icon == "X":
            print("You have choosen X for your icon")
            symbol1 = "X"
            symbol2 = "O"
            break
        elif icon == "O":
            print("You have choosen O for your icon")
            symbol1 = "O"
            symbol2 = "X"
            break
        else:
            print(inp_name1, "have entered a wrong input, Enter again!!!")
    # loop for the toss
    while True:
        print("         GET READY FOR THE TOSS ---->>>")
        print()
        selection = input(
            inp_name1 + " Select heads or tails :   \n -->\t").upper()
        coin = ["HEADS", "TAILS"]
        toss = random.choice(coin)
        if selection == toss:
            print("CONGRATULATIONS", inp_name1, "Won the toss, The coin landed on",
                  toss, "\n You will go first")
            user_turn = True
            name1 = inp_name1
            name2 = "COMPUTER"
            break
        elif selection not in coin:
            print(inp_name1, "have entered a wrong input, Please input it again")
        else:
            print("Whoops", inp_name1, "lost the toss the coin landed on\n",
                  toss, inp_name2, " will go first")
            user_turn = False
            name1 = "COMPUTER"
            name2 = inp_name1
            break

    # Taking player 1 input

    def player_input1(board):
        while True:
            inp = int(
                input(inp_name1 + " Enter a number between 1 -9 ------>>>>  "))
            if inp > 0 and inp < 10:
                if inp == 1 and board[0][0] == " ":
                    board[0][0] = symbol1
                    return False
                if inp == 2 and board[0][1] == " ":
                    board[0][1] = symbol1
                    return False
                if inp == 3 and board[0][2] == " ":
                    board[0][2] = symbol1
                    return False
                if inp == 4 and board[1][0] == " ":
                    board[1][0] = symbol1
                    return False
                if inp == 5 and board[1][1] == " ":
                    board[1][1] = symbol1
                    return False
                if inp == 6 and board[1][2] == " ":
                    board[1][2] = symbol1
                    return False
                if inp == 7 and board[2][0] == " ":
                    board[2][0] = symbol1
                    return False
                if inp == 8 and board[2][1] == " ":
                    board[2][1] = symbol1
                    return False
                if inp == 9 and board[2][2] == " ":
                    board[2][2] = symbol1
                    return False
            else:
                print("It's a wrong input", inp_name1, "input it again!!!")

 # computer input

    def computermove(board):

        # checking if the center is free
        if board[1][1] == " ":
            board[1][1] = symbol2

# WIning moves of the computer
        # checking first row
        elif board[0][0] == board[0][1] == symbol2 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][0] == board[0][2] == symbol2 and board[0][1] == " ":
            board[0][1] = symbol2
        elif board[0][2] == board[0][1] == symbol2 and board[0][0] == " ":
            board[0][0] = symbol2

        # checking second row
        elif board[1][0] == board[1][1] == symbol2 and board[1][2] == " ":
            board[1][2] = symbol2
        elif board[1][1] == board[1][2] == symbol2 and board[1][0] == " ":
            board[1][0] = symbol2
        elif board[1][0] == board[1][2] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

        # checking third row
        elif board[2][0] == board[2][1] == symbol2 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[2][1] == board[2][2] == symbol2 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[2][0] == board[2][2] == symbol2 and board[2][1] == " ":
            board[2][1] = symbol2

        # checking first column
        elif board[0][0] == board[1][0] == symbol2 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[1][0] == board[2][0] == symbol2 and board[0][0] == " ":
            board[0][0] = symbol2
        elif board[0][0] == board[2][0] == symbol2 and board[1][0] == " ":
            board[1][0] = symbol2

        # checking second column
        elif board[0][1] == board[1][1] == symbol2 and board[2][1] == " ":
            board[2][1] = symbol2
        elif board[1][1] == board[2][1] == symbol2 and board[0][1] == " ":
            board[0][1] = symbol2
        elif board[0][1] == board[2][1] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

        # checking third column
        elif board[0][2] == board[1][2] == symbol2 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[1][2] == board[2][2] == symbol2 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][2] == board[2][2] == symbol2 and board[1][2] == " ":
            board[1][2] = symbol2

        # checking first diagonal
        elif board[0][0] == board[1][1] == symbol2 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[1][1] == board[2][2] == symbol2 and board[0][0] == " ":
            board[0][0] = symbol2
        elif board[0][0] == board[2][2] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

        # checking second diagonal
        elif board[0][2] == board[1][1] == symbol2 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[1][1] == board[2][0] == symbol2 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][2] == board[2][0] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

  # computer blocking the player moves

        # blocking first row
        elif board[0][0] == board[0][1] == symbol1 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][0] == board[0][2] == symbol1 and board[0][1] == " ":
            board[0][1] = symbol2
        elif board[0][2] == board[0][1] == symbol1 and board[0][0] == " ":
            board[0][0] = symbol2
        # blocking second row
        elif board[1][0] == board[1][1] == symbol1 and board[1][2] == " ":
            board[1][2] = symbol2
        elif board[1][1] == board[1][2] == symbol1 and board[1][0] == " ":
            board[1][0] = symbol2
        elif board[1][0] == board[1][2] == symbol1 and board[1][1] == " ":
            board[1][1] = symbol2

        # blocking third row
        elif board[2][0] == board[2][1] == symbol1 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[2][1] == board[2][2] == symbol1 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[2][0] == board[2][2] == symbol1 and board[2][1] == " ":
            board[2][1] = symbol2

        # blocking first column
        elif board[0][0] == board[1][0] == symbol1 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[1][0] == board[2][0] == symbol1 and board[0][0] == " ":
            board[0][0] = symbol2
        elif board[0][0] == board[2][0] == symbol1 and board[1][0] == " ":
            board[1][0] = symbol2

        # blocking second column
        elif board[0][1] == board[1][1] == symbol1 and board[2][1] == " ":
            board[2][1] = symbol2
        elif board[1][1] == board[2][1] == symbol1 and board[0][1] == " ":
            board[0][1] = symbol2
        elif board[0][1] == board[2][1] == symbol1 and board[1][1] == " ":
            board[1][1] = symbol2

        # blocking third column
        elif board[0][2] == board[1][2] == symbol1 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[1][2] == board[2][2] == symbol1 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][2] == board[2][2] == symbol1 and board[1][2] == " ":
            board[1][2] = symbol2

        # blocking first diagonal
        elif board[0][0] == board[1][1] == symbol1 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[1][1] == board[2][2] == symbol1 and board[0][0] == " ":
            board[0][0] = symbol2
        elif board[0][0] == board[2][2] == symbol1 and board[1][1] == " ":
            board[1][1] = symbol2

        # blocking second diagonal
        elif board[0][2] == board[1][1] == symbol1 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[1][1] == board[2][0] == symbol1 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][2] == board[2][0] == symbol1 and board[1][1] == " ":
            board[1][1] = symbol2

        # special moves
        elif board[0][0] == board[2][2] == symbol1 and board[1][1] == symbol2 and board[1][2] == " ":
            board[1][2] = symbol2
        elif board[0][0] == board[2][2] == symbol1 and board[1][1] == symbol2 and board[2][1] == " ":
            board[2][1] = symbol2
        elif board[0][2] == board[2][0] == symbol1 and board[1][1] == symbol2 and board[1][0] == " ":
            board[1][0] = symbol2
        elif board[0][2] == board[2][0] == symbol1 and board[1][1] == symbol2 and board[2][1] == " ":
            board[2][1] = symbol2
        elif board[1][1] == symbol1 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[0][1] == board[1][0] == symbol1 and board[1][1] == symbol2 and board[0][0] == " ":
            board[0][0] = symbol2
        elif board[2][1] == board[1][0] == symbol1 and board[1][1] == symbol2 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[0][1] == board[1][2] == symbol1 and board[1][1] == symbol2 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[1][2] == board[2][1] == symbol1 and board[1][1] == symbol2 and board[2][2] == " ":
            board[2][2] = symbol2
# again winning moves of the computer

        # checking first row
        elif board[0][0] == board[0][1] == symbol2 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][0] == board[0][2] == symbol2 and board[0][1] == " ":
            board[0][1] = symbol2
        elif board[0][2] == board[0][1] == symbol2 and board[0][0] == " ":
            board[0][0] = symbol2

        # checking second row
        elif board[1][0] == board[1][1] == symbol2 and board[1][2] == " ":
            board[1][2] = symbol2
        elif board[1][1] == board[1][2] == symbol2 and board[1][0] == " ":
            board[1][0] = symbol2
        elif board[1][0] == board[1][2] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

        # checking third row
        elif board[2][0] == board[2][1] == symbol2 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[2][1] == board[2][2] == symbol2 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[2][0] == board[2][2] and board[2][1] == " ":
            board[2][1] = symbol2

        # checking first column
        elif board[0][0] == board[1][0] == symbol2 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[1][0] == board[2][0] == symbol2 and board[0][0] == " ":
            board[0][0] = symbol2
        elif board[0][0] == board[2][0] == symbol2 and board[1][0] == " ":
            board[1][0] = symbol2

        # checking second column
        elif board[0][1] == board[1][1] == symbol2 and board[2][1] == " ":
            board[2][1] = symbol2
        elif board[1][1] == board[2][1] == symbol2 and board[0][1] == " ":
            board[0][1] = symbol2
        elif board[0][1] == board[2][1] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

        # checking third column
        elif board[0][2] == board[1][2] == symbol2 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[1][2] == board[2][2] == symbol2 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][2] == board[2][2] == symbol2 and board[1][2] == " ":
            board[1][2] = symbol2

        # checking first diagonal
        elif board[0][0] == board[1][1] == symbol2 and board[2][2] == " ":
            board[2][2] = symbol2
        elif board[1][1] == board[2][2] == symbol2 and board[0][0] == " ":
            board[0][0] = symbol2
        elif board[0][0] == board[2][2] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

        # checking second diagonal
        elif board[0][2] == board[1][1] == symbol2 and board[2][0] == " ":
            board[2][0] = symbol2
        elif board[1][1] == board[2][0] == symbol2 and board[0][2] == " ":
            board[0][2] = symbol2
        elif board[0][2] == board[2][0] == symbol2 and board[1][1] == " ":
            board[1][1] = symbol2

        # checking the rest edges
        elif board[0][0] == " ":
            board[0][0] = symbol2
        elif board[2][0] == " ":
            board[2][0] = symbol2
        elif board[2][2] == " ":
            board[2][2] = symbol2
        elif board[0][2] == " ":
            board[0][2] = symbol2

        # checking the restparts
        elif board[1][0] == " ":
            board[1][0] = symbol2
        elif board[2][1] == " ":
            board[2][1] = symbol2
        elif board[1][2] == " ":
            board[1][2] = symbol2
        elif board[0][1] == " ":
            board[0][1] = symbol2

    # checking who win

    def checkwin(board):
        global gamerunning

        if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
            if board[0][0] == board[0][1] == board[0][2] == symbol1:
                print("Congratulations", name1, "won!!")
                gamerunning = False
            else:
                print("Computer won")
                gamerunning = False
        elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
            if board[1][0] == board[1][1] == board[1][2] == symbol1:
                print("Congratulations", name1, "won!!")
                gamerunning = False
            else:
                print("Computer won!")
                gamerunning = False
        elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
            if board[2][0] == board[2][1] == board[2][1] == symbol1:
                print("Congratulations", name1, "won!!")
                gamerunning = False
            else:
                print("Computer Won!")
                gamerunning = False
        elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
            if board[0][0] == board[1][0] == board[2][0] == symbol1:
                print("Congratulations", name1, "Won!!")
                gamerunning = False
            else:
                print("Computer Won!")
                gamerunning = False
        elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
            if board[0][1] == board[1][1] == board[2][1] == symbol1:
                print("Congratulations", name1, "Won!!")
                gamerunning = False
            else:
                print("Computer Won!!")
                gamerunning = False
        elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
            if board[0][2] == board[1][2] == board[2][2] == symbol1:
                print("Congratulations", name1, "Won!!")
                gamerunning = False
            else:
                print("Computer Won!!")
                gamerunning = False
        elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            if board[0][0] == board[1][1] == board[2][2] == symbol1:
                print("Congratulations", name1, "Won!!")
                gamerunning = False
            else:
                print("Computer Won!!")
                gamerunning = False
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            if board[0][2] == board[1][1] == board[2][0] == symbol1:
                print("Congratulations", name1, "Won!!")
                gamerunning = False
            else:
                print("Computer Won!!")
                gamerunning = False
        elif board[0][0] in [symbol1, symbol2] and board[0][1] in [symbol1, symbol2] and board[0][2] in [symbol1, symbol2] and\
                board[1][0] in [symbol1, symbol2] and board[1][1] in [symbol1, symbol2] and board[1][2] in [symbol1, symbol2] and\
                board[2][0] in [symbol1, symbol2] and board[2][1] in [symbol1, symbol2] and board[2][2] in [symbol1, symbol2]:
            print("The game is a draw")
            gamerunning = False
# Main loop to run the game step by step
    while gamerunning:
        if user_turn:
            printboard(board)
            player_input1(board)
            printboard(board)
            checkwin(board)
            if gamerunning == False:
                break
            else:
                user_turn = False
        else:
            computermove(board)
            print("It's computer move!!")
            checkwin(board)
            if gamerunning == False:
                printboard(board)
                break
            else:
                user_turn = True
# loop to repeat the game
    repeat = input("Enter Y to play again and N to exit ------>>>>   ").upper()
    if repeat == "N":
        print("Thnaks for playing plz give us your feedback ")
        # getting user feedback
        input("Enter your feedback here :\n -->")
        print("Hope you have a good day,!!!")
        break
    elif repeat == "Y":
        repeat == "Y"
    else:
        print("Entered a wrong input,Plz enter it again")


"""
        THANKS FOR GOING THOROUGH I HOPE YOU GET THE BEST OF THE ALGORITHM POSSIBLE
        
"""
