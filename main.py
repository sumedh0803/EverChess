# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:17:46 2020

@author: sumed
"""
        
def beginGame():
    #initializing the last player to [-1,-1], which will be updated when a player makes a move
    lastPlayer = [-1,-1]
    printBoard(board)
    currentPlayer = 0 # 0 == white, 1 == black
    over,status = isGameOver() 
    while(not over):
        currentPlayerColor = players[currentPlayer]
        if currentPlayer == 0:
            print("Its White's turn")
        else:
            print("Its Black's turn")
            
        #Taking coordinates of a pawn from the user    
        print("Enter your pawn's current position as: y,x")
        fromIp = input().split(",") 
        if len(fromIp) == 2:
            fromY,fromX = fromIp[0],fromIp[1]
            fromY,fromX = int(fromY),int(fromX)
        else:
            print("invaid coordinates. Try Again")
            continue        
        
        #checking if the coordinates belong to a valid pawn
        pawnValid,pawnMsg = validPawn(currentPlayerColor,lastPlayer,fromX,fromY)
        if pawnValid:
            print("Enter your pawn's new position as: y,x")
            #Taking coordinates of the position where the pawn is supposed to move to 
            toIp = input().split(",") 
            if len(toIp) == 2:
                toY,toX = toIp[0],toIp[1]
                toY,toX = int(toY),int(toX)
            else:
                 print("invaid coordinates. Try Again")
                 continue  
             
            #checking if the coordinates belong to a valid position
            moveValid,moveMsg,mode = validMove(currentPlayerColor,fromX,fromY,toX,toY)
            if moveValid:
               #if mode == "move", we move the pawn 1 position ahead and play control goes to opponent
               if mode == "move":
                   board[fromY][fromX] = "_"
                   board[toY][toX] = currentPlayerColor   
                   currentPlayer = 1 - currentPlayer
                   
               else:
                   #the pawn attacks the opponent, and the play control remains with the current player
                   board[fromY][fromX] = "_"
                   board[toY][toX] = currentPlayerColor
               
               lastPlayer = [toY,toX]
            else:
                print(moveMsg)
            
        else:
            print(pawnMsg)
        
        printBoard(board)
        over,status = isGameOver() 
    print (status)

#Checking if any pawn has a valid move left, or if any side is winning       
def isGameOver():
    #if we have a white pawn in opponent side
    if "W" in board[7]:
        return True,"White wins!"
    #if we have a black pawn in opponent side
    if "B" in board[0]:
        return True,"Black wins!"
    #checking if any pawn as a valid move left
    for i in range(h):
        for j in range(w):
            if board[i][j] == "W":
                valid,msg,mode = validMove("W",j,i,j,i+1) #checking if pawn can go ahead
                if valid:
                    return False,""
                valid,msg,mode = validMove("W",j,i,j+1,i+1) #checking if pawn can attack
                if valid:
                    return False,""
                valid,msg,mode = validMove("W",j,i,j-1,i+1) #checking if pawn can attack
                if valid:
                    return False,""
            elif board[i][j] == "B":
                valid,msg,mode = validMove("B",j,i,j,i-1) #checking if pawn can go ahead
                if valid:
                    return False,""
                valid,msg,mode = validMove("B",j,i,j+1,i-1) #checking if pawn can attack
                if valid:
                    return False,""
                valid,msg,mode = validMove("B",j,i,j-1,i-1) #checking if pawn can attack
                if valid:
                    return False,""
    return True, "Game Tied!"
        

#printing the chess board
def printBoard(board):
    colId = "\t"
    for i in range(w): colId += str(i) + "\t" 
    print(colId)
    for i in range(h):
        rowId = str(i)
        temp = ""
        for j in range(w):
            temp += board[i][j] + "\t"
        rowId += "\t" +  temp
        print(rowId)
        
#checking if we selected a valid pawn with respect to color and position            
def validPawn(currentPlayerColor,lastPlayer,fromX,fromY):
    if 0 <= fromX < w and 0 <= fromY < h:
        #position is valid
        if board[fromY][fromX] == currentPlayerColor:
            #correct pawn selected
            if lastPlayer == [fromY,fromX]:
                return False,"Cannot play the same pawn twice in a row"
            return True,"valid"
        else:
            return False,"Invalid pawn. Please check your position"
    else:
            #Position out of bounds
            return False,"invalid position. please check again"
 
#checking if the move to be performed is valid with respect to pawn's position and opponent's position
def validMove(currentPlayerColor,fromX,fromY,toX,toY):
    if currentPlayerColor == "W":
        direction = "f"
    else:
        direction = "b"
        
    if 0 <= toX < w and 0 <= toY < h:
        #position is valid
        if fromY == toY:
            return False, "Cannot move sideways",""
        elif fromX == toX:
            #going straight ahead. check if no pawn is there in front:
            if abs(fromY - toY) == 1: 
                #moved only 1 position
                if (direction == "f" and fromY < toY) or (direction == "b" and  toY < fromY):
                    if board[toY][toX] == "_":
                        return True,"valid","move"
                    else:
                        return False, "Position is occupied by a pawn",""
                else:
                    return False,"Cannot move backwards",""
            else:
                #moved more than 1 position:
                return False, "Cannot move more than 1 position",""
        elif abs(fromX - toX) == 1 and abs(fromY - toY) == 1:
            if (direction == "f" and fromY < toY) or (direction == "b" and toY < fromY):
                #attacking
                if board[toY][toX] == "_":
                    return False,"Cannot attack on an empty spot",""
                elif board[toY][toX] == currentPlayerColor:
                    return False,"Cannot attack on your own pawn",""
                else:
                    #valid attacking move
                    return True,"valid","attack"
            else:
                return False,"Cannot move backwards","" 
        else:
            return False,"Cannot jump more than 1 position",""
    else:
        return False, "Invalid position",""
        


if __name__ == "__main__": 
    #Initializing the EverChess board
    h = 8
    w = 8
    board = [["*" for i in range(w)] for i in range(h)]
    for i in range(h):
        if i == 1:
            board[i] = ["W" for j in range(w)]
        elif i == 6:
            board[i] = ["B" for j in range(w)]
    players = ["W","B"]    
    beginGame()
                    
                     
                
                
                
                
                
        
        
        