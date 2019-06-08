''' This Module contains functions for the game of Tic Tac Toe'''
from random import randint
# for displaying the board
def printBoard(board):
    print("    |   |   ")
    print("  "+board[7]+" | "+board[8]+" | "+board[9] )
    print("    |   |   ")
    print("-------------")
    print("    |   |   ")
    print("  "+board[4]+" | "+board[5]+" | "+board[6] )
    print("    |   |   ")
    print("-------------")
    print("    |   |   ")
    print("  "+board[1]+" | "+board[2]+" | "+board[3] )
    print("    |   |   ")
    return

# for choosing the team 'X' or 'O'
def chooseTeam(player):
    choice = ''
    print("What team would you like to be", player, ": X or O")
    while not(choice == 'X' or choice == 'O'):
        choice = input().upper()
    if choice == 'O':
        teams = ('X', 'O') # where 'X' will be computer
    elif choice == 'X':
        teams = ('O', 'X') # where 'O' will be computer
    return teams

# for choosing the turn
def chooseTurn(player1, player2):
    if randint(1,2) == 1:
        return player1
    else:
        return player2
# for taking player input
def inputPlayer(board, player, team, moveslist):
    ch_frm = (1,2,3,4,5,6,7,8,9)
    pos = int(input("Your move "+player+" (1,9):"))
    # to check if move is valid and in
    if pos not in ch_frm:
        print("Move not available")
        inputPlayer(board, player, team, moveslist)
    # check if move is valid or not
    elif pos in moveslist:
        print("Move not valid !")
        inputPlayer(board, player, team, moveslist)
    # input move in board
    else:
        board[pos] = team # chosen team of player i.e. 'X' or 'O'
        moveslist.append(pos)
    return board

# Win conditions
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonalv