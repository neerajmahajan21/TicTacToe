from module import *

# Main Game
print("Welcome to the game of Tic Tac Toe")
print("Instructions:\n 1. Do not make move on same boxes\n 2. Use the format of NumPad as board")
print("\n")
# default values
board = ["null", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Player naming and choosing turn
players = []    # Player names
for i in range(2):
    player = input("Enter your name Player"+str(i+1)+": ")
    player = player[0].upper() + player[1:]
    players.append(player)
player1 = players[0]
player2 = players[1]
temp = chooseTurn(player1, player2)

# choosing turn
print(temp,"will go first")
print()
teams = chooseTeam(player2)
team1 = teams[0] # team Player1
team2 = teams[1] # team Player2
print()
print(player1,"is",team1)
print(player2,"is",team2)
print()
turn = temp

# moves already made
moveslist = []

# Start game
running = True
# print Empty board
printBoard(board)

while running and len(moveslist)<9:
    if turn == player1:
        printBoard(inputPlayer(board, player1, team1, moveslist))
        turn = player2          # for changing turn
        if isWinner(board,team1):
            print(player1,"is the winner!\n")
            running = False
            break
    elif turn == player2:
        printBoard(inputPlayer(board, player2, team2, moveslist))
        turn = player1          # for changing turn
        if isWinner(board,team2):
            print(player2,"is the winnner!\n")
            running = False
            break
if running:
    print("Sorry! No one is Winner\n")
input("Press Enter to exit.")