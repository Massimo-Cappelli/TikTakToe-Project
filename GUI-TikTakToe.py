
#IMPORTING LIBRARIES
import itertools
import csv
import pandas as pd
import tkinter as tk    # Library for GUI
from tkinter import font

# INIZIALIZING VARIABLES
gameBoard = [[0,0,0],[0,0,0],[0,0,0]]              # GAME BOARD MATRIX
playersNumber = (1,2)
players = itertools.cycle(playersNumber)            # Array with the player number
player = players.__next__()                         # Active player
winner = False                                      # Winning criteria has been met
round = 0                                           # Round number
gameStats = ['','','','','','','','','','']
gameStatsus = True                                   # Is the game still running?
gameTurn = 0                                        # The number of the turn of the game
gameDraw = False

# Creating the class for the board game
class TicTacToeBoard(tk.Tk):
    def __init__(self, screenName = 'Tic Tac Toe', baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('Tic Tac Toe - GAME')
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=1,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

def main():
    """Create the game's board and run its main loop."""
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
'''
# Check Win Horizonta
def checkHWim(gameBoard, player, winner):
    
    for row in gameBoard:
       list(row).count(player)
       
       if list(row).count(player)==list(row).__len__():
          winner=True
          print("palyer", player," win the gmae by HR.")

    return(winner)

# Check Win Vertical
def checkVWim(gameBoard, player, winner):

    for col in range(list(gameBoard).__len__()):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col] != 0:
            winner=True
            print("palyer", player," win the gmae by VR.")

    return(winner)

# Check D1
def checkD1Win(gameBoard, player, winner):

    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] != 0:
        winner=True
        print("palyer", player," win the gmae by Stright Diagonal.")
            
    return(winner)

# Check D1
def checkD2Win(gameBoard, player, winner):
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] != 0:
        winner=True
        print("palyer", player," win the gmae by Reverse Diagonal.")
        
    return(winner)


def checkDraw(gameBoard):
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
     
    winner = checkHWim(gameBoard, player, winner)

    winner = checkVWim(gameBoard, player, winner)

    winner = checkD1Win(gameBoard, player, winner)

    winner = checkD2Win(gameBoard, player, winner)
    
    gameDraw = checkDraw(gameBoard) 
        
    if winner:
        gameStatsus = False
        gameStats[9]=(str(gameTurn)+':'+str(player))
        
    if gameDraw:
        gameStatsus = False
        gameStats[9]=(str(gameTurn)+':'+'0')
    
    player = players.__next__()

# print(gameStats)
writeGameStats(gameStats)
print('End Game')

'''