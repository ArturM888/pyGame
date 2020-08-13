import numpy as np
import pygame
import sys
import math

# Gra conncect4 polega na wrzucaniu krążka do kolumny w planszy i spada on na sam dół lub pierwsze wolne miejsce jeśli
# jakieś krążki są już w tej kolumnie

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

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
    return board[ROW_COUNT-1][col] == 0

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

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE  + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()



board = create_board()
running = True
turn = 0

pygame.init()

SQUARESIZE = 100  # wymiar pojedynczego kwadratu, który oznacza jedno pole na planszy

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5) # wymiar promienia koła, które oznacza puste pole na planszy, w którym umieszczamy krążek

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()



        if event.type == pygame.MOUSEBUTTONDOWN:
            # Player 1 Zapytanie o kolumnę do której chce wrzucić krążek
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_peace(board, row, col, 1)

                    if winning_move(board, 1):
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        label = myfont.render("Gracz 1 wygrał", 1, RED)
                        screen.blit(label, (40, 10))
                        running = False



            # # Player 2 Zapytanie o kolumnę do której chce wrzucić krążek
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_peace(board, row, col, 2)

                    if winning_move(board, 2):
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        label = myfont.render("Gracz 2 wygrał", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        running = False

            draw_board(board)

            # Zmiana gracza

            turn += 1
            turn = turn % 2

            if not running:
                pygame.time.wait(3000)