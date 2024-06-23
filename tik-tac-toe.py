import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 6
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Fonts
FONT = pygame.font.SysFont('comicsans', 90)

def draw_grid():
    # Draw horizontal lines
    pygame.draw.line(WIN, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(WIN, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
    # Draw vertical lines
    pygame.draw.line(WIN, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(WIN, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_xo(row, col, symbol):
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if symbol == 'X':
        pygame.draw.line(WIN, RED, (x - SQUARE_SIZE // 3, y - SQUARE_SIZE // 3), (x + SQUARE_SIZE // 3, y + SQUARE_SIZE // 3), LINE_WIDTH // 2)
        pygame.draw.line(WIN, RED, (x + SQUARE_SIZE // 3, y - SQUARE_SIZE // 3), (x - SQUARE_SIZE // 3, y + SQUARE_SIZE // 3), LINE_WIDTH // 2)
    elif symbol == 'O':
        pygame.draw.circle(WIN, BLUE, (x, y), SQUARE_SIZE // 3, LINE_WIDTH // 2)

def check_win(board):
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]

    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0

def main():
    board = [[0] * BOARD_COLS for _ in range(BOARD_ROWS)]
    turn = 'X'
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 'X':
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE

                if board[row][col] == 0:
                    board[row][col] = 'X'
                    turn = 'O'

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 'O':
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE

                if board[row][col] == 0:
                    board[row][col] = 'O'
                    turn = 'X'

        # Fill the window with black color
        WIN.fill(BLACK)
        draw_grid()

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] != 0:
                    draw_xo(row, col, board[row][col])

        winner = check_win(board)
        if winner:
            text = FONT.render(f"{winner} wins!", True, WHITE)
            WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            run = False

        pygame.display.update()

if __name__ == "__main__":
    main()
