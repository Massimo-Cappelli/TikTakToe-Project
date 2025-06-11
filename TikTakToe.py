
#Initialize
import itertools

game_board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

playersNumber = (1,2)
players = itertools.cycle(playersNumber)            # Array with the player number
player = players.__next__()                         # Active player
winner = False                                      # Winning criteria has been met
round = 0                                           # Round number
x = 0                                               # X coordinate of a placement
y = 0                                               # Y coordinate of a placement
gamestat = []
gameStatus = True                                   # Is the game still running?
gameTurn = 0                                        # The number of the turn of the game

# Check Win Horizonta
def Check_H_wim(game_board, player, winner):
    
    for row in game_board:
       list(row).count(player)
       
       if list(row).count(player)==list(row).__len__():
          winner=True
          print("palyer", player," win the gmae by HR.")

    return(winner)

# Check Win Vertical
def Check_V_wim(game_board, player, winner):

    for col in range(list(game_board).__len__()):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != 0:
            winner=True
            print("palyer", player," win the gmae by VR.")

    return(winner)

# Check D1
def Check_D1_win(game_board, player, winner):

    if game_board[0][0] == game_board[1][1] == game_board[2][2] != 0:
        winner=True
        print("palyer", player," win the gmae by Stright Diagonal.")
            
    return(winner)

# Check D1
def Check_D2_win(game_board, player, winner):
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != 0:
        winner=True
        print("palyer", player," win the gmae by Reverse Diagonal.")
        
    return(winner)

# Update Bard Game
def UpdateBoardGame(player, game_board):
    column_choice = input("What column do you want to play? (0, 1, 2): ") 
    
    row_choice = input("What row do you want to play? (0, 1, 2): ")
    
    if game_board[int(column_choice)][int(row_choice)] not in (1,2):
        game_board[int(column_choice)][int(row_choice)] = player

    return(game_board)


while gameStatus:
    gameTurn = gameTurn + 1    # Count the game turn
    print(winner)

    print("Turn of the player ", player, " turn ", gameTurn)    # Print general information
    
    for row in game_board:
        print(row)           # Print the game board

    game_board = UpdateBoardGame(player, game_board)
    
    winner = Check_H_wim(game_board, player, winner)

    winner = Check_V_wim(game_board, player, winner)

    winner = Check_D1_win(game_board, player, winner)

    winner = Check_D2_win(game_board, player, winner)
        
    if winner:
        gameStatus = False

    player = players.__next__()

print('End Game')
