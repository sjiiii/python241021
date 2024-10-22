import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (128, 0, 0)
]

# 게임 설정
BLOCK_SIZE = 30
FIELD_WIDTH = 10
FIELD_HEIGHT = 20
SCREEN_WIDTH = FIELD_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = FIELD_HEIGHT * BLOCK_SIZE

# 테트로미노 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = FIELD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

class Tetris:
    def __init__(self):
        self.field = [[0] * FIELD_WIDTH for _ in range(FIELD_HEIGHT)]
        self.current_piece = Tetromino()
        self.score = 0

    def new_piece(self):
        self.current_piece = Tetromino()
        if self.check_collision():
            return False
        return True

    def check_collision(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    if (self.current_piece.y + y >= FIELD_HEIGHT or
                        self.current_piece.x + x < 0 or
                        self.current_piece.x + x >= FIELD_WIDTH or
                        self.field[self.current_piece.y + y][self.current_piece.x + x]):
                        return True
        return False

    def merge_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.field[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color

    def remove_lines(self):
        lines_removed = 0
        for y in range(FIELD_HEIGHT):
            if all(self.field[y]):
                del self.field[y]
                self.field.insert(0, [0] * FIELD_WIDTH)
                lines_removed += 1
        self.score += lines_removed ** 2 * 100

    def move(self, dx, dy):
        self.current_piece.x += dx
        self.current_piece.y += dy
        if self.check_collision():
            self.current_piece.x -= dx
            self.current_piece.y -= dy
            if dy > 0:
                self.merge_piece()
                self.remove_lines()
                if not self.new_piece():
                    return False
        return True

    def rotate(self):
        old_shape = self.current_piece.shape
        self.current_piece.rotate()
        if self.check_collision():
            self.current_piece.shape = old_shape

def draw_field(screen, field):
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_piece(screen, piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, piece.color,
                                 ((piece.x + x) * BLOCK_SIZE, (piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("테트리스")
    clock = pygame.time.Clock()
    game = Tetris()
    fall_time = 0
    fall_speed = 0.5
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()

        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            if not game.move(0, 1):
                running = False
            fall_time = 0

        draw_field(screen, game.field)
        draw_piece(screen, game.current_piece)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"점수: {game.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()