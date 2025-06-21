
#Initialize

# Need to create logic for 1 or 2 players
# Need to create the logic for X or Y player
# Need to create the logic for move first or last

import itertools
import csv
import pandas as pd

gameBoard = [
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
gameStats = ['','','','','','','','','','']          # Document move for each turn
gameStatsus = True                                   # Is the game still running?
gameTurn = 0                                        # The number of the turn of the game
gameDraw = False                                    # Game drav

# Check Win Horizonta
def checkHWim(gameBoard, player):
    '''
    Check if the game met the condiotn for a horizontal victory.
    input values
    - game board 3x3 2D matrix
    - player either 1 or 2
    output
    - winner (bool)
    '''
    global winner

    for row in gameBoard:
       list(row).count(player)
       
       if list(row).count(player)==list(row).__len__():
          winner=True
          print("palyer", player," win the gmae by HR.")

    return(winner)

# Check Win Vertical
def checkVWim(gameBoard, player):
    '''
    Check if the game met the condiotn for a vertical victory.
    input values
    - game board 3x3 2D matrix
    - player either 1 or 2
    output
    - winner (bool)
    
    Comment: Should remove Hardcoded values
    '''
    global winner

    for col in range(list(gameBoard).__len__()):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col] != 0:
            winner=True
            print("palyer", player," win the gmae by VR.")

    return(winner)

# Check D1
def checkD1Win(gameBoard, player):
    '''
    Check if the game met the condiotn for a stright diagonal vicotry.
    input values
    - game board 3x3 2D matrix
    - player either 1 or 2
    output
    - winner (bool)
    
    Comment: Should remove Hardcoded values
    '''
    global winner

    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] != 0:
        winner=True
        print("palyer", player," win the gmae by Stright Diagonal.")
            
    return(winner)

# Check D2
def checkD2Win(gameBoard, player):
    '''
    Check if the game met the condiotn for a reverse diagonal vicotry.
    input values
    - game board 3x3 2D matrix
    - player either 1 or 2
    output
    - winner (bool)
    
    Comment: Should remove Hardcoded values
    '''
    global winner

    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] != 0:
        winner=True
        print("palyer", player," win the gmae by Reverse Diagonal.")
        
    return(winner)

# Check if the game draw
def checkDraw(gameBoard):

    '''
    Check if the game met the condiotn for a draw.
    input values
    - game board 3x3 2D matrix
    output
    - gameDraw (bool)
    
    Comment: Should remove Hardcoded values
    '''
    gaemDraw = False
    id=0
    for col in range(list(gameBoard).__len__()):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col] != 0:
            id=id+1
        
    if id==3:
        print("Game draw")
        gaemDraw = True
            
    return(gaemDraw)

def updateStats(gameStats, player, column_choice, row_choice, gameTurn):
    print(player, column_choice, row_choice)
    gameStats[gameTurn-1]=(str(column_choice) + ':' + str(row_choice))
    #list(gameStats).append([column_choice, row_choice])
    print(gameStats)
    
    return(gameStats)


# Update Bard Game
def updateBoardGame(gameBoard, player, gameTurn):
    
    cellCheck = True
    
    for row in gameBoard:
        print(row)           # Print the game board
    
    while cellCheck:    
        column_choice = input("What column do you want to play? (0, 1, 2): ")
        row_choice = input("What row do you want to play? (0, 1, 2): ")

        if gameBoard[int(row_choice)][int(column_choice)] == 0:
            gameBoard[int(row_choice)][int(column_choice)] = player
            updateStats(gameStats, player, column_choice, row_choice, gameTurn)
            cellCheck = False
        else:
            print("cell already selected, pls. chose a different cell")
            
    return(gameBoard)

def writeGameStats(gameStatss):
    print(str(gameStatss))
    with open('C:/Temp/EITCA_AI/gameStatss.csv', 'a') as f:
        f.write("\n" + str(gameStats))


while gameStatsus:
    
    gameTurn = gameTurn + 1    # Count the game turn
    
    print('Turn ', gameTurn, 'Player ', player)

    gameBoard = updateBoardGame(gameBoard, player, gameTurn)
     
    winner = checkHWim(gameBoard, player)

    winner = checkVWim(gameBoard, player)

    winner = checkD1Win(gameBoard, player)

    winner = checkD2Win(gameBoard, player)
    
    gameDraw = checkDraw(gameBoard) 
        
    if winner:
        gameStatsus = False
        gameStats[9]=(gameTurn, player)
        
    if gameDraw:
        gameStatsus = False
        gameStats[9]=(gameTurn, 0)
    
    player = players.__next__()

# print(gameStats)
writeGameStats(gameStats)
print('End Game')