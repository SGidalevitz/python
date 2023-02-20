#Moves before cut / after cut turn into notation for better terminal usage

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

pieceorder_fen_write = {
    1: 'p',
    2: 'n',
    3: 'b',
    4: 'q',
    5: 'r',
    6: 'k',
    7: 'P',
    8: 'N',
    9: 'B',
    10: 'Q',
    11: 'R',
    12: 'K'
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
allmoves = []
class Pawn(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 1 if self.color == WHITE_PIECE else 7

    def get_moves(self):
        global allmoves
        self.moves = []
        self.captures = []
    
        if self.color == WHITE_PIECE:
            if self.posy == 1:
                self.moves.append((self.posx, self.posy + 2))
            self.moves.append((self.posx, self.posy + 1))
            #diagonal pawn captures
            self.captures.append((self.posx + 1, self.posy + 1))
            self.captures.append((self.posx - 1, self.posy + 1))

        
        else:
            if self.posy == 6:
                self.moves.append((self.posx, self.posy - 2))
            self.moves.append((self.posx, self.posy - 1))
            #diagonal pawn captures
            self.captures.append((self.posx + 1, self.posy - 1))
            self.captures.append((self.posx - 1, self.posy - 1))
        self.valid_moves = []
        self.valid_captures = []
        for x, y in self.moves:
            if 0 <= x <= 7 and 0 <= y <= 7:
                self.valid_moves.append((x, y))
        self.moves = self.valid_moves
        for x, y in self.captures:
            if 0 <= x <= 7 and 0 <= y <= 7:
                self.valid_captures.append((x, y))
        self.captures = self.valid_captures
    
            
class Knight(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 2 if self.color == WHITE_PIECE else 8
    def get_moves(self):
        self.moves = []
        self.moves = [(self.posx + 2, self.posy + 1),(self.posx - 2, self.posy + 1),(self.posx + 2, self.posy - 1),(self.posx - 2, self.posy - 1),(self.posx + 1, self.posy + 2),(self.posx - 1, self.posy + 2),(self.posx + 1, self.posy - 2),(self.posx - 1, self.posy - 2)]
        self.valid_moves = []
        for x, y in self.moves:
            if 0 <= x <= 7 and 0 <= y <= 7:
                self.valid_moves.append((x, y))
        self.moves = self.valid_moves


class Bishop(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 3 if self.color == WHITE_PIECE else 9
    def get_moves(self):
        self.moves = []
        self.iterx = self.posx
        self.itery = self.posy
        print((self.iterx, self.itery))
        iteration = 0
        #bottom left
        while (self.iterx > -1) and (self.itery > -1):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx -= 1
            self.itery -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #bottom right
        while (self.iterx < 8) and (self.itery > -1):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx += 1
            self.itery -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #top left
        while (self.iterx > -1) and (self.itery < 8):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx -= 1
            self.itery += 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #top right
        while (self.iterx < 8) and (self.itery < 8):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx += 1
            self.itery += 1
            iteration = 1
        iteration = 0
class Queen(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 4 if self.color == WHITE_PIECE else 10
    def get_moves(self):
        self.moves = []
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #left
        while 0 <= self.iterx <= 7:
            if iteration == 1:
                if board.boardarray[7 - self.posy][self.iterx] != 0:
                    if board.boardarray[7-self.posy][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.posy))
                        break
                self.moves.append((self.iterx, self.posy))
            self.iterx -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #right
        while 0 <= self.iterx <= 7:
            if iteration == 1:
                if board.boardarray[7 - self.posy][self.iterx] != 0:
                    if board.boardarray[7-self.posy][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.posy))
                        break
                self.moves.append((self.iterx, self.posy))
            self.iterx += 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #down
        while 0 <= self.itery <= 7:
            if iteration == 1:
                if board.boardarray[7 - self.itery][self.posx] != 0:
                    if board.boardarray[7-self.itery][self.posx].color == self.color:
                        break
                    else:
                        self.moves.append((self.posx, self.itery))
                        break
                self.moves.append((self.posx, self.itery))
            self.itery -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #down
        while 0 <= self.itery <= 7:
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.posx] != 0:
                    if board.boardarray[7-self.itery][self.posx].color == self.color:
                        break
                    else:
                        self.moves.append((self.posx, self.itery))
                        break
                self.moves.append((self.posx, self.itery))
            self.iterx += 1
            self.itery += 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #bottom left
        while (self.iterx > -1) and (self.itery > -1):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx -= 1
            self.itery -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #bottom right
        while (self.iterx < 8) and (self.itery > -1):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx += 1
            self.itery -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #top left
        while (self.iterx > -1) and (self.itery < 8):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx -= 1
            self.itery += 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #top right
        while (self.iterx < 8) and (self.itery < 8):
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.iterx] != 0:
                    if board.boardarray[7-self.itery][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.itery))
                        break
                self.moves.append((self.iterx, self.itery))
                print((self.iterx, self.itery))
            self.iterx += 1
            self.itery += 1
            iteration = 1
        iteration = 0
