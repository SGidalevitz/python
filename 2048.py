#board = [0, 1, 4, 0, 0, 0, 0, 7, 0, 0, 8, 0, 0, 0, 0, 0]


CELL_STR_MAX = 4
class Cell:
  num = 0
  def __init__(self, num):
    self.num = num
  def __str__(self):
    num_str = str(self.num)
    return num_str + " " * (CELL_STR_MAX - len(num_str))

class Board:
    sizew = 4
    sizeh = 4
    cells = [[0]]
    def __init__(self, size=(4,4)):
        self.sizew = size[0]
        self.sizeh = size[1]
        self.cells = []
        for i in range(self.sizeh):
            arr = []
            for j in range(self.sizew):
                arr.append(Cell(0))
            self.cells.append(arr)
    def __str__(self):
        board_print = ""
        for i in range(self.sizeh):
            
            for j in range(self.sizew):
                board_print += str(self.cells[i][j])
                board_print += " "
            
            if i != (self.sizeh - 1):
                board_print += "\n"
        return  board_print
    def changecell(self, row, col, val):
        game.board.cells[row][col].num = val
    def getcell(self, row, col):
        return game.board.cells[row][col]
MOVE_UP = 0
MOVE_DOWN = 1
MOVE_RIGHT = 2
MOVE_LEFT = 3

class Game:  
    board = None
    def __init__(self, sizew, sizeh):
        self.board = Board((sizew, sizeh))
    def move_left(self, row, col):
        if col == 0:
            return False
        

game = Game(4, 4)
game.board.changecell(0, 3, 16)
print(game.board)




"""target_cell_len = 4
cell_str += (target_cell_len - len(cell_str)) * " "
def print_board():

    for a, b, c, d in board:
        print(a, b, c, d)
    print(2 ** board[0] += (target_cell_len - len(2 ** board[0])) * " ", "  ", 2 ** board[1], "  ", 2 ** board[2], "  ", 2 ** board[3])
    print(2 ** board[4], "  ", 2 ** board[5], "  ", 2 ** board[6], "  ", 2 ** board[7])
    print(2 ** board[8], "  ", 2 ** board[9], "  ", 2 ** board[10], "  ",2 ** board[11])
    print(2 ** board[12], "  ", 2 ** board[13], "  ", 2 ** board[14], "  ", 2 ** board[15])
print_board()
""""""

def print_board():
    index = 0
    for i in board:
    
        row1 = i + (target_cell_len - len(cell_str)) * " "
        
def move_left():
    index = 0
    for i in board:
        index += 1
        if i != 0 and index % 4 != 0:
            pass

def left(i):
    if i % 4 != 0:
        return i-1
    else:
        return False
def right(i):
    if i % 4 != 3:
        return i+1
    else:
        return False
def up(i):
    if i > 3:
        return i-4
    else:
        return False
def down(i):
    if i < 12:
        return i+4
    else:
        return False
        """

