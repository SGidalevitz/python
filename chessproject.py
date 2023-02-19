import pygame
pieceorder = {
    0: ".",
    1: "p",
    2: "n",
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
class ChessBoard:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(0)
            self.board.append(row)
        self.gray_square = (240, 217, 181)
        self.brown_square = (181, 136, 99)
        self.square_size = 55
        self.window_size = (self.square_size * 8, self.square_size * 8)

    
        
    def set_piece(self, row, col, value):
        self.board[row][col] = value
        
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def display(self):
        for row in range(8):
            currentrow = ''
            for col in range(8):
                currentrow += str(pieceorder[self.board[row][col]])
                currentrow += ' '
            print(currentrow)

    def draw(self):
        pygame.init()
        screen = pygame.display.set_mode(self.window_size)
        screen.fill((255, 255, 255))
        for row in range(8):
            for col in range(8):
                x_pos = col * self.square_size
                y_pos = row * self.square_size
                if (row + col) % 2 == 0:
                    color = self.gray_square
                else:
                    color = self.brown_square
                pygame.draw.rect(screen, color, (x_pos, y_pos, self.square_size, self.square_size))
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
board = ChessBoard()

fen = 'r4rk1/1ppqb1pp/p1n1pn2/3p1p2/Q1PP4/PP4P1/1B1NPPBP/R4RK1'
def read_fen(fen):
    fen_split = fen.split('/')
    for row in range(8):
        fen_split2 = list(fen_split[row])
        print(fen_split2)
        col_index = 0
        for col in fen_split2:
            if col.isdigit():
                col_index += int(col)
            elif col.lower() in ['p', 'n', 'b', 'r', 'q', 'k']:
                board.set_piece(row, col_index, pieceorder_fen[col])
                col_index += 1
                
read_fen(fen)
board.display()
board.draw()