class Rook(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 5 if self.color == WHITE_PIECE else 11
    def get_moves(self):
        self.moves = []
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #left
        while 0 <= self.iterx <= 7:
            if iteration == 1:
                if board.boardarray[7 - self.posy][self.iterx] != 0:
                    if board.boardarray[7-self.posy][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.posy))
                        break
                self.moves.append((self.iterx, self.posy))
            self.iterx -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #right
        while 0 <= self.iterx <= 7:
            if iteration == 1:
                if board.boardarray[7 - self.posy][self.iterx] != 0:
                    if board.boardarray[7-self.posy][self.iterx].color == self.color:
                        break
                    else:
                        self.moves.append((self.iterx, self.posy))
                        break
                self.moves.append((self.iterx, self.posy))
            self.iterx += 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #down
        while 0 <= self.itery <= 7:
            if iteration == 1:
                if board.boardarray[7 - self.itery][self.posx] != 0:
                    if board.boardarray[7-self.itery][self.posx].color == self.color:
                        break
                    else:
                        self.moves.append((self.posx, self.itery))
                        break
                self.moves.append((self.posx, self.itery))
            self.itery -= 1
            iteration = 1
        self.iterx = self.posx
        self.itery = self.posy
        iteration = 0
        #down
        while 0 <= self.itery <= 7:
            if iteration == 1:
                
                if board.boardarray[7 - self.itery][self.posx] != 0:
                    if board.boardarray[7-self.itery][self.posx].color == self.color:
                        break
                    else:
                        self.moves.append((self.posx, self.itery))
                        break
                self.moves.append((self.posx, self.itery))
            self.iterx += 1
            self.itery += 1
            iteration = 1
        iteration = 0

