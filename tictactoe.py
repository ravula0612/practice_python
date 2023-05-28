board = ["_","_","_",
         "_","_","_",
         "_","_","_"]
current_player = "X"
winner = None
gameRunning = True

# printing the game board
def printBoard(board):
    print(board[0] +" | " +board[1] +" | "+ board[2])
    print("------------------------------")
    print(board[3] +" | " +board[4] +" | "+ board[5])
    print("------------------------------")
    print(board[6] +" | " +board[7] +" | "+ board[8])
# take player input

def playerInput(board):
    inp = int(input("enter a number 1-9: "))
    if inp>=1 and inp <=9 and board[inp-1]=="_":
        board[inp-1] = current_player
    else:
        print("Opps player is already in that spot! ")

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2]  and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!="_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!="_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!="_":
        winner = board[2]
        return True
def diagonal(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0]!="_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!="_":
        winner = board[2]
        return True
    

def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("it's a tie")
        gameRunning = False

def switchplayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def checkwin():
    if diagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"the winner {winner}")

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkwin()
    checkTie(board)
    switchplayer()


# check for win  or tie


# switch player 

# check for win or tie 

# repeat