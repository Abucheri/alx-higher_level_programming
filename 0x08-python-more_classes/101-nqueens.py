#!/usr/bin/python3
import sys

"""NQueens function definition."""


def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list of list): The chessboard.
        row (int): The current row.
        col (int): The current column.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row):
    """Solve the N queens problem using a recursive backtracking algorithm.

    Args:
        board (list of list): The chessboard.
        row (int): The current row.

    Returns:
        list of list: List of solutions.
    """
    if row == len(board):
        solution = [[r, c] for r, row in enumerate(board) \
                for c, val in enumerate(row) if val == 1]
        return [solution]

    solutions = []
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            sub_solutions = solve_nqueens(board, row + 1)
            solutions.extend(sub_solutions)
            board[row][col] = 0

    return solutions

def print_solutions(solutions):
    """Print the solutions to the N queens problem.

    Args:
        solutions (list of list): List of solutions.
    """
    for solution in solutions:
        print(solution)

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = solve_nqueens(board, 0)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