class King(Piece):
    def __init__(self, color, row, col):
        self.color = color
        self.notx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][col]
        self.noty = str(8 - row)
        self.posx = col
        self.posy = 7 - row
        self.type = 6 if self.color == WHITE_PIECE else 12
    def get_moves(self):
        self.moves = [(self.posx - 1, self.posy + 1), #top left
                      (self.posx, self.posy + 1), #top middle
                      (self.posx + 1, self.posy + 1), #top right
                      (self.posx - 1, self.posy), #middle left
                      #skip center
                      (self.posx + 1, self.posy), #middle right
                      (self.posx - 1, self.posy - 1), #bottom left
                      (self.posx, self.posy - 1), #bottom middle
                      (self.posx + 1, self.posy - 1)#bottom right
                      ]
        self.valid_moves = []
        for (x,y) in self.moves:
            if 0 <= x <= 7 and 0 <= y <= 7:
                self.valid_moves.append((x,y))
        self.moves = self.valid_moves

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
        self.board = [[0 for col in range(8)] for row in range(8)]
        self.fen_read(FEN)
        self.create_objects()
        
        
    def create_objects(self):
        self.boardarray = [[0 for col in range(8)] for row in range(8)]
        
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != 0:
                    piecetype = self.board[row][col]
                    piece_type = pieceorderreal[piecetype][0]
                    piece_color = pieceorderreal[piecetype][1]
                    self.boardarray[7 - row][col] = piece_type(piece_color, 7 - row, col)
    def create_theoretical_objects(self, board):
        self.theoretical_board = [[0 for col in range(8)] for row in range(8)]
        for row in range(8):
            for col in range(8):
                if board[row][col] != 0:
                    piecetype = board[row][col]
                    piece_type = pieceorderreal[piecetype][0]
                    piece_color = pieceorderreal[piecetype][1]
                    self.theoretical_board[7 - row][col] = piece_type(piece_color, 7 - row, col)
    def fen_read(self, FEN):
        fen_board_andvars = FEN.split(' ')
        fen_split = fen_board_andvars[0].split('/')
        for row in range(8):
            fen_split2 = list(fen_split[row])
            col_index = 0
            for col in fen_split2:
                if col.isdigit():
                    col_index += int(col)
                elif col.lower() in ['p', 'n', 'b', 'r', 'q', 'k']:
                    self.set_piece(row, col_index, pieceorder_fen[col])
                    col_index += 1
        self.to_move = {'w': WHITE_PIECE, 'b': BLACK_PIECE}[fen_board_andvars[1]]
        self.castling_rights = fen_board_andvars[2]
        self.en_passant_ts = fen_board_andvars[3]
        if self.en_passant_ts == '-':
            self.en_passant_next_move = False
        else:
            self.en_passant_next_move = True
        self.halfmove_clock_since_event = int(fen_board_andvars[4])
        self.fullmove_clock = int(fen_board_andvars[5])
    def fen_write(self):
        fen = ''
        col_index = 0
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != 0:
                    if col_index > 0:
                        fen += str(col_index)
                    fen += pieceorder_fen_write[self.board[row][col]]
                else:
                    col_index += 1
            if col_index > 0:
                fen += str(col_index)
            col_index = 0
            fen += '/'
        
        


    def cut_down_options(self, posx, posy):
        if self.boardarray[7-posy][posx] == 0:
            return False
        self.boardarray[7 - posy][posx].get_moves()
        #print(f'moves: {self.boardarray[7-posy][posx].moves}, captures: {self.boardarray[7-posy][posx].captures}')
        self.valid_moves = []
        #If the piece is a pawn, note pawns have special capturing rules
        if self.boardarray[7-posy][posx].type == 1 or self.boardarray[7-posy][posx].type == 7:
            for (x,y) in self.boardarray[7 - posy][posx].moves:
                if self.board[7-y][x] == 0:
                    self.valid_moves.append((x,y))
            for (x,y) in self.boardarray[7-posy][posx].captures:
                if self.boardarray[7-y][x] != 0:
                    if self.boardarray[7-y][x].color != self.boardarray[7-posy][posx].color:
                        self.valid_moves.append((x,y))
                else: 
                    #if en passant is valid in this case
                    if (x,y) == self.en_passant_ts:
                        self.valid_moves.append((x,y))
                        self.en_passant_next_move = True
        else:
            for (x,y) in self.boardarray[7 - posy][posx].moves:
                if self.board[7-y][x] == 0 or self.boardarray[7-y][x].color != self.boardarray[7-posy][posx].color:
                        self.valid_moves.append((x,y))
        return True
    def isvalid(self, des_posx, des_posy, valid_moves):
        if (des_posx, des_posy) in valid_moves:    
            return True
        else:
            return False   
    def make_move(self, posx, posy, des_posx, des_posy, en_passant):
        if self.boardarray[7-posy][posx].type == 1:
            if ((des_posx, des_posy) == self.en_passant_ts) and self.en_passant_next_move:
                self.boardarray[8 - self.en_passant_ts[1]][self.en_passant_ts[0]] = 0
                self.board[8 - self.en_passant_ts[1]][self.en_passant_ts[0]] = 0
        elif self.boardarray[7-posy][posx].type == 7:
            if ((des_posx, des_posy) == self.en_passant_ts) and self.en_passant_next_move:
                self.boardarray[6 - self.en_passant_ts[1]][self.en_passant_ts[0]] = 0
                self.board[6 - self.en_passant_ts[1]][self.en_passant_ts[0]] = 0
    
        self.boardarray[7 - posy][posx].posx = des_posx
        self.boardarray[7 - posy][posx].posy = des_posy
        self.board[7 - posy][posx] = 0
        self.board[7 - des_posy][des_posx] = self.boardarray[7 - posy][posx].type
        self.boardarray[7 - des_posy][des_posx] = deepcopy(self.boardarray[7 - posy][posx])
        self.boardarray[7 - posy][posx] = 0
    def make_move_theoretical(self, posx, posy, des_posx, des_posy)         
    def move_white(self):
        check = list(input('Where would you like to go? (white)'))
        if len(check) == 4:
            if not (check[1].isnumeric() and check[3].isnumeric()):
                print('invalid move')
                self.move_white()
                return
            else:
                check[1] = int(check[1])
                check[3] = int(check[3])
            if not (check[0] in notationorder.keys() and check[1] >= 1 and check[1] <= 8 and check[2] in notationorder.keys() and check[3] >= 1 and check[3] <= 8):
                print('invalid move')
                self.move_white()
                return
            posx = notationorder[check[0]]
            posy = int(check[1]) - 1
            des_posx = notationorder[check[2]]
            des_posy = int(check[3]) - 1
            if not self.cut_down_options(posx, posy):
                print('no piece there')
                self.move_white()
                return
            if not self.isvalid(des_posx, des_posy, self.valid_moves):
                print('invalid move')
                self.move_white()
                return
            self.cut_down_options(posx, posy)
            if not self.boardarray[7 - posy][posx].color == self.to_move:
                print('it not cho turn dumbass')
                self.move_white()
                return
            if (des_posy - posy == 2) and (self.boardarray[7-posy][posx].type == 1 or self.boardarray[7-posy][posx].type == 7):
                self.en_passant_ts = (posx, posy + 1)
            self.make_move(posx, posy, des_posx, des_posy, ...)
            
        elif len(check) == 2:
            if not check[1].isnumeric():
                print('invalid move')
                self.move_white()
                return
            check[1] = int(check[1])   
            if not ((check[0] in notationorder.keys()) and 1 <= check[1] <= 8):
                print('invalid move')
                self.move_white()
                return
            posx = notationorder[check[0]]
            posy = int(check[1]) - 1
            if self.cut_down_options(posx, posy) == False:
                print('no piece there')
                self.move_white()
                return
            self.display_possible_moves(self.valid_moves)
            self.move_white()      
        else: 
            print('invalid move')
            self.move_white()
            return
    def move_black(self):
        check = list(input('Where would you like to go? (black)'))
        if len(check) == 4:
            if not (check[1].isnumeric() and check[3].isnumeric()):
                print('invalid move')
                self.move_black()
                return
            else:
                check[1] = int(check[1])
                check[3] = int(check[3])
            if not (check[0] in notationorder.keys() and check[1] >= 1 and check[1] <= 8 and check[2] in notationorder.keys() and check[3] >= 1 and check[3] <= 8):
                print('invalid move')
                self.move_black()
                return
            posx = notationorder[check[0]]
            posy = int(check[1]) - 1
            des_posx = notationorder[check[2]]
            des_posy = int(check[3]) - 1
            if self.cut_down_options(posx, posy) == False:
                print('no piece there')
                self.move_black()
                return
            if not self.isvalid(des_posx, des_posy, self.valid_moves):
                print('invalid move')
                self.move_black()
                return
            self.cut_down_options(posx, posy)
            if not self.boardarray[7 - posy][posx].color == self.to_move:
                print('it not cho turn dumbass')
                self.move_black()
                return
            if (posy - des_posy == 2) and (self.boardarray[7-posy][posx].type == 1 or self.boardarray[7-posy][posx].type == 7):
                self.en_passant_ts = (posx, posy - 1)

            self.make_move(posx, posy, des_posx, des_posy, ...)
        elif len(check) == 2:
            if not check[1].isnumeric():
                print('invalid move')
                self.move_black()
                return
            check[1] = int(check[1])   
            if not ((check[0] in notationorder.keys()) and 1 <= check[1] <= 8):
                print('invalid move')
                self.move_black()
                return
            posx = notationorder[check[0]]
            posy = int(check[1]) - 1
            if not self.cut_down_options(posx, posy):
                print('no piece there')
                self.move_black()
                return
            self.display_possible_moves(self.valid_moves)
            self.move_black() 
        else: 
            print('invalid move')
            self.move_black()
            return


    def on_move(self, color):
        self.to_move = 1 - color
        if color == BLACK_PIECE:
            self.fullmove_clock += 1
        if self.en_passant_next_move:
            self.en_passant_next_move = False

    def set_piece(self, row, col, value):
        self.board[row][col] = value
        
    def get_piece(self, row, col):
        return self.board[row][col]
    running = True

    def en_passant_cycle(self, move):
        while self.on_move == move:
            pass
        self.en_passant_ts = '-'
    def display(self):
        for row in range(8):
            currentrow = ''
            for col in range(8):
                if self.boardarray[row][col] != 0:
                    if self.boardarray[row][col].color == BLACK_PIECE:  
                        colorstr = "\033[35m" 
                    elif self.boardarray[row][col].color == WHITE_PIECE: 
                        colorstr = "\033[36m"
                else: colorstr  = ''
                #7 is the start of the black piece index #s
                currentrow += (colorstr + str(pieceorder[self.board[row][col]]) + '\033[0m')
                currentrow += ' '
            print(currentrow)
    def display_possible_moves(self, valid_moves):
        #MAKE SURE TO FIX WHETHER THE TWO CHAR INPUT WORKS OR NAH
        self.valid_moves_notations = []
        for (x, y) in valid_moves:
            self.valid_moves_notations.append(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][x] + str(y + 1))
        self.valid_moves_notations_str = ', '.join(self.valid_moves_notations)
        print(f'Possible moves are: {self.valid_moves_notations_str}')
        for row in range(8):
            currentrow = ''
            for col in range(8):
                
                if self.boardarray[row][col] != 0:
                    if self.boardarray[row][col].color == BLACK_PIECE:  
                        colorstr = "\033[35m" 
                    elif self.boardarray[row][col].color == WHITE_PIECE: 
                        colorstr = "\033[36m"
                else: 
                    colorstr  = ''
                if (col, 7 - row) in valid_moves:
                    colorstr = "\033[31m"
                
                #7 is the start of the black piece index #s
                currentrow += (colorstr + str(pieceorder[self.board[row][col]]) + '\033[0m')
                currentrow += ' '
            print(currentrow)
    #note this checks for if the color passed through as an argument is in check    
    def check_for_check(self, color):
        if color == WHITE_PIECE:
            self.king_id = 6
        else:
            self.king_id = 12
        
        for row in range(8):
            for col in range(8):
                if self.boardarray[row][col] != 0:
                    if self.boardarray[row][col].color == 1 - color:
                        if self.boardarray[row][col].type == self.king_id:
                            self.king_posx = col
                            self.king_posy = 7 - row
                        self.cut_down_options(7 - col, row)
                        self.allmoves += self.valid_moves
                        self.valid_moves = []
        if (self.king_posx, self.king_posy) in self.allmoves:
            return True
        else:
            return False



def game_loop():
    while True:
        board.move_white()
        board.on_move(WHITE_PIECE)
       
        board.display()
        board.move_black()
        board.on_move(BLACK_PIECE)
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
game_loop()