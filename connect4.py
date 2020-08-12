import numpy as np


# Gra conncect4 polega na wrzucaniu krążka do kolumny w planszy i spada on na sam dół lub pierwsze wolne miejsce jeśli
# jakieś krążki są już w tej kolumnie

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
    return board[5][col] == 0

# Sprawdzenie czy już są jakieś krążki w kolumnie i zwrócenie pierwszego wolnego wiersza
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


# Wyświetlenie planszy , odwrócenie flip ponieważ krążki są dodawane od dołu a w macierzy odwrotne liczenie wierszy i kolumn
def print_board(board):
    print(np.flip(board, 0))



board = create_board()
print_board(board)
running = True
turn = 0

while running:
    # Player 1 Zapytanie o kolumnę do której chce wrzucić krążek
    if turn == 0:
        col = int(input("Player 1 Wybierz miejsce (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_peace(board, row, col, 1)



    # Player 2 Zapytanie o kolumnę do której chce wrzucić krążek
    else:
        col = int(input("Player 2 Wybierz miejsce (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_peace(board, row, col, 2)

    print_board(board)


    # Zmiana gracza

    turn += 1
    turn = turn % 2