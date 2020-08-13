import numpy as np
import pygame
import sys

# Gra conncect4 polega na wrzucaniu krążka do kolumny w planszy i spada on na sam dół lub pierwsze wolne miejsce jeśli
# jakieś krążki są już w tej kolumnie

BLUE = (0,0,255)
BLACK = (0,0,0)

ROW_COUNT = 6
COLUMN_COUNT = 7


# Stworzenie macierzy o podanych wymiarach
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

# Wpisanie krążka do planszy
def drop_peace(board, row, col, piece):
    board[row][col] = piece

# Sprawdzenie czy podana kolumna jest dostępna
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

# Sprawdzenie czy już są jakieś krążki w kolumnie i zwrócenie pierwszego wolnego wiersza
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


# Wyświetlenie planszy , odwrócenie flip ponieważ krążki są dodawane od dołu a w macierzy odwrotne liczenie wierszy i kolumn
def print_board(board):
    print(np.flip(board, 0))

# Sprawdzenie czy gracz wygrał
def winning_move(board, piece):
    # Sprawdzenie wierszy
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Sprawdzenie kolumn
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Sprawdzenie linii prawoukośnych
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Sprawdzenie linii lewoukośnych
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


# Rysowanie planszy w okienku gry
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int( r*SQUARESIZE + SQUARESIZE+SQUARESIZE/2)), RADIUS)

board = create_board()
print_board(board)
running = True
turn = 0

pygame.init()


SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            continue
            # Player 1 Zapytanie o kolumnę do której chce wrzucić krążek
            # if turn == 0:
            #     col = int(input("Player 1 Wybierz miejsce (0-6): "))
            #
            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_peace(board, row, col, 1)
            #
            #         if winning_move(board, 1):
            #             print("Player 1 wygrał")
            #             running = False
            #
            #
            #
            # # Player 2 Zapytanie o kolumnę do której chce wrzucić krążek
            # else:
            #     col = int(input("Player 2 Wybierz miejsce (0-6): "))
            #
            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_peace(board, row, col, 2)
            #
            #         if winning_move(board, 2):
            #             print("Player 2 wygrał")
            #             running = False
            #
            # print_board(board)
            #
            # # Zmiana gracza
            #
            # turn += 1
            # turn = turn % 2