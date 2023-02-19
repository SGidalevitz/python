import chess
import pygame
import random
piece_images = {
    1: pygame.image.load("black_piece_pawn.png"),
    2: pygame.image.load("black_piece_knight.png"),
    3: pygame.image.load("black_piece_bishop.png"),
    4: pygame.image.load("black_piece_queen.png"),
    5: pygame.image.load("black_piece_rook.png"),
    6: pygame.image.load("black_piece_king.png"),
    7: pygame.image.load("white_piece_pawn.png"),
    8: pygame.image.load("white_piece_knight.png"),
    9: pygame.image.load("white_piece_bishop.png"),
    10: pygame.image.load("white_piece_queen.png"),
    11: pygame.image.load("white_piece_rook.png"),
    12: pygame.image.load("white_piece_king.png")
}
fen = 'r1b1k2r/ppN3pp/5pn1/2p1p3/2P1P3/5N2/PPP2PPP/3R1RK1 b - - 0 13'

}
def draw():
        global screen
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption('Chess')

        screen.fill((255, 255, 255))
        for row in range(8):
            for col in range(8):
                x_pos = col * SQUARE_SIZE
                y_pos = row * SQUARE_SIZE
                if (row + col) % 2 == 0:
                    color = GRAY_SQUARE
                else:
                    color = self.BROWN_SQUARE
                pygame.draw.rect(screen, color, (x_pos, y_pos, self.SQUARE_SIZE, self.SQUARE_SIZE))
                if self.board[row][col] != 0:
                    piece = piece_images[self.board[row][col]]
                    x = (col * board.SQUARE_SIZE) - 2.5
                    y = (row * board.SQUARE_SIZE) - 3
                    screen.blit(piece, (x, y))
if __name__ == "__main__":
    dragging = False
    start_pos = (0, 0)



    board = ChessBoard()
         
    board.run_game()

