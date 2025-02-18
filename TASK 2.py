# TASK 2.
import math

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def minimax(board, depth, is_max, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

def play_game(moves):
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe! You are 'X' and AI is 'O'")
    print_board(board)

    move_index = 0
    for _ in range(9):
        if check_winner(board):
            break
        if is_moves_left(board):
            if move_index < len(moves):
                row, col = moves[move_index]
                move_index += 1
            else:
                break
            if board[row][col] == " ":
                board[row][col] = "X"
            else:
                print("Invalid move, skipping.")
                continue
        print_board(board)

        if check_winner(board) or not is_moves_left(board):
            break

        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"
        print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    test_moves = [(0, 0), (1, 1), (0, 1), (2, 2), (0, 2)]  # Example predefined moves
    play_game(test_moves)

