import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]


def minimax(board, depth, is_maximizing, symbol, opponent_symbol):
    winner = check_winner(board)
    if winner == symbol:
        return 1
    elif winner == opponent_symbol:
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row, col in get_empty_positions(board):
            board[row][col] = symbol
            score = minimax(board, depth + 1, False, symbol, opponent_symbol)
            board[row][col] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_positions(board):
            board[row][col] = opponent_symbol
            score = minimax(board, depth + 1, True, symbol, opponent_symbol)
            board[row][col] = " "
            best_score = min(best_score, score)
        return best_score


def computer_move(board, symbol, opponent_symbol):
    best_score = -float("inf")
    best_move = None
    for row, col in get_empty_positions(board):
        board[row][col] = symbol
        score = minimax(board, 0, False, symbol, opponent_symbol)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    symbols = ["X", "O"]
    current_player = 0

    print("Tic-Tac-Toe: Perfect Play (Always a Tie)")
    print_board(board)

    while True:
        print(f"\nPlayer {symbols[current_player]}'s turn.")
        row, col = computer_move(
            board, symbols[current_player], symbols[1 - current_player]
        )
        board[row][col] = symbols[current_player]
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player


if __name__ == "__main__":
    main()
