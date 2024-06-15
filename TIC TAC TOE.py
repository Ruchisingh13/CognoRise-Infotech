def sum(a, b, c):
    return a + b + c

def printBoard(xTurn, zTurn):
    chance = []
    for i in range(9):
        if xTurn[i]:
            chance.append('X')
        elif zTurn[i]:
            chance.append('O')
        else:
            chance.append(str(i))
    
    print(f"{chance[0]} | {chance[1]} | {chance[2]}")
    print("--|---|--")
    print(f"{chance[3]} | {chance[4]} | {chance[5]}")
    print("--|---|--")
    print(f"{chance[6]} | {chance[7]} | {chance[8]}")

def checkwin(xTurn, zTurn):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    for win in wins:
        if sum(xTurn[win[0]], xTurn[win[1]], xTurn[win[2]]) == 3:
            print("X won the match!")
            return 1
        if sum(zTurn[win[0]], zTurn[win[1]], zTurn[win[2]]) == 3:
            print("O won the match!")
            return 0
    return -1

if __name__ == "__main__":
    xTurn = [0] * 9
    zTurn = [0] * 9
    turn = 1  # 1 for X's turn, 0 for O's turn
    print("Welcome to Tic Tac Toe")

    while True:
        printBoard(xTurn, zTurn)
        if turn == 1:
            print("X's turn")
        else:
            print("O's turn")
        
        try:
            value = int(input("Please enter a value (0-8): "))
            if value < 0 or value > 8:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue
            if xTurn[value] or zTurn[value]:
                print("Cell already occupied. Choose another cell.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if turn == 1:
            xTurn[value] = 1
        else:
            zTurn[value] = 1

        cwin = checkwin(xTurn, zTurn)
        if cwin != -1:
            printBoard(xTurn, zTurn)
            print("Match over")
            break
        
        turn = 1 - turn
        
        