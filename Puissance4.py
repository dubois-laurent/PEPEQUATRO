# Initialisation du plateau de jeu (6 lignes x 7 colonnes)
ROWS = 6
COLS = 7
EMPTY = -1

# Création du tableau initial avec des valeurs par défaut
def create_board(rows, cols, default_value):
    return [[default_value for _ in range(cols)] for _ in range(rows)]

# Affichage du plateau
def print_board(board):
    for row in board:
        print(" | ".join(
            "X" if cell == 1 else "O" if cell == 2 else "." for cell in row
        ))
    print("-" * (COLS * 4 - 1))

# Vérifie si une colonne est jouable
def is_valid_column(board, col):
    return board[0][col] == EMPTY

# Trouve la première ligne vide dans une colonne
def get_next_open_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return None

# Place un jeton sur le plateau
def drop_piece(board, row, col, player):
    board[row][col] = player

# Vérifie si un joueur a gagné
def check_victory(board, player):
    # Vérifie les lignes
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Vérifie les colonnes
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Vérifie les diagonales descendantes
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Vérifie les diagonales montantes
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

# Évalue le plateau pour un joueur
def evaluate_board(board, player):
    score = 0

    # Bonus pour les cases centrales
    center_col = [board[row][COLS // 2] for row in range(ROWS)]
    score += center_col.count(player) * 3

    # Vérifie les lignes,
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = [board[row][col + i] for i in range(4)]
            score += evaluate_window(window, player)

    # Vérifie les colonnes
    for col in range(COLS):
        for row in range(ROWS - 3):
            window = [board[row + i][col] for i in range(4)]
            score += evaluate_window(window, player)

    # Vérifie les diagonales descendantes
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, player)

    # Vérifie les diagonales montantes
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row - i][col + i] for i in range(4)]
            score += evaluate_window(window, player)

    return score

# Évalue une fenêtre de 4 cases
def evaluate_window(window, player):
    score = 0
    opponent = 2 if player == 1 else 1

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

# Vérifie si le plateau est plein
def is_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

# Implémente l'algorithme MinMax
def minimax(board, depth, alpha, beta, maximizing_player, player):
    opponent = 2 if player == 1 else 1

    # Vérifie si le joueur actuel ou l'adversaire a gagné
    if check_victory(board, player):
        return (None, 1000000 if maximizing_player else -1000000)
    if check_victory(board, opponent):
        return (None, -1000000 if maximizing_player else 1000000)
    if is_full(board) or depth == 0:
        return (None, evaluate_board(board, player))

    if maximizing_player:
        value = float('-inf')
        best_col = None
        for col in range(COLS):
            if is_valid_column(board, col):
                row = get_next_open_row(board, col)
                temp_board = [r.copy() for r in board]
                drop_piece(temp_board, row, col, player)

                # Vérifie si ce coup permet à l'IA de gagner immédiatement
                if check_victory(temp_board, player):
                    return (col, 1000000)

                _, new_score = minimax(temp_board, depth - 1, alpha, beta, False, player)
                if new_score > value:
                    value = new_score
                    best_col = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return best_col, value
    else:
        value = float('inf')
        best_col = None
        for col in range(COLS):
            if is_valid_column(board, col):
                row = get_next_open_row(board, col)
                temp_board = [r.copy() for r in board]
                drop_piece(temp_board, row, col, opponent)

                _, new_score = minimax(temp_board, depth - 1, alpha, beta, True, player)
                if new_score < value:
                    value = new_score
                    best_col = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
        return best_col, value

# Exemple d'utilisation
if __name__ == "__main__":
    board = create_board(ROWS, COLS, EMPTY)
    game_over = False
    turn = 0

    while not game_over:
        print_board(board)

        if turn == 0:
            col = int(input("Joueur 1 choisissez une colonne (0-6) : "))
            if is_valid_column(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                if check_victory(board, 1):
                    print_board(board)
                    print("Joueur 1 gagne !")
                    game_over = True
        else:
            print("Claire réfléchit...")
            col, _ = minimax(board, 4, float('-inf'), float('inf'), True, 2)
            if col is not None and is_valid_column(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                if check_victory(board, 2):
                    print_board(board)
                    print("Claire gagne !")
                    game_over = True

        if is_full(board):
            print("Match nul !")
            print_board(board)
            game_over = True

        turn = (turn + 1) % 2