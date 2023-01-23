import random
import time
board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]]
class style:
    BOLD = "\033[1m"
    END = "\033[0m"
    BLACK = "\033[30m"
    RED =  "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    STRIKETHROUGH = "\033[9m"

board_predict = board
TTT_EMPTY = 0
TTT_X = 1
TTT_O = 2
recents = []
def place(xy, row, col):
    if board[row][col] == 0:
        board[row][col] = xy
        if len(recents) > 1:
            recents.append((board[row],board[col]))
            recents.remove(recents[0])
        else: 
            recents.append((board[row],board[col]))
        return True
    else:
        return False
class Player:
    totalturns = 0
    symbol = TTT_EMPTY
    def __init__(self, sym):
        self.symbol = sym
    def turn(self):
        a = 0
        while a == 0:
            pos = self.get_move_pos()
            if place(self.symbol, pos[0], pos[1]):
                a = 1
                break
            else:
                print("This tile is already taken.")
            
class Computer(Player):
    color = style.BLUE
    
    def get_move_pos(self):
        possiblemoves = []
        movevalues = []
        global board_predict
        for x in range(3):
            for y in range(3):
                print(board[x][y])
                if board[x][y] == 0:
                    possiblemoves.append((x, y))
        print(board)
        if len(possiblemoves) < 7:
            for x in possiblemoves:
                print(x)
                board_predict = board.copy()
                board_predict[x[0]][x[1]] = 2
                if wincheck(TTT_O, True):
                    #if the predicted board is winning then it has a higher value than if it isn't
                    movevalues.append(1)
                else:
                    movevalues.append(0)
                board_predict.clear()
            print(movevalues)
            print(possiblemoves)
            pos = possiblemoves[movevalues.index(max(movevalues))]
        else:
            if (0,1) in possiblemoves:
                pos = (0,1)
            if (1,0) in possiblemoves:
                pos = (1,0)
            if (2,1) in possiblemoves:
                pos = (2,1)
            if (1,2) in possiblemoves:
                pos = (1,2)
        #prefers edge tiles over any others
        return pos

    
    
class Human(Player):
    color = style.RED
    def get_move_pos(self):
        valid = False
        while not valid:
            move_str = input("Where would you like to move? ")
            if move_str == "ex":
                exit()
            pos = move_str.split(",")
            
            if len(pos) != 2:
                print("Please enter a valid position.")
                continue
            for element in pos:
                if element == "1" or element == "2" or element == "3":
                    valid = True
                else:
                    print("Please enter a valid position.")
                    break
        for i in range(2):
            pos[i] = int(pos[i])-1
        return pos    
player = Human(TTT_X)
computer = Computer(TTT_O)

def print_board(player):
    
        
        
    for i in range(3):
        for x in range(3):
            prefix = ""
            if (i, x) in winseq:
                prefix = style.STRIKETHROUGH + player.color
            elif (board[i], board[x]) in recents:
                prefix = style.BOLD
            if board[i][x] == 0:
                print(prefix  + "." + style.END, end="")
            if board[i][x] == 1:
                print(prefix + style.RED + "X" + style.END, end = "")
            if board[i][x] == 2:
                print(prefix + style.BLUE + "O" + style.END, end = "")
            if x != 3:
                print(prefix + " " + style.END, end="")
        print()


def run_game():
  while True:
    if wincheck(TTT_O, False):
        print("You lose.")
        print_board(Computer)
        exit()
    elif player.totalturns > 8:
        print("Draw.")
    player.turn()
    print_board(None)
    player.totalturns += 1
    if wincheck(TTT_X, False):
        print("Congratulations! You Win!")
        print_board(Human)
        exit()
    elif player.totalturns > 8:
        print("Draw.")
        exit()
    time.sleep(0.5)
    print("_____")
    computer.turn()
    print_board(None)
    print(board)
    player.totalturns += 1
    

winseq = []
def wincheck(symbol, predict):
    if wincheck_row(symbol, predict) or wincheck_column(symbol, predict) or wincheck_diag_1(symbol, predict) or wincheck_diag_2(symbol, predict):
        return True
    else:
        return False
def wincheck_row(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict.copy()
    else:
        boardno = board.copy()
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    for i in range(3):
        if (boardno[i][0] == boardno[i][1] == boardno[i][2]) and (boardno[i][0] == symbol):
            winseq = [(i, 0), (i, 1), (i, 2)]
            return True
def wincheck_column(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict
    else:
        boardno = board
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    for i in range(3):    
        if (boardno[0][i] == boardno[1][i] == boardno[2][i]) and (boardno[0][i] == symbol):
            winseq = [(0, i), (1, i), (2, i)]
            return True
def wincheck_diag_1(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict
    else:
        boardno = board
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    if (boardno[0][0] == boardno[1][1] == boardno[2][2]) and (boardno[0][0] == symbol):
        winseq = [(0, 0), (1, 1), (2, 2)]
        return True
def wincheck_diag_2(symbol, predict):
    global winseq
    if predict:
        boardno = board_predict
    else:
        boardno = board
    #Checks whether the wincheck is a normal wincheck or tied to the computer algo
    if (boardno[2][0] == boardno[1][1] == boardno[0][2]) and (boardno[2][0] == symbol):
        winseq = [(2, 0), (1, 1), (0, 2)]
        return True





run_game()
