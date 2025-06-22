
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
    
    for row in gameBoard:
       playerCountRow = row.count(player)   
       if playerCountRow==len(row):
          print("palyer", player," win the gmae by HR.")
          return(True)

    return(False)

# Check Win Vertical
def checkVWim(gameBoard, player):
    '''
    Check if the game met the condiotn for a vertical victory.
    - Input values
    - game board 3x3 2D matrix
    - player either 1 or 2
    - Output value
    - winner (bool)
    
    Comment: Should remove Hardcoded values
    '''
    
    for col in range(len(gameBoard)):
        if gameBoard[0][col] == player and gameBoard[1][col] == player and gameBoard[2][col] == player:
            print("palyer", player," win the gmae by VR.")
            return(True)

    return(False)

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

    if gameBoard[0][0] == player and gameBoard[1][1] == player and gameBoard[2][2] == player:
        print("player", player," win the gmae by Stright Diagonal.")
        return(True)    
    return(False)

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

    if gameBoard[0][2] == player and gameBoard[1][1] == player and gameBoard[2][0] == player:
        print("player", player," win the gmae by Reverse Diagonal.")
        return(True)
    
    return(False)

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

def checkGameStatus(gameBoard,player):
    '''
    Check game status, return True if final state.
    Return also the type of final state:
    - H Horizontal victory
    - V Vertical victory
    - D1 and D2 strignt or reverse diagonal
    - Draw
    Input
    - game board 3x3 2D matrix
    - palyer
    output
    - True / False - Final state
    - Player
    - Type of final state 
    
    Comment: Uses already developed funcitons
    '''
    
    if checkHWim(gameBoard,player):
        return(True, player, 'H')
    elif checkVWim(gameBoard,player):
        return(True, player, 'V')
    elif checkD1Win(gameBoard,player):
        return(True, player, 'D1')
    elif checkD2Win(gameBoard,player):
        return(True, player, 'D2')
    elif checkDraw(gameBoard):
        return(True, player, 'Draw')
    
    return(False)

def updateStats(gameStats, player, column_choice, row_choice, gameTurn):
    print(player, column_choice, row_choice)
    gameStats[gameTurn-1]=(str(column_choice) + ':' + str(row_choice))
    #list(gameStats).append([column_choice, row_choice])
    print(gameStats)
    
    return(gameStats)

def interactiveMove(player):
    cellCheck = True
    
    while cellCheck:    
        x = input("What column do you want to play? (0, 1, 2): ")
        y = input("What row do you want to play? (0, 1, 2): ")

        if gameBoard[int(x)][int(y)] == 0:
            gameBoard[int(x)][int(y)] = player
            #updateStats(gameStats, player, x, y, gameTurn)
            cellCheck = False
        else:
            print("cell already selected, pls. chose a different cell")
    
    return(x,y)


def checkValidMove(x, y, gameBoard):
     
    if gameBoard[int(x)][int(y)] == 0:
            return(True)
            
    return(False)



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

def game(gameStatsus, gameTurn, gameBoard, player, winner, gameStats):
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

#game(gameStatsus, gameTurn, gameBoard, player, winner, gameStats)