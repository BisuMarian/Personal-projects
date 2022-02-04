import time

def drawGame(field):
    for line in range(5):
        if line % 2 == 0:
            practicalLine = int(line/2)
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = int(column/2)
                    if column != 4:
                        print(field[practicalColumn][practicalLine], end="")
                    else: print(field[practicalColumn][practicalLine])
                else: print("|", end="")
        else: print("-----")

Winner = 0
Player = 1
countMoves = 0
valoriPermise = [0,1,2]
PlayingField = [[" "," "," "],[" "," "," "],[" "," "," "]]

print("-----Tic-Tac-Toe----- \n")
print("How to play: To make a move, a player must insert first a column associated value and then a row associted value.")
print("The values are entered from the keyboard. Every entered value must be an integer and it must be between 0 and 2 \n")

drawGame(PlayingField)

while(True):
    print("Player", Player)
    Column = int(input("Column:\n"))
    Row = int(input("Row:\n"))
    try:
        if Column not in valoriPermise:
            raise ValueError("Input value error. The entered value was not equal to 0, 1 or 2.")
        if Row not in valoriPermise:
            raise ValueError("Input value error. The entered value was not equal to 0, 1 or 2.")
    except ValueError:
        while(True):
            if Column not in valoriPermise:
                print("The entered value cannnot be found in the permitted values list supported by the game. Please reassign the column value.")
                Column = int(input("Column:"))
            elif Row not in valoriPermise:
                print("The entered value cannnot be found in the permitted values list supported by the game. Please reassign the row value.")
                Row = int(input("Row:"))        
            else:
                break
    if Player == 1:

        if PlayingField[Column][Row] == " ":
            PlayingField[Column][Row] = "X"
            for i in range(3):
                if PlayingField[0][i] == "X" and PlayingField[1][i] == "X" and PlayingField[2][i] == "X":
                    drawGame(PlayingField)
                    print("Player 1 has won !")
                    Winner = 1
                    break
            
                elif PlayingField[i][0] == "X" and PlayingField[i][1] == "X" and PlayingField[i][2] == "X":
                    drawGame(PlayingField)
                    print("Player 1 has won !")
                    Winner = 1
                    break
            
            if PlayingField[0][0] == "X" and PlayingField[1][1] == "X" and PlayingField[2][2] == "X":
                drawGame(PlayingField)
                print("Player 1 has won !")
                break
            elif PlayingField[2][0] == "X" and PlayingField[1][1] == "X" and PlayingField[0][2] == "X":
                drawGame(PlayingField)
                print("Player 1 has won !")
                break
            else:  
                Player = 2
                countMoves += 1
    else:
        if PlayingField[Column][Row] == " ": 
            PlayingField[Column][Row] = "O"
            for i in range(3):
                if PlayingField[0][i] == "O" and PlayingField[1][i] == "O" and PlayingField[2][i] == "O":
                    drawGame(PlayingField)
                    print("Player 2 has won !")
                    Winner = 1
                    break
            
                elif PlayingField[i][0] == "O" and PlayingField[i][1] == "O" and PlayingField[i][2] == "O":
                    drawGame(PlayingField)
                    print("Player 2 has won !")
                    Winner = 1
                    break

            if PlayingField[0][0] == "O" and PlayingField[1][1] == "O" and PlayingField[2][2] == "O":
                drawGame(PlayingField)
                print("Player 2 has won !")
                break
            elif PlayingField[2][0] == "O" and PlayingField[1][1] == "O" and PlayingField[0][2] == "O":
                drawGame(PlayingField)
                print("Player 2 has won !")
                break
            else:  
                Player = 1
                countMoves += 1
    if Winner == 1:
        break
    
    if countMoves == 9:
        drawGame(PlayingField)
        print("TIE!")
        break

    drawGame(PlayingField)

time.sleep(5)