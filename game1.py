import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set board dimensions
ROWS = 3
COLS = 3
CELL_SIZE = 200

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('3D GUI Tic Tac Toe')

# Initialize the board
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Function to draw the grid
def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(screen, WHITE, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), 2)
    for j in range(1, COLS):
        pygame.draw.line(screen, WHITE, (j * CELL_SIZE, 0), (j * CELL_SIZE, SCREEN_HEIGHT), 2)

# Function to draw the Xs and Os
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * CELL_SIZE + 50, row * CELL_SIZE + 50), 
                                 ((col + 1) * CELL_SIZE - 50, (row + 1) * CELL_SIZE - 50), 5)
                pygame.draw.line(screen, RED, ((col + 1) * CELL_SIZE - 50, row * CELL_SIZE + 50), 
                                 (col * CELL_SIZE + 50, (row + 1) * CELL_SIZE - 50), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3, 5)

# Function to check for a win
def check_win():
    # Check rows
    for row in range(ROWS):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return True
    # Check columns
    for col in range(COLS):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

# Function to check for a tie
def check_tie():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == ' ':
                return False
    return True

# Main loop
running = True
turn = 'X'

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if board[row][col] == ' ':
                board[row][col] = turn
                if check_win():
                    print(turn + " wins!")
                    running = False
                elif check_tie():
                    print("It's a tie!")
                    running = False
                else:
                    turn = 'O' if turn == 'X' else 'X'

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Draw Xs and Os
    draw_board()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
