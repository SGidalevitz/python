import random
import time
board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]]
class style:
   BOLD = '\033[1m'
   END = '\033[0m'


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

def print_board():
    for i in range(3):
        for x in range(3):
            if board[i][x] == 0:
                print(".", end="")
            if board[i][x] == 1:
                if (board[i],board[x]) in recents:
                    print(style.BOLD + "X" + style.END, end="")
                else:
                    print("X", end = "")
            if board[i][x] == 2:
                if (board[i],board[x]) in recents:
                    print(style.BOLD + "O" + style.END, end="")
                else:
                    print("O", end = "")
            print(" ", end="")
        print()

def run_game():
  while True:
    if wincheck(TTT_O):
        print("You lose.")
        exit()
    elif player.totalturns > 8:
        print("Draw.")
    player.turn()
    print_board()
    player.totalturns += 1
    if wincheck(TTT_X):
        print("Congratulations! You Win!")
        exit()
    elif player.totalturns > 8:
        print("Draw.")
        exit()
    time.sleep(0.5)
    print("_____")
    computer.turn()
    print_board()
    player.totalturns += 1
    

def wincheck(symbol):
    if wincheck_row(symbol) or wincheck_column(symbol) or wincheck_diag_1(symbol) or wincheck_diag_2(symbol):
        return True
def wincheck_row(symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] == symbol:
            return True
def wincheck_column(symbol):
    for i in range(3):    
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] == symbol:
            return True
def wincheck_diag_1(symbol):
    return board[0][0] == board[1][1] == board[2][2] and board[0][0] == symbol
def wincheck_diag_2(symbol):
    return board[2][0] == board[1][1] == board[0][2] and board[2][0]== symbol





run_game()
