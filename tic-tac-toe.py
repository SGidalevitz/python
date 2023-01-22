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
        while True:
            pos = self.get_move_pos()
            if place(self.symbol, pos[0], pos[1]):
                break
            else:
                print("This tile is already taken.")
            
class Computer(Player):
    color = style.BLUE
    def get_move_pos(self):
        moves = []
        randmoves = []
        for x in range(3):
            for y in range(3):
                if board[x][y] == 0:
                    moves.append((x, y))
        randmoves = moves[random.randrange(len(moves)-1)]
        return randmoves
    
    
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
    if wincheck(TTT_O):
        print("You lose.")
        print_board(Computer)
        exit()
    elif player.totalturns > 8:
        print("Draw.")
    player.turn()
    print_board(None)
    player.totalturns += 1
    if wincheck(TTT_X):
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
    player.totalturns += 1
    

winseq = []
def wincheck(symbol):
    if wincheck_row(symbol) or wincheck_column(symbol) or wincheck_diag_1(symbol) or wincheck_diag_2(symbol):
        return True
def wincheck_row(symbol):
    global winseq
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] == symbol:
            winseq = [(i, 0), (i, 1), (i, 2)]
            return True
def wincheck_column(symbol):
    global winseq
    for i in range(3):    
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] == symbol:
            winseq = [(0, i), (1, i), (2, i)]
            return True
def wincheck_diag_1(symbol):
    global winseq
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == symbol:
        winseq = [(0, 0), (1, 1), (2, 2)]
        return True
def wincheck_diag_2(symbol):
    global winseq
    if board[2][0] == board[1][1] == board[0][2] and board[2][0]== symbol:
        winseq = [(2, 0), (1, 1), (0, 2)]
        return True





run_game()
