
N = 8

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queens(board, row):
    if row == N:
        return [board[:]]  # Found one solution

    solutions = []
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solutions.extend(solve_n_queens(board, row + 1))
            board[row] = -1  # backtrack
    return solutions


def print_board(board):
    for i in range(N):
        row = ["Q" if board[i] == j else "." for j in range(N)]
        print(" ".join(row))
    print("\n")


if __name__ == "__main__":
    board = [-1] * N
    solutions = solve_n_queens(board, 0)

    print(f"Total solutions found: {len(solutions)}")

    # Print first 3 solutions only
    for i, sol in enumerate(solutions[:3]):
        print(f"Solution {i+1}:")
        print_board(sol)
