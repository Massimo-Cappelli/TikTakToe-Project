import itertools
import TikTakToe as ttt
import copy


# Varables
gameBoard = [
    [1,2,1],
    [1,2,2],
    [2,1,0]
]
player = 1
PossibleMoves = []

def checkPossibleMoves(gameBoard):
    possibleMoves=[]
    for x, row in enumerate(gameBoard):
        for y, col in enumerate(row):
            if gameBoard[x][y] == 0:
                possibleMoves.append((x,y))

    return(possibleMoves)    


def selectPossibleMoves(gameBoard, player):
    '''
    Read the possible move file.
    fro each possible move update the game board
    check end game condition.
    If win socre +1.
    If lose score -1.
    If draw score 0.

    '''
    winner=None
    possibleMoves = checkPossibleMoves(gameBoard)
    #print(possibleMoves)
    
    for move in possibleMoves:
        #print(move)
        gameBoard1 = copy.deepcopy(gameBoard)
        gameBoard1[move[0]][move[1]]=player

        if ttt.checkVWim(gameBoard1,player):
            print('V', move, gameBoard1, player)
            winner=player
                   
        elif ttt.checkHWim(gameBoard1,player):
            print('H', move, gameBoard1, player)
            winner=player
        
        elif ttt.checkD1Win(gameBoard1,player):
            print('D1', move, gameBoard1, player)
            winner=player

        elif ttt.checkD2Win(gameBoard1,player):
            print('D2', move, gameBoard1, player)
            winner=player

        if winner is None:
            print('Game Draw', move, gameBoard1, player)
            ttt.checkDraw(gameBoard1)
            winner=0

    if winner == 1:
        score=100
    elif winner == 2:
        score=-100
    elif winner ==0:
        score=0

    return(score)

def checkGameStatus(gameBoard1, player):

    if ttt.checkVWim(gameBoard1,player):
            print('V', move, gameBoard1, player)
            winner=player
                   
    elif ttt.checkHWim(gameBoard1,player):
        print('H', move, gameBoard1, player)
        winner=player
        
    elif ttt.checkD1Win(gameBoard1,player):
        print('D1', move, gameBoard1, player)
        winner=player

    elif ttt.checkD2Win(gameBoard1,player):
        print('D2', move, gameBoard1, player)
        winner=player

    if winner is None:
        print('Game Draw', move, gameBoard1, player)
        ttt.checkDraw(gameBoard1)
        winner=0

    if winner == 1:
        score=100
    elif winner == 2:
        score=-100
    elif winner ==0:
        score=0

    return(score)

print(checkPossibleMoves(gameBoard))
selectPossibleMoves(gameBoard, player)