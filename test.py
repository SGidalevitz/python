import random
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.scr = pygame.display.set_mode((200, 200))
        pygame.display.set_caption("2048")
        self.font = pygame.font.Font(None, 30)
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.spawn_tile()
        self.spawn_tile()


    def spawn_tile(self):
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_tiles:
            value = 2 if random.random() < 0.9 else 4
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = value

    def move(self, direction):
        if direction == 'up':
            self.grid = [list(row) for row in zip(*self.grid[::-1])]
        elif direction == 'down':
            self.grid = [list(row) for row in zip(*self.grid)[::-1]]
        elif direction == 'right':
            self.grid = [row[::-1] for row in self.grid]
        for i in range(4):
            self.grid[i] = self.slide(self.grid[i])
            self.grid[i] = self.combine(self.grid[i])
            self.grid[i] = self.slide(self.grid[i])
        if direction == 'up':
            self.grid = [list(row) for row in zip(*self.grid[::-1])]
        elif direction == 'down':
            self.grid = [list(row) for row in zip(*self.grid)[::-1]]
        elif direction == 'right':
            self.grid = [row[::-1] for row in self.grid]
        self.spawn_tile()

    def slide(self, row):
        return [x for x in row if x != 0] + [0 for _ in range(row.count(0))]

    def combine(self, row):
        for i in range(3):
            if row[i] == row[i+1] and row[i] != 0:
                row[i] *= 2
                row[i+1] = 0
                row = self.slide(row)
        return row

    def is_over(self):
        if any(0 in row for row in self.grid):
            return False
        for i in range(4):
            for j in range(4):
                if j < 3 and self.grid[i][j] == self.grid[i][j+1]:
                    return False
                if i < 3 and self.grid[i][j] == self.grid[i+1][j]:
                    return False
        return True

    def is_won(self):
        return any(any(x >= 2048 for x in row) for row in self.grid)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])
    def draw_grid(self):
        for i in range(4):
            for j in range(4):
                value = self.grid[i][j]
                color = (0, 0, 0) if value == 0 else (255, 255, 255)
                text = self.font.render(str(value) if value else '', True, color)
                text_rect = text.get_rect()
                text_rect.center = (50 * j + 25, 50 * i + 25)
                self.scr.blit(text, text_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move('up')
                    elif event.key == pygame.K_DOWN:
                        self.move('down')
                    elif event.key == pygame.K_LEFT:
                        self.move('left')
                    elif event.key == pygame.K_RIGHT:
                        self.move('right')

            self.scr.fill((0, 0, 0))
            self.draw_grid()
            pygame.display.update()

            if self.is_over():
                running = False
                if self.is_won():
                    print("You won!")
                else:
                    print("Game over.")

    
if __name__ == '__main__':
    game = Game()
    game.run()