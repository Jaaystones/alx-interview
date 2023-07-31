#!/usr/bin/env python3
"""
N Queens Puzzle Solver

Usage: nqueens N

The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
The program prints every possible solution to the problem,
one solution per line.
"""

import sys


def is_safe(board, row, col, N):
    """ Check if a queen can be placed in the current
    position without attacking others
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    """ Recursive function to find all solutions using backtracking
    """
    def backtrack(row):
        if row == N:
            solutions.append([(i, board[i]) for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * N
    solutions = []
    backtrack(0)
    return solutions


def print_solutions(solutions):
    """ Format and print the solutions
    """
    for solution in solutions:
        formatted_solution = str(solution).replace("), ", "], [")\
                .replace("(", "[").replace(")", "]")
        print(formatted_solution)


def main():
    """ Check for the correct number of arguments
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    """ Parse and validate N
    """
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """ Solve and print the solutions
    """
    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
