from copy import deepcopy
GRAY_SQUARE = (240, 217, 181)
BROWN_SQUARE = (181, 136, 99)

SQUARE_SIZE = 55
WINDOW_SIZE = (SQUARE_SIZE * 8, SQUARE_SIZE * 8)
WHITE_PIECE = 0
BLACK_PIECE = 1

pieceorder = {
    0: ".",
    1: "♟",
    2: "♞",
    3: '♝',
    4: '♛',
    5: '♜',
    6: '♚',
    7: '♙',
    8: '♘',
    9: '♗',
    10: '♕',
    11: '♖',
    12: '♔'
}
pieceorder_fen = {

    ".": 0,
    "p": 1,
    "n": 2,
    "b": 3,
    "q": 4,
    "r": 5,
    "k": 6,
    'P': 7,
    'N': 8,
    'B': 9,
    'Q': 10,
    'R': 11,
    'K': 12
}    
notationorder = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}
class Piece():
    #def __init__(self, color, row, col):
        #self.color = color
        #self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        #self.noty = str(8 - row)
        #self.posx = col
        #self.posy = 7 - row
        #print(f'position is {self.notx}{self.noty}')
    
    def get_moves(self):
        assert False, "dont use the base base class ya whippa snapper"
class Pawn(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 1 if self.color == WHITE_PIECE else 7
    def get_moves(self):
        print(self.color)
        self.moves = []
        if self.color == WHITE_PIECE:
            if self.posy == 1:
                self.moves.append((self.posx, self.posy + 2))
            self.moves.append((self.posx, self.posy + 1))
        else:
            if self.posy == 6:
                self.moves.append((self.posx, self.posy - 2))
            self.moves.append((self.posx, self.posy - 1))
        print(self.moves)
        print([self.posx, self.posy])
        print(self.color)
        
                
            
class Knight(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 1 if self.color == WHITE_PIECE else 7
    def get_moves(self):
        self.moves = []
        self.moves.append((self.posx + 2, self.posy + 1),(self.posx - 2, self.posy + 1),(self.posx + 2, self.posy - 1),(self.posx - 2, self.posy - 1)(self.posx + 1, self.posy + 2),(self.posx - 1, self.posy + 2),(self.posx + 1, self.posy - 2),(self.posx - 1, self.posy - 2))
        for a, (x,y) in enumerate(self.moves):
            if (x > 7 or y > 7) or (x < 0 or y < 0):
                self.moves.pop(a) 

class Bishop(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
class Queen(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
class Rook(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
class King(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
pieceorderreal = {
1: (Pawn, 0),
2: (Knight, 0),
3: (Bishop, 0),
4: (Queen, 0),
5: (Rook, 0),
6: (King, 0),
7: (Pawn, 1),
8: (Knight, 1),
9: (Bishop, 1),
10: (Queen, 1),
11: (Rook, 1),
12: (King, 1)}


class ChessBoard():
    def __init__(self, FEN):
        self.boardarray = [[0 for col in range(8)] for row in range(8)]
        self.board = [[0 for col in range(8)] for row in range(8)]
        print(self.board)
        fen_split = FEN[:-13].split('/')
        for row in range(8):
            fen_split2 = list(fen_split[row])
            col_index = 0
            for col in fen_split2:
                if col.isdigit():
                    col_index += int(col)
                elif col.lower() in ['p', 'n', 'b', 'r', 'q', 'k']:
                    self.set_piece(row, col_index, pieceorder_fen[col])
                    col_index += 1
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != 0:
                    piecetype = self.board[row][col]
                    piece_type = pieceorderreal[piecetype][0]
                    piece_color = pieceorderreal[piecetype][1]
                    print(piece_color)
                    self.boardarray[7 - row][col] = piece_type(piece_color, 7 - row, col)
    def check_if_valid(self, posx, posy, des_posx, des_posy):
        
        print(self.boardarray[7-posy][posx])
        if self.boardarray[7-posy][posx] == 0:
            return False
        self.boardarray[7 - posy][posx].get_moves()
        for a, (x,y) in enumerate(self.boardarray[7 - posy][posx].moves):
            if self.board[7-y][x] != 0:
                self.boardarray[7-posy][posx].moves.pop(a)
                
        if (des_posx, des_posy) in self.boardarray[7 - posy][posx].moves:
            self.boardarray[7 - posy][posx].posx = des_posx
            self.boardarray[7 - posy][posx].posy = des_posy
            self.board[7 - posy][posx] = 0
            self.board[7 - des_posy][des_posx] = self.boardarray[7 - posy][posx].type
            self.boardarray[7 - des_posy][des_posx] = deepcopy(self.boardarray[7 - posy][posx])
            self.boardarray[7 - posy][posx] = 0
            return True
        else:
            return False

    def move_white(self):
        check = list(input('Where would you like to go? (white)'))
        print((notationorder[check[0]], int(check[1]) - 1, notationorder[check[2]], int(check[3]) - 1))
        while self.check_if_valid(notationorder[check[0]], int(check[1]) - 1, notationorder[check[2]], int(check[3]) - 1) == False:
            print('invalid move')
            check = list(input('Where would you like to go? (white)'))
    def move_black(self):
        check = list(input('Where would you like to go? (black)'))
        while self.check_if_valid(notationorder[check[0]], int(check[1]) - 1, notationorder[check[2]], int(check[3]) - 1) == False:
            print('invalid move')
            check = list(input('Where would you like to go? (black)'))



                
        
    def set_piece(self, row, col, value):
        self.board[row][col] = value
        
    def get_piece(self, row, col):
        return self.board[row][col]
    running = True
    def display(self):
        for row in range(8):
            currentrow = ''
            for col in range(8):
                if self.board[row][col] > 6:  
                    colorstr = "\033[35m" 
                elif self.board[row][col] > 0: 
                    colorstr = "\033[36m"
                else: colorstr  = ''
                #7 is the start of the black piece index #s
                currentrow += (colorstr + str(pieceorder[self.board[row][col]]) + '\033[0m')
                currentrow += ' '
            print(currentrow)
    

def run_game():
    while True:
        board.move_white()
        board.display()
        print(board.board)
        board.move_black()
        board.display()

        #pygame.display.update() #temp
        
'''        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
           #elif event.type == pygame.MOUSEBUTTONDOWN:
    
    
    def run_game(self):
        if __name__ == '__main__':
            #pygame.init()
            self.read_fen(fen)
            #self.draw()
            while self.running:
                
                self.handle_events()
                #board.update_board()
                screen.blit(piece_images[random.randrange(1,13)], (random.randrange(8) * board.SQUARE_SIZE, (random.randrange(8) * board.SQUARE_SIZE)))
                pygame.display.update()  # Add this line to update the display  # Add this line to limit the frame rate
'''

board = ChessBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
board.display()
print(board.boardarray)
run_game()