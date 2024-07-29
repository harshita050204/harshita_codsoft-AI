def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    for row in board:
        if any([spot == " " for spot in row]):
            return False
    return True
def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval
def get_ai_move(board):
    best_score = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = "X"
    ai_player = "O"
    current_player = human_player

    while True:
        print_board(board)
        if current_player == human_player:
            move = input("Enter your move (row and column): ").split()
            row, col = int(move[0]), int(move[1])
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = human_player
            if check_win(board, human_player):
                print_board(board)
                print("Congratulations! You win!")
                break
            current_player = ai_player
        else:
            move = get_ai_move(board)
            board[move[0]][move[1]] = ai_player
            if check_win(board, ai_player):
                print_board(board)
                print("AI wins! Better luck next time.")
                break
            current_player = human_player

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